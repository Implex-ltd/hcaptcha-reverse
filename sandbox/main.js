const { JSDOM, ResourceLoader } = require("jsdom");
const fs = require('fs');
const express = require('express');

const fileContent = fs.readFileSync('cleaned.txt', 'utf8');
const lines = fileContent.split('\n').filter(line => line.trim() !== '');

function get_fp() {
    const randomIndex = Math.floor(Math.random() * lines.length);
    const randomLine = lines[randomIndex];
    return randomLine
}

const app = express();
const port = process.argv[2];;

app.use(express.json());

const NUM_CONTEXTS = 10;
const jsdomContexts = [];

const hswBindScript = fs.readFileSync(__dirname + "/hsw_bind.js", "utf-8");

for (let i = 0; i < NUM_CONTEXTS; i++) {
    const { window } = new JSDOM(``, {
        includeNodeLocations: false,
        runScripts: "dangerously",
        pretendToBeVisual: false,
        resources: new ResourceLoader({
            userAgent: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36`
        })
    });
    window.eval(hswBindScript);
    jsdomContexts.push(window);
}

app.post('/n', async (req, res) => {
    const startTime = performance.now();
    const { jwt: token, fp: fpb64 } = req.body;

    const currentContext = jsdomContexts.shift();
    jsdomContexts.push(currentContext);

    try {
        let fp = fpb64
        const result = await currentContext.hsw(token, fp);

        const endTime = performance.now();
        console.log(`(took ${(endTime - startTime).toFixed(2)} ms, chars: ${result.length})`);
        res.send(result);
    } catch (error) {
        console.error(error);
        res.status(401).json({ error: 'Invalid JWT' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
