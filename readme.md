# HCaptcha reverse engineer

## Fingerprint events

> `fingerprint_events` is parsed output of fingerprinting script, somes data are hashed.
> Final output is used into n data.
> Hash algorithm is xxHash3 (sixty_four.rs). 

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

### String integrity check

[This script](https://gist.github.com/nikolahellatrigger/a8856463170fbe3596569977148ebaf4) is used to "encrypt" somes data into fingerprint_event such as:
    - webgl vendor + renderer
    - browser performance
    - browser timezone
    
I think it's used to verify the data is authentic / non duplicated (output is different each time you run the function)

## Lib used by WASM

- https://crates.io/crates/rand_chacha/0.2.2
- https://crates.io/crates/cipher/0.3.0
- https://crates.io/crates/ctr/0.8.0
- https://crates.io/crates/rust-hashcash/0.3.3
- https://crates.io/crates/aes/0.7.5
- https://crates.io/crates/js-sys/0.3.52
- https://crates.io/crates/twox-hash/1.6.0

## Stamp

Hcaptcha is using [hashcash](https://crates.io/crates/rust-hashcash/0.3.3) algorithm to generate stamp value with custom date format (`2006-01-02`), bits is set by using the difficulty present into the JWT 

## Fingerprint hash

Hcaptcha is using [xxHash3 (sixty_four.rs)](https://crates.io/crates/twox-hash/1.6.0) algorithm with custom seed (`5575352424011909552`) to create unique hash of somes properties

## Rand

Rand is a `CRC-32` checksum hash of the N payload in json format, it's used to check the payload integrity if you edited it from memory etc...
Format: `[math.random, crc-32 * 2.3283064365386963e-10]` (`table: 79764919`)

## Encryption

Final payload is encrypted using `AES-256-GCM` (`256 bits key`)