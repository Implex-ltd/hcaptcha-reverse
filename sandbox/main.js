const {JSDOM, ResourceLoader} = require("jsdom");
const fs = require('fs')

const {window} = new JSDOM(``, {
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

async function eval_hsw(jwt) {
    window.hsw(jwt).then(function (result) {
        return {
            token: result,
            size: result.length
        }
    })
}

(async () => {
    console.log(eval_hsw("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiJUZllCanIrVE1tMUs2WENNcDgwM09BbTRvaGh2OWNqNWErQmF4UjZ5NWd6WHFzQi9pN1FtZHdZWkcvek9kNXY5Nm5oVll5RmFzamRjcUUxSnBSQm94NmN5YnVuLzRuQUVDT3UrcmVyK21LdVdRR0VIdlJHNlNUeG84UTVPZG04cnFWVXdDbnVOZ0c4ZExKcWFObGtlOVhTdEZRVGo1YWhocXZ1R0I5R2JpRjd0akVZRDNNWGNjVzRMcnc9PXFwemIxckIxZ1JUMlBzbUoiLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvMzE4OTJmYiIsImUiOjE2OTQ3NjE1MDYsIm4iOiJoc3ciLCJjIjoxMDAwfQ.rXelXmavm3mI_sYAD9g7PbuGZ0JGQEB3ZiXUK-ZlVI_966XQDNYfczXG4gcWDdY5y7xLRwxfvUICMiPe7uVas3bULkspBzrezd5nJdKmt0jSHQGBEBXSZPDWMBpZkz8JTAfELuw5yoOIfr5X7si4ZbOeilc7Ex5YkjXizz9boUY"))
})()