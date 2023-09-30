 # HCaptcha reverse engineer

## Fingerprint events

> `fingerprint_events` is parsed output of fingerprinting script, somes data are hashed.
> Final output is used into n data.

| id     | type                                                               | type     | hashed    | fp_raw                |
| ------ | ------------------------------------------------------------------ | -------- | --------- | --------------------- |
| `3`    |                                                                    |          | **false** | [link](https://x.com) |
| `1902` |                                                                    |          | **false** | [link](https://x.com) |
| `1901` |                                                                    |          | **true**  | [link](https://x.com) |
| `1101` |                                                                    |          | **true**  | [link](https://x.com) |
| `1103` |                                                                    |          | **true**  | [link](https://x.com) |
| `1105` |                                                                    |          | **true**  | [link](https://x.com) |
| `1107` |                                                                    |          | **false** | [link](https://x.com) |
| `201`  |                                                                    |          | **false** | [link](https://x.com) |
| `211`  |                                                                    |          | **true**  | [link](https://x.com) |
| `3401` |                                                                    |          | **true**  | [link](https://x.com) |
| `3403` |                                                                    |          | **false** | [link](https://x.com) |
| `803`  |                                                                    |          | **false** | [link](https://x.com) |
| `604`  | [n.appv,n.ua,n.mem,n.hwconc,n.lang,n.langs,n.platform,x,versin...] |          | **false** | [link](https://x.com) |
| `2801` |                                                                    |          | **true**  | [link](https://x.com) |
| `2805` |                                                                    |          | **false** | [link](https://x.com) |
| `107`  | `[w,h,aw,ah,pd,pd,x,x,x,x,x,x,x,x,x]`                              | `array`  | **false** | [link](https://x.com) |
| `302`  |                                                                    |          | **true**  | [link](https://x.com) |
| `303`  | `fonts`                                                            | `array`  | **false** | [link](https://x.com) |
| `301`  |                                                                    |          | **true**  | [link](https://x.com) |
| `304`  | length of CSS properties                                           | `int`    | **false** | [link](https://x.com) |
| `1401` | `timezone`                                                         | `string` | **false** | [link](https://x.com) |
| `1402` | `[timezone,x,x,new Date("1/1/1970").getTimezoneOffset(),x,n.lang]` | `array`  | **false** | [link](https://x.com) |
| `1403` |                                                                    |          | **false** | [link](https://x.com) |
| `3504` |                                                                    |          | **false** | [link](https://x.com) |
| `3501` |                                                                    |          | **false** | [link](https://x.com) |
| `3503` | current unix timestamp                                             | `int`    | **false** | [link](https://x.com) |
| `3502` |                                                                    |          | **false** | [link](https://x.com) |
| `3505` |                                                                    |          | **false** | [link](https://x.com) |
| `401`  |                                                                    |          | **true**  | [link](https://x.com) |
| `402`  | length of windows properties                                       | `int`    | **false** | [link](https://x.com) |
| `407`  |                                                                    |          | **false** | [link](https://x.com) |
| `412`  |                                                                    |          | **true**  | [link](https://x.com) |
| `2402` | `[webgl_vendor, webgl_renderer]`                                   | `array`  | **false** | [link](https://x.com) |
| `2420` | `[encrypt_webgl_vendor, encrypt_webgl_renderer]`                   | `array`  | **false** | [link](https://x.com) |
| `2403` | `[webgl2_vendor, webgl2_renderer]`                                 | `array`  | **false** | [link](https://x.com) |
| `2401` |                                                                    |          | **true**  | [link](https://x.com) |
| `2408` | `!!navigator.webdriver`                                            | `bool`   | **false** | [link](https://x.com) |
| `2407` |                                                                    |          | **true**  | [link](https://x.com) |
| `2409` |                                                                    |          | **false** | [link](https://x.com) |
| `2410` |                                                                    |          | **false** | [link](https://x.com) |
| `2411` |                                                                    |          | **false** | [link](https://x.com) |
| `2412` |                                                                    |          | **false** | [link](https://x.com) |
| `2413` |                                                                    |          | **false** | [link](https://x.com) |
| `2414` |                                                                    |          | **false** | [link](https://x.com) |
| `2415` |                                                                    |          | **false** | [link](https://x.com) |
| `2416` |                                                                    |          | **false** | [link](https://x.com) |
| `2417` |                                                                    |          | **false** | [link](https://x.com) |
| `3800` | CSP                                                                | `error`  | **false** | [link](https://x.com) |
| `1302` |                                                                    |          | **false** | [link](https://x.com) |
| `901`  |                                                                    |          | **true**  | [link](https://x.com) |
| `905`  |                                                                    |          | **false** | [link](https://x.com) |
| `3210` |                                                                    |          | **false** | [link](https://x.com) |
| `3211` |                                                                    |          | **false** | [link](https://x.com) |
| `702`  | `[os.name, os.version, null, os.bits, os.arch, navigator.version]` | `array`  | **false** | [link](https://x.com) |
| `2001` |                                                                    |          | **true**  | [link](https://x.com) |
| `2002` | Notifications permissions                                          | `array`  | **false** | [link](https://x.com) |
| `0`    |                                                                    |          | **false** | [link](https://x.com) |
