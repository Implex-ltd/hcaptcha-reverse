# HCaptcha reverse engineer

```
this repo (and more generally all those linked to implex) are the result of countless hours of work, a lot of learning and new things.
Take the time to look and learn, instead of copying without thinking, because it won't work. If you need a developer, contact me.
```

## String integrity check

[This script](https://gist.github.com/nikolahellatrigger/a8856463170fbe3596569977148ebaf4) is used to "encode" somes data into `fingerprint_event` field such as:
    
    - webgl vendor + renderer
    - browser performance
    - browser timezone
    
I think it's used to verify the data is authentic / non duplicated (output is different each time you run the function)

## Lib used by WASM

- https://crates.io/crates/rand_chacha/0.2.2 (encryption)
- https://crates.io/crates/cipher/0.3.0 (encryption)
- https://crates.io/crates/ctr/0.8.0 (encryption)
- https://crates.io/crates/rust-hashcash/0.3.3 (stamp)
- https://crates.io/crates/aes/0.7.5 (encryption)
- https://crates.io/crates/js-sys/0.3.52 (javascript)
- https://crates.io/crates/twox-hash/1.6.0 (hash)

## Stamp (proof of work)

[Hashcash](https://crates.io/crates/rust-hashcash/0.3.3) algorithm is used to generate stamp value as a POW with custom date format (`2006-01-02`), bits is set by using the difficulty present into the JWT 

## Fingerprint hash

[XxHash3 (sixty_four.rs)](https://crates.io/crates/twox-hash/1.6.0) algorithm is used with custom seed (`5575352424011909552`) to create unique hash of 15 unique properties such as:

    - Html DOM
    - Webgl properties
    - Css properties
    - Javascript window functions
    - ...
    

## Rand

Rand is a `CRC-32` checksum hash of the N payload in json format, it's used to check the payload integrity if you edited it from memory etc...
Format: `[math.random, crc-32 * 2.3283064365386963e-10]` (`table: 79764919`)

## Encryption

Final payload is encrypted using `AES-256-GCM` (`256 bits key`)

## Fingerprint events

> `fingerprint_events` is parsed output of fingerprinting script, somes data are hashed.
> Final output is used into n data.
> Hash algorithm is xxHash3 (sixty_four.rs). 

### Raw javascript fp output

- [1.40.10](https://gist.github.com/nikolahellatrigger/65ff078faa990db653adb2d6052be6b0)
- [1.39.0](https://gist.github.com/nikolahellatrigger/b34456fdc7383ffbb26246bb9db28b7e)

| id     | type                                                                   | type      | hashed    | fp_raw                                                                              |
| ------ | ---------------------------------------------------------------------- | --------- | --------- | ----------------------------------------------------------------------------------- |
| `3`    |                                                                        | `float64` | **false** | [x](https://x.com)                                                                  |
| `1902` | `57`                                                                   | `int`     | **false** | [x](https://x.com)                                                                  |
| `1901` | math fingerprint wich give different result + err between device       | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `1101` | canvas fingerprint hash of the image (`data:image/png;base64,...`)     | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `1103` | `[255,255,255,255,192,192,192,255,244,244,244,255,53,53,53,255]`       | `array`   | **true**  | [x](https://x.com)                                                                  |
| `1105` | `[14,4,1,41.3203125,17,4,44.2890625]`                                  | `array`   | **true**  | [x](https://x.com)                                                                  |
| `1107` | `[274.609375,266,274.609375,266,274.609375,266,274.609375,....]`       | `array`   | **false** | [x](https://x.com)                                                                  |
| `201`  | hash of `1107`                                                         |           | **false** | [x](https://x.com)                                                                  |
| `211`  | audio fingerprint                                                      | `array`   | **true**  | [x](https://x.com)                                                                  |
| `3401` | page HTML Tree                                                         |           | **true**  | [x](https://x.com)                                                                  |
| `3403` | Link of hcaptcha.js                                                    |           | **false** | [x](https://x.com)                                                                  |
| `803`  | `[1,4,5,7,9,12,20,21,24,25,29]`                                        | `array`   | **false** | [x](https://x.com)                                                                  |
| `604`  | `[n.appv,n.ua,n.mem,n.hwconc,n.lang,n.langs,n.platform,n.cpu,versin]`  | `array`   | **false** | [link](https://gist.github.com/nikolahellatrigger/c4d6cf4ddb0ab219c38ddd133dc772eb) |
| `2801` | probably webgl related                                                 | `u8`      | **true**  | [x](https://x.com)                                                                  |
| `2805` | hash of `2801`                                                         | `array`   | **false** | [x](https://x.com)                                                                  |
| `107`  | `[s.w,s.h,s.aw,s.ah,s.cd,s.pd,event,n.maxtp,w.dpr,w.ow,w.oh...]`       | `array`   | **false** | [link](https://gist.github.com/nikolahellatrigger/ea00832b010c0db8f0a0d5ca0d467072) |
| `302`  | css default colors                                                     | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `303`  | `fonts`                                                                | `array`   | **false** | [x](https://x.com)                                                                  |
| `301`  | CSS properties list                                                    | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `304`  | length of CSS properties                                               | `int`     | **false** | [x](https://x.com)                                                                  |
| `1401` | `timezone`                                                             | `string`  | **false** | [x](https://x.com)                                                                  |
| `1402` | `[timezone,x,x,new Date("1/1/1970").getTimezoneOffset(),x,n.lang]`     | `array`   | **false** | [x](https://x.com)                                                                  |
| `1403` | timezone "encrypted"                                                   | `array`   | **false** | [x](https://x.com)                                                                  |
| `3504` |                                                                        | `float64` | **false** | [x](https://x.com)                                                                  |
| `3501` | navigation timestamp                                                   | `array`   | **false** | [x](https://x.com)                                                                  |
| `3503` | current unix timestamp                                                 | `int`     | **false** | [x](https://x.com)                                                                  |
| `3502` |                                                                        | `float64` | **false** | [x](https://x.com)                                                                  |
| `3505` |                                                                        | `float64` | **false** | [x](https://x.com)                                                                  |
| `401`  | browser properties hash                                                | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `402`  | length of windows properties                                           | `int`     | **false** | [x](https://x.com)                                                                  |
| `407`  | browser keys?                                                          | `array`   | **false** | [x](https://x.com)                                                                  |
| `412`  | `[true,true,true,true,true,true,true,true,true,true,...]`              | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `2402` | `[webgl_vendor, webgl_renderer]`                                       | `array`   | **false** | [x](https://x.com)                                                                  |
| `2420` | `[encrypt_webgl_vendor, encrypt_webgl_renderer]` "encrypted"           | `array`   | **false** | [x](https://x.com)                                                                  |
| `2403` | `[webgl2_vendor, webgl2_renderer]`                                     | `array`   | **false** | [x](https://x.com)                                                                  |
| `2401` | WebGL properties hash                                                  | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `2408` | `!!navigator.webdriver`                                                | `bool`    | **false** | [x](https://x.com)                                                                  |
| `2407` | Math fingerprint of 28 first fibonacci number                          | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `2409` | probably webgl related                                                 | `array`   | **false** | [x](https://x.com)                                                                  |
| `2410` | `[16,1024,4096,7,12,120,[23,127,127]]`                                 | `array`   | **false** | [x](https://x.com)                                                                  |
| `2411` | `[32767,32767,16384,8,8,8]`                                            | `array`   | **false** | [x](https://x.com)                                                                  |
| `2412` | `[1,1024,1,1,4]`                                                       | `array`   | **false** | [x](https://x.com)                                                                  |
| `2413` | probably webgl related                                                 | `array`   | **false** | [x](https://x.com)                                                                  |
| `2414` | `[16384,32,16384,2048,2,2048]`                                         | `array`   | **false** | [x](https://x.com)                                                                  |
| `2415` | `[4,120,4]`                                                            | `array`   | **false** | [x](https://x.com)                                                                  |
| `2416` | `[24,24,65536,212988,200704]`                                          | `array`   | **false** | [x](https://x.com)                                                                  |
| `2417` | `[16,4095,30,16,16380,120,12,120,[23,127,127]]`                        | `array`   | **false** | [x](https://x.com)                                                                  |
| `3800` | CSP (disabled)                                                         | `error`   | **false** | [x](https://x.com)                                                                  |
| `1302` | `[0,1,2,3,4]`                                                          | `array`   | **false** | [x](https://x.com)                                                                  |
| `901`  | All browser voices hash                                                | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `905`  | Browser voice enabled                                                  | `array`   | **false** | [x](https://x.com)                                                                  |
| `3210` | `[143254600089,143254600089,null,null,4294705152,true,true,true,null]` | `array`   | **false** | [x](https://x.com)                                                                  |
| `3211` | first arg of performance **3210** "encrypted"                          | `array`   | **false** | [x](https://x.com)                                                                  |
| `702`  | `[os.name, os.version, null, os.bits, os.arch, navigator.version]`     | `array`   | **false** | [x](https://x.com)                                                                  |
| `2001` | Permissions hash                                                       | `u64`     | **true**  | [x](https://x.com)                                                                  |
| `2002` | Notifications permissions                                              | `array`   | **false** | [x](https://x.com)                                                                  |
| `0`    |                                                                        | `float64` | **false** | [x](https://x.com)                                                                  |

## Sandbox

Sandbox is fast way to encrypt own HSW without retrieving stuff as encryption-key, xxHash nonce and stuff that change, or if new update happen and you don't reversed it yet.
You can build custom HSW wasm using [builder](https://github.com/Implex-ltd/hcaptcha-reverse/blob/main/src/main.py) / [WABT](https://github.com/WebAssembly/wabt) tools.

HSW usualy take less than 10ms to execute. (you have to remove all fingerprints from array)

### how sandbox work ?

the sandbox executes a custom hsw containing a hand-modified WASM which adds the payload to be encrypted to the end of memory and returns the pointer to encrypt our payload and not the one generated by hcaptcha. It's kinda smart isn't it ?

### Wasm hook
```wasm
;; new modules import
(func $./client_bg.js.inject (;31;) (import "./client_bg.js" "inject") (param i32 i32))
(func $./client_bg.js.getLen (;56;) (import "./client_bg.js" "getLen") (result i32))
(func $./client_bg.js.getPtr (;75;) (import "./client_bg.js" "getPtr") (result i32))

;; edited function: func 150 (1.39) // func 152 (1.40.10)

;; JSON is built above...
local.set $var7
local.get $var5
i32.const 32
i32.add

local.get $var6 ;; load len of the JSON
local.get $var7 ;; load ptr of the JSON
call $./client_bg.js.inject ;; append custom payload into memory
      
call $./client_bg.js.getLen
local.set $var6 ;; ^+ get the payload len and overwrite original one
      
call $./client_bg.js.getPtr
local.set $var7 ;; ^+ get the payload ptr and overwrite original one

call $func211 ;; continue wasm with out custom payload...
```

### Hsw hook
```js

let jlen = 0
let jptr = 0
let fp_json_curr = {}

// this append over and over and can lead to memory leak // 100% RAM but it's working
function appendJsonToMemory(pp) {
    const to_inject = new TextEncoder().encode(pp);
    const buffer = M.memory.buffer;

    const currentSize = buffer.byteLength;
    const requiredSize = currentSize + to_inject.length;

    M.memory.grow(Math.ceil((requiredSize - currentSize) / 65536));

    const updatedBuffer = M.memory.buffer;
    const memoryView = new Uint8Array(updatedBuffer);

    memoryView.set(to_inject, currentSize);

    return {
        ptr: currentSize,
        len: to_inject.length
    };
}

inject: function (len, ptr) {
    try {
        /*
            - This part was used to get the stamp + rand when it was not fully reversed

            let parsed = JSON.parse(__getStrFromWasm(ptr, len))
            fp_json_curr.stamp = parsed.stamp
            fp_json_curr.rand = parsed.rand
        */

        console.log(JSON.stringify(fp_json_curr))
        const data = appendJsonToMemory(JSON.stringify(fp_json_curr));

        // save new ptr + len
        jlen = data.len
        jptr = data.ptr
        } catch (err) { console.log(err) }
},

getPtr: function () {
    return jptr
},

getLen: function () {
    return jlen
},
```
