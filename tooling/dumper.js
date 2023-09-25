(() => {
    function dump() {
        const buff = memories.$memory.buffer;
        const uint8Array = new Uint8Array(buff);

        const decodedString = new TextDecoder('utf-8').decode(uint8Array);

        let str = []

        for (let i = 0; i < decodedString.length; i++) {
            if (decodedString[i] == '\u001b' || decodedString[i] == '\u0015' || decodedString[i] == '\u0017' || decodedString[i] == '\u0018' || decodedString[i] == '\u0011' || decodedString[i] == '\b' || decodedString[i] == '\u000b' || decodedString[i] == '\u000e' || decodedString[i] == '\u001e' || decodedString[i] == '\r' || decodedString[i] == '\u0019' || decodedString[i] == '\f' || decodedString[i] == '�' || decodedString[i] == '\n' || decodedString[i] == '' || decodedString[i] == '' || decodedString[i] == '\u001a' || decodedString[i] == '\u0016' || decodedString[i] == '\u0010' || decodedString[i] == '\u0012' || decodedString[i] == '\u0013' || decodedString[i] == '\u001f' || decodedString[i] == '\u0000' || decodedString[i] == '\u0001' || decodedString[i] == '\u0002' || decodedString[i] == '\u0003' || decodedString[i] == '\u0004' || decodedString[i] == '\u0005' || decodedString[i] == '\u0006' || decodedString[i] == '\u0007') continue;
            str.push(decodedString[i]);
        }

        console.log(str)
        console.log(str.join(''));
    }

    function main() {
        console.clear()
        dump()
    }

    main()
})()