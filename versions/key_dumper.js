
/**
 * Dump all memory chunk 32 by 32 bits and retrieve string that start by "c" or "C" (first char of encryption-key)
 */

(() => {
    const uint8Array = new Uint8Array(memories.$memory.buffer);
    let found = []

    function parseRegion(offset, len) {
        const subArray = uint8Array.subarray(offset, offset + len);

        if (subArray[0] != 67 && subArray[0] != 99) return;

        const decodedString = new TextDecoder('utf-8').decode(subArray);
        console.log(decodedString)

        let out = []
        subArray.forEach(b => {
            out.push(b)
        })
        found.push(out)
    }


    for (let i = 0; i < uint8Array.length; i += 32) {
        parseRegion(i, 32)
    }

    console.log(found)
})();

