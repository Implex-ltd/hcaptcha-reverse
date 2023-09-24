const uint8Array = new Uint8Array(memories.$memory.buffer);

const decodedString = new TextDecoder('utf-8').decode(uint8Array);

let d1 = `{"proof_spec"`
let d2 = `]]}`

let n = `${d1}${decodedString.split(d1)[1].split(d2)[0]}${d2}`

console.log(n);