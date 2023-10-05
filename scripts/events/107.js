GA = z('5de', function (A) {
    A('f99', [
        window.screen.width,
        window.screen.height,
        window.screen.availWidth,
        window.screen.availHeight,
        window.screen.colorDepth,
        window.screen.pixelDepth,
        !!document.createEvent('TouchEvent') && ontouchstart in window,
        navigator.maxTouchPoints,
        window.devicePixelRatio,
        window.outerWidth,
        window.outerHeight,
        matchMedia(
            '(device-width: '.concat(window.screen.availWidth, 'px) and (device-height: ').concat(window.screen.height, 'px)')
        ).matches,
        matchMedia('(-webkit-device-pixel-ratio: '.concat(1, ')')).matches,
        matchMedia('(resolution: '.concat(1, 'dppx)')).matches,
        matchMedia('(-moz-device-pixel-ratio: '.concat(1, ')')).matches,
    ])
})
