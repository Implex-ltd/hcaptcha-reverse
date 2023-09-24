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


/*
window.setInterval(() => {
    try {
        console.log(window.pg)

        const uint8Array = new Uint8Array(window.pg);

        const decodedString = new TextDecoder('utf-8').decode(uint8Array);

        let d1 = `{"proof_spec"`
        let d2 = `]]}`

        let n = `${d1}${decodedString.split(d1)[1].split(d2)[0]}${d2}`

        console.log(n);
    } catch (err) { console.log(err) }
}, 1);
*/

async function eval_hsw(jwt) {
    await window.hsw(jwt).then(function (result) {
        console.log(result, result.length)
    })
}

(async () => {
    let result = await eval_hsw("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiJLOE94d0NsNFY4Zm5Gbk43QmY4MVJDRmNMaTRjMFFPNisyRVdWWEtFVkVXS2MyaTRwblJOOGUxYTNNZ2pmd0V0WlBiUWEyMm5Fd0VxZWc1Zjd5dzR2L05MbUlOaGlwaUNhMjc1d2wvYlVxNndvZmlRWHM3SDc2Sld0ek1GTGllZXhlcHlNd09UdzRWSkJyUlVUSjAvZC9hMkdDV2RNWHJmN2FSQjJJYzV1V3B0Qm9rcTRsSlR1OHg3blE9PW5BdVdBTlZ3RTFPUU9FNGciLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvYmY2MDBiZCIsImkiOiJzaGEyNTYtTmxDelZxSlVqYnFaWUxoYXRJKzZUVStDVzBOb3BUbVh6bGdmL21oMjk1Zz0iLCJlIjoxNjk1NDk0Nzk3LCJuIjoiaHN3IiwiYyI6MTAwMH0.rFAiBCuPPQ_lTsRCPhQUlDL7qbe_lAMZ8POJPJKIzAmiAbXczKlIUh7z5y43OdysTfH1odwrWGZUpVQK30_3yrphiTcHJGVxlb7fZEdJUJwXNBVKBjAZ6OoKh10rHUpquNLzQWkFNc5fQ7-pwkTPwx3qsaVh0pH3JTiysKZKEVY")
})()