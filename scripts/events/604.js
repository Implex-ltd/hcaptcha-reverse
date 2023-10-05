var out = require("bd6", function (assert) {
    var result;

    assert(
        'getElementById',
        [
            navigator.appVersion,
            navigator.userAgent,
            navigator.deviceMemory,
            navigator.hardwareConcurrency,
            navigator.language,
            navigator.languages,
            navigator.platform,
            navigator.oscpu,
            (navigator.userAgentData.brands || []).map(function (brand) {
                return "".concat(brand.brand, " ").concat(brand.version);
            }),
            navigator.userAgentData.mobile,
            navigator.userAgentData.platform,
            navigator.mimeTypes.length,
            (navigator.plugins || []).length,
            navigator.pdfViewerEnabled,
            "downlinkMax" in navigator.connection,
            null == navigator.connection ? void 0 : navigator.connection.rtt,
            navigator.webdriver,
            null === (result = window.clientInformation) || void 0 === result ? void 0 : result.webdriver,
            "share" in navigator,
            "object" == typeof "keyboard" in navigator && navigator.keyboard ? String("keyboard" in navigator && navigator.keyboard) : "keyboard" in navigator && navigator.keyboard,
            "brave" in navigator,
            "duckduckgo" in navigator
        ]
    );
});
