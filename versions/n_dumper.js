/*
    Dump WASM memory and look for N data.
    - Doesnt' work for versions above 1.40.20 (you have to find memories.xxx var name)
*/

(() => {
    const del_1 = `{"proof_spec":{"difficulty":`
    const del_2 = `]]}`

    function dump() {
        if (memories.$$a.buffer === undefined) {
            console.log("Buffer not found, Please execute while HSW is running.")
            return
        }

        const u8 = new Uint8Array(memories.$$a.buffer) // as example 1.40.21 would be memories.$Za.buffer
        const buff = new TextDecoder('utf-8').decode(u8)

        if (!buff.includes(del_1) && !buff.includes(del_2)) {
            console.log("N data not found.")
            console.log(buff)
            return
        }

        try {
            let n_data = JSON.parse(`${del_1}${decodedString.split(del_1)[1].split(del_2)[0]}${del_2}`)

            console.log(n_data)
        } catch (err) {
            console.log('N data is not complete.')
            console.log(buff)
        }
    }

    function main() {
        console.clear()
        dump()
    }

    main()
})()