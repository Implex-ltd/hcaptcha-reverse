 # HCaptcha reverse engineer

## Fingerprint events

> `fingerprint_events` is parsed output of fingerprinting script, somes data are hashed.
> Final output is used into n data.

| id     | type                                                                  | type     | hashed    | fp_raw                                                                              |
| ------ | --------------------------------------------------------------------- | -------- | --------- | ----------------------------------------------------------------------------------- |
| `3`    |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `1902` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `1901` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `1101` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `1103` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `1105` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `1107` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `201`  |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `211`  |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `3401` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `3403` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `803`  |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `604`  | `[n.appv,n.ua,n.mem,n.hwconc,n.lang,n.langs,n.platform,n.cpu,versin]` |          | **false** | [link](https://gist.github.com/nikolahellatrigger/c4d6cf4ddb0ab219c38ddd133dc772eb) |
| `2801` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `2805` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `107`  | `[s.w,s.h,s.aw,s.ah,s.cd,s.pd,event,n.maxtp,w.dpr,w.ow,w.oh...]`      | `array`  | **false** | [link](https://gist.github.com/nikolahellatrigger/ea00832b010c0db8f0a0d5ca0d467072) |
| `302`  |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `303`  | `fonts`                                                               | `array`  | **false** | [x](https://x.com)                                                                  |
| `301`  |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `304`  | length of CSS properties                                              | `int`    | **false** | [x](https://x.com)                                                                  |
| `1401` | `timezone`                                                            | `string` | **false** | [x](https://x.com)                                                                  |
| `1402` | `[timezone,x,x,new Date("1/1/1970").getTimezoneOffset(),x,n.lang]`    | `array`  | **false** | [x](https://x.com)                                                                  |
| `1403` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `3504` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `3501` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `3503` | current unix timestamp                                                | `int`    | **false** | [x](https://x.com)                                                                  |
| `3502` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `3505` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `401`  |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `402`  | length of windows properties                                          | `int`    | **false** | [x](https://x.com)                                                                  |
| `407`  |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `412`  |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `2402` | `[webgl_vendor, webgl_renderer]`                                      | `array`  | **false** | [x](https://x.com)                                                                  |
| `2420` | `[encrypt_webgl_vendor, encrypt_webgl_renderer]`                      | `array`  | **false** | [x](https://x.com)                                                                  |
| `2403` | `[webgl2_vendor, webgl2_renderer]`                                    | `array`  | **false** | [x](https://x.com)                                                                  |
| `2401` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `2408` | `!!navigator.webdriver`                                               | `bool`   | **false** | [x](https://x.com)                                                                  |
| `2407` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `2409` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `2410` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `2411` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `2412` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `2413` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `2414` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `2415` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `2416` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `2417` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `3800` | CSP                                                                   | `error`  | **false** | [x](https://x.com)                                                                  |
| `1302` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `901`  |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `905`  |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `3210` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `3211` |                                                                       |          | **false** | [x](https://x.com)                                                                  |
| `702`  | `[os.name, os.version, null, os.bits, os.arch, navigator.version]`    | `array`  | **false** | [x](https://x.com)                                                                  |
| `2001` |                                                                       |          | **true**  | [x](https://x.com)                                                                  |
| `2002` | Notifications permissions                                             | `array`  | **false** | [x](https://x.com)                                                                  |
| `0`    |                                                                       |          | **false** | [x](https://x.com)                                                                  |
