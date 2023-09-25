const { JSDOM, ResourceLoader } = require("jsdom");
const fs = require('fs')

const { window } = new JSDOM(``, {
    url: "https://discord.com",
    referrer: "https://discord.com",
    contentType: "text/html",
    includeNodeLocations: false,
    runScripts: "dangerously",
    pretendToBeVisual: true,
    resources: new ResourceLoader({
        userAgent: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36`
    })
});

window.eval(fs.readFileSync(__dirname + "/assets/clean_hsw.js", "utf-8"))


Object.defineProperty(window, 'matchMedia', {
    writable: true,
    value: (query) => ({
        matches: false,
        media: query,
        addListener: () => { },
        removeListener: () => { },
    }),
});

class LocalStorageMock {
    constructor() {
        this.store = {};
    }

    clear() {
        this.store = {};
    }

    getItem(key) {
        return this.store[key] || null;
    }

    setItem(key, value) {
        this.store[key] = value;
    }
}

Object.defineProperty(window, 'localStorage', {
    value: new LocalStorageMock(),
});

class PerformanceMock {
    constructor() {
        this.store = {
            resource: [],
        };
    }

    setResourceEntries(url) {
        this.store.resource.push({
            name: url.trim(),
            duration: 450,
        });
    }

    getEntriesByType(type) {
        return this.store[type];
    }
}

Object.defineProperty(window, 'performance', {
    value: new PerformanceMock(),
});

async function eval_hsw(jwt) {
    await window.hsw(jwt).then(function (result) {
        console.log(result, result.length)
    })
}

(async () => {
    let result = await eval_hsw("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiI0VExPTVZ1Nm9LTlRvcVBNcWpZOUtSTWtya1p4MmR2bHZzbWdMclU2bHVkM3ZiTVhXbitpWWs3MDQzL2pkNGdFaG1WZG9sakdrNXRneFZJNlVrQndRbi84eEsrWTlTMnV5MzJ4T2l0WENSRXRrNS9LWTVrQ0JySnRUUHdzR3BCbXQ2SEhkUDU4cmpUcU9OV1oxWGIrakdtanVKVVNyRXpEOXYzeVgrdnVhUVg5MkdjdCtCTlQydTNwTGc9PW84VURuMjZaSlFvYTZlYWciLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvYmY2MDBiZCIsImkiOiJzaGEyNTYtTmxDelZxSlVqYnFaWUxoYXRJKzZUVStDVzBOb3BUbVh6bGdmL21oMjk1Zz0iLCJlIjoxNjk1NTk1MTExLCJuIjoiaHN3IiwiYyI6MTAwMH0.XCoVemNFxU0MQ2xYm5ir687lUDeG08dbE6q5VxoddHXEyZa0-OoOpkJgQHP0KftmYOvtXOzgHngnJr-95GzXXHmiIcUQPkT7lvfLZ4I5_dqvANIMUq1h0O2vq1ZXkeOs4DBKRKsY20fPE5rtpTk6v-I4J9dljCi_UjHAZtHQMlk")
})()