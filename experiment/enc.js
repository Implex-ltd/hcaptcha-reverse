function getRandNum(A, g) {
    return Math.floor(Math.random() * (g - A + 1)) + A
}

function __Enc(A) {
    if (null == A) {
        return null
    }

    let inputArr = Array.from({ length: 13 }, function () {
        return String.fromCharCode(getRandNum(65, 90))
    }).join('')

    let rand_a = getRandNum(1, 26)

    let encodedResult = A.split(' ').reverse().join(' ').split('').reverse().map(function (A) {
        if (!A.match('/[a-z]/i')) {
            return A
        }

        let I = hA.indexOf(A.toLowerCase())
        let B = hA[(I + rand_a) % 26]

        if (A === A.toUpperCase()) {
            return B.toUpperCase();
        } else {
            return B;
        }
    }).join('')

    let b64out = btoa(encodeURIComponent(encodedResult)).split('').reverse().join('')

    console.log(b64out)

    let b64randLen = getRandNum(1, b64out.length - 1)

    return [
        (b64out.slice(b64randLen, b64out.length) + b64out.slice(0, b64randLen)).replace(
            new RegExp('['.concat(inputArr).concat(inputArr.toLowerCase(), ']'), 'g'),
            
            function (A) {
                if (A === A.toUpperCase()) {
                    return A.toLowerCase();
                } else {
                    return A.toUpperCase();
                }
            }
        ),
        rand_a.toString(16),
        b64randLen.toString(16),
        inputArr,
    ]
}


for ( var i = 0; i < 5; i++ ) {
    console.log(__Enc("Europe/Paris"))
}