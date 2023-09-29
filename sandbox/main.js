const { JSDOM, ResourceLoader } = require("jsdom");
const fs = require('fs');

const express = require('express');

const app = express();
const port = 1234;

app.use(express.json());

// Create an array to hold multiple JSDOM contexts
const jsdomContexts = [];
const NUM_CONTEXTS = 2; // Adjust the number of contexts as needed

for (let i = 0; i < NUM_CONTEXTS; i++) {
    const { window } = new JSDOM(``, {
        contentType: "text/html",
        includeNodeLocations: false,
        runScripts: "dangerously",
        pretendToBeVisual: true,
        resources: new ResourceLoader({
            userAgent: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36`
        })
    });
    jsdomContexts.push(window);
}

app.post('/n', (req, res) => {
    const { jwt: token } = req.body;

    // Rotate through the JSDOM contexts
    const currentContext = jsdomContexts.shift();
    jsdomContexts.push(currentContext);

    try {
        currentContext.eval(fs.readFileSync(__dirname + "/hsw_bind.js", "utf-8"));
        currentContext.hsw(token).then(function (result) {
            console.log('got', result.length)
            res.send(result);
        });
    } catch (error) {
        console.error(error);
        res.status(401).json({ error: 'Invalid JWT' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
