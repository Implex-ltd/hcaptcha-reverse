import httpx, json

headers = {
    "authority": "api.hcaptcha.com",
    "accept": "application/json",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    # 'content-length': '0',
    "content-type": "text/plain",
    # 'cookie': 'hmt_id=5a4e6207-3c9d-4209-a025-7b72c0ea7a15; __cflb=04dTobrcPfCH2Cv1uxYioAFTikqddqviXUhhT3P6j7',
    "origin": "https://newassets.hcaptcha.com",
    "referer": "https://newassets.hcaptcha.com/",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
}

params = {
    "v": "540c361",
    "host": "accounts.hcaptcha.com",
    "sitekey": "a5f74b19-9e45-40e0-b45d-47ff91b7a6c2",
    "sc": "1",
    "swa": "1",
    "spst": "1",
}

checksiteconfig = httpx.post(
    "https://api.hcaptcha.com/checksiteconfig", params=params, headers=headers
)
print(checksiteconfig.json())

r = httpx.post(
    "http://127.0.0.1:8080/n",
    json={
        "jwt": checksiteconfig.json()["c"]['req'],
        "fp": "eyJwcm9vZl9zcGVjIjp7ImRpZmZpY3VsdHkiOjIsImZpbmdlcnByaW50X3R5cGUiOjAsIl90eXBlIjoidyIsImRhdGEiOiJiUlJaNHlBUWk4NG1Rb3N1bmVWa3JFTGVPVzNVblkzZXJHbHUzTWlRRUpVOG1VNWtuUkNJWk4xYkhUOFhVZndPcWtGaXR3VW5lbFhzZ1BPN29WRXFXdUlDdDVDUnl2dkdKenhQRldJNVJKNVhvNXpPdXBxclM3WlZTdGZ5SkN0Zm5IRGQxVG52VUdvNkNucWd6TllKTU1yZWNvZHVmem9RNHd2MzA1a2Q0THBSU1RHcWNFS0dkdTBNM0E9PVo4cnV3SGY0ZWZNVnQ0dlAiLCJfbG9jYXRpb24iOiJodHRwczovL25ld2Fzc2V0cy5oY2FwdGNoYS5jb20vYy83OGVlNmZjIiwidGltZW91dF92YWx1ZSI6MTAwMH0sInJhbmQiOlswLjMzOTEyOTAwMDM0NDUxMDY2LDAuMjE1MTQ1OTI4OTkyNzYxMzZdLCJjb21wb25lbnRzIjp7InZlcnNpb24iOiIxLjQwLjcvNzhlZTZmYyIsIm5hdmlnYXRvciI6eyJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwibGFuZ3VhZ2UiOiJ2aS1WTiIsImxhbmd1YWdlcyI6WyJ2aS1WTiIsInZpIiwiZnItRlIiLCJmciIsImVuLVVTIiwiZW4iXSwicGxhdGZvcm0iOiJXaW4zMiIsIm1heF90b3VjaF9wb2ludHMiOjAsIndlYmRyaXZlciI6ZmFsc2UsIm5vdGlmaWNhdGlvbl9xdWVyeV9wZXJtaXNzaW9uIjpudWxsLCJwbHVnaW5zX3VuZGVmaW5lZCI6dHJ1ZX0sInNjcmVlbiI6eyJjb2xvcl9kZXB0aCI6MjQsInBpeGVsX2RlcHRoIjoyNCwid2lkdGgiOjE5MjAsImhlaWdodCI6MTA4MCwiYXZhaWxfd2lkdGgiOjE5MjAsImF2YWlsX2hlaWdodCI6MTA0MH0sImRldmljZV9waXhlbF9yYXRpbyI6MSwiaGFzX3Nlc3Npb25fc3RvcmFnZSI6dHJ1ZSwiaGFzX2xvY2FsX3N0b3JhZ2UiOnRydWUsImhhc19pbmRleGVkX2RiIjp0cnVlLCJ3ZWJfZ2xfaGFzaCI6Ii0xIiwiY2FudmFzX2hhc2giOiI3OTU0NjE4ODgyMzkzMDUwNjA1IiwiaGFzX3RvdWNoIjpmYWxzZSwibm90aWZpY2F0aW9uX2FwaV9wZXJtaXNzaW9uIjoiRGVuaWVkIiwiY2hyb21lIjp0cnVlLCJ0b19zdHJpbmdfbGVuZ3RoIjozMywiZXJyX2ZpcmVmb3giOm51bGwsInJfYm90X3Njb3JlIjowLCJyX2JvdF9zY29yZV9zdXNwaWNpb3VzX2tleXMiOltdLCJyX2JvdF9zY29yZXZlbnRzIjowLCJhdWRpb19oYXNoIjoiLTEiLCJleHRlbnNpb25zIjpbZmFsc2VdLCJwYXJlbnRfd2luX2hhc2giOiIyNTU2MzM5NjM2MDA3MTQ0MzA4Iiwid2VicnRjX2hhc2giOiItMSIsInBlcmZvcm1hbmNlX2hhc2giOiIyMDQ3NzU4NDM1ODQ3MTIyMjA5IiwidW5pcXVlX2tleXMiOiIwLEludGxQb2x5ZmlsbCxoY2FwdGNoYSxfX1NFQ1JFVF9FTU9USU9OX18sRGlzY29yZFNlbnRyeSxncmVjYXB0Y2hhLHBsYXRmb3JtLDEsX19zZW50cnlfaW5zdHJ1bWVudGF0aW9uX2hhbmRsZXJzX18sc2V0SW1tZWRpYXRlLHdlYnBhY2tDaHVua2Rpc2NvcmRfYXBwLF8sR0xPQkFMX0VOVixjbGVhckltbWVkaWF0ZSxfX2xvY2FsZURhdGFfXyxfX09WRVJMQVlfXyxfX1NFTlRSWV9fLHJlZ2VuZXJhdG9yUnVudGltZSxoY2FwdGNoYU9uTG9hZCxfX3RpbWluZ0Z1bmN0aW9uLERpc2NvcmRFcnJvcnMsX19ESVNDT1JEX1dJTkRPV19JRCxfX0JJTExJTkdfU1RBTkRBTE9ORV9fIiwiaW52X3VuaXF1ZV9rZXlzIjoiX193ZGF0YSxpbWFnZV9sYWJlbF9iaW5hcnksX3NoYXJlZExpYnMsdGV4dF9mcmVlX2VudHJ5LHNlc3Npb25TdG9yYWdlLGhzdyxsb2NhbFN0b3JhZ2UiLCJmZWF0dXJlcyI6eyJwZXJmb3JtYW5jZV9lbnRyaWVzIjp0cnVlLCJ3ZWJfYXVkaW8iOnRydWUsIndlYl9ydGMiOnRydWUsImNhbnZhc18yZCI6dHJ1ZSwiZmV0Y2giOnRydWV9fSwiZmluZ2VycHJpbnRfZXZlbnRzIjpbWzAsIjM2LjE4MzMwODY4NzA3MDYwIl0sWzMsIjMzNTU0LjM1Il0sWzEwNywiWzE5MjAsMTA4MCwxOTIwLDEwNDAsMjQsMjQsZmFsc2UsMCwxLDE3MDcsMTY2Mix0cnVlLHRydWUsdHJ1ZSxmYWxzZV0iXSxbMjAxLCIxNDE1NTY0NTc3NjI4MTg2NDAwMCJdLFsyMTEsIlstNi4xNzI4NDAxMTg0MDgyMDMsLTIwLjcxMDY3ODEwMDU4NTkzOCwxMjAuNzEwNjc4MTAwNTg1OTQsLTIwLjcxMDY3ODEwMDU4NTkzOCwxNDEuNDIxMzU2MjAxMTcxODgsMTIwLjcxMDY3ODEwMDU4NTk0LC0yMC43MTA2NzgxMDA1ODU5MzgsMTQxLjQyMTM1NjIwMTE3MTg4LC0yMC43MTA2NzgxMDA1ODU5MzgsLTIwLjcxMDY3ODEwMDU4NTkzOCwwLDAsMTg4NywxMjQ2LjU2MjUsZmFsc2UsWzAsMiw1LDYsOCw5LDEyLDE1LDE4LDIxLDIzLDI4LDMzLDM0LDM1LDM3LDM5LDQyLDQ3LDY2LDY3LDY5LDcxLDc1LDc2LDc5LDgyXV0iXSxbMzAxLCI4MzgzNDczMDQzMzYwMDc4MDAwIl0sWzMwNCwiNjIzIl0sWzQwMSwiMTA4OTkxNTQzMTYzMjM3MDAwMDAiXSxbNDAyLCIxMTE5Il0sWzQwNywiW1tcImxvYWRUaW1lc1wiLFwiY3NpXCIsXCJhcHBcIl0sMzUsMzQsbnVsbCxmYWxzZSxmYWxzZSx0cnVlLDM3LHRydWUsdHJ1ZSx0cnVlLHRydWUsdHJ1ZSxbXCJSYXZlblwiLFwiX3NoYXJlZExpYnNcIixcImhzd1wiLFwiX193ZGF0YVwiLFwiaW1hZ2VfbGFiZWxfYmluYXJ5XCIsXCJ0ZXh0X2ZyZWVfZW50cnlcIl0sW1tcImdldEVsZW1lbnRzQnlDbGFzc05hbWVcIixbXV0sW1wiZ2V0RWxlbWVudEJ5SWRcIixbXV0sW1wicXVlcnlTZWxlY3RvclwiLFtdXSxbXCJxdWVyeVNlbGVjdG9yQWxsXCIsW11dXSxbXSx0cnVlXSJdLFs0MTIsIjE1NTg0NjYwNDMzMDkzODYxMDAwIl0sWzYwNCwiW1wiNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTguMC4wLjAgU2FmYXJpLzUzNy4zNlwiLFwiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOC4wLjAuMCBTYWZhcmkvNTM3LjM2XCIsNCwyLFwidmktVk5cIixbXCJ2aS1WTlwiLFwidmlcIixcImZyLUZSXCIsXCJmclwiLFwiZW4tVVNcIixcImVuXCJdLFwiV2luMzJcIixudWxsLFtcIkdvb2dsZSBDaHJvbWUgMTE4XCIsXCJOb3Q9QT9CcmFuZCA4XCIsNjddLGZhbHNlLFwiV2luZG93c1wiLDIsNSx0cnVlLGZhbHNlLDEwMCxmYWxzZSxmYWxzZSx0cnVlLFwiW29iamVjdCBLZXlib2FyZF1cIixmYWxzZSxmYWxzZV0iXSxbNzAyLCJbXCJXaW5kb3dzXCIsXCIxMC4wLjBcIixudWxsLFwiNjRcIixcIng4NlwiLFwiMTE4LjAuNTk5My43MFwiXSJdLFs4MDMsIlsxLDQsNSw3LDksMTIsMjAsMjEsMjMsMjUsMjksMzFdIl0sWzkwMSwiMTM1ODY5MDU1ODc2Njc4NTQwIl0sWzkwNSwiW1t0cnVlLFwiZW4tVVNcIix0cnVlLFwiTWljcm9zb2Z0IERhdmlkIC0gRW5nbGlzaCAoVW5pdGVkIFN0YXRlcylcIixcIk1pY3Jvc29mdCBEYXZpZCAtIEVuZ2xpc2ggKFVuaXRlZCBTdGF0ZXMpXCJdLFtmYWxzZSxcImVuLVVTXCIsdHJ1ZSxcIk1pY3Jvc29mdCBNYXJrIC0gRW5nbGlzaCAoVW5pdGVkIFN0YXRlcylcIixcIk1pY3Jvc29mdCBNYXJrIC0gRW5nbGlzaCAoVW5pdGVkIFN0YXRlcylcIl0sW2ZhbHNlLFwiZW4tVVNcIix0cnVlLFwiTWljcm9zb2Z0IFppcmEgLSBFbmdsaXNoIChVbml0ZWQgU3RhdGVzKVwiLFwiTWljcm9zb2Z0IFppcmEgLSBFbmdsaXNoIChVbml0ZWQgU3RhdGVzKVwiXV0iXSxbMTEwMSwiMTUwMDQ0NDg5OTM5ODI4NDMwMDAiXSxbMTEwMywiNDkzMjM4MzIxMTQ5NzM2MDAwMCJdLFsxMTA1LCIyMzM3NjY2NzUzMzIyNjk3MDAwIl0sWzExMDcsIlsyNzQuNjA5Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4Miw0NjUuMDQ2ODc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwxNTQuNzk2ODc1LDI4MiwyMzkuNTYyNSwyODIsMjc0LjYwOTM3NSwyODIsNDE1LjQzNzUsMjgyLDE1Mi40MDYyNSwyNDgsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsNTM1LjI2NTYyNSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjYwLjU0Njg3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjYwLjY1NjI1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNDYuNTkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI1My42MjUsMjgyLDI3NC42MDkzNzUsMjgyLDI0Ni41OTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjE4LjQ2ODc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNzQuNzE4NzUsMjgyLDM4Ny40MDYyNSwyODIsMzE3LjE4NzUsMjgyLDI3NC42MDkzNzUsMjgyLDE4Ny42MDkzNzUsMjQ4LDE4Ny42MDkzNzUsMjQ4LDE1NC40MDYyNSwyNDgsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjY3LjY4NzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDIwNC41LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNjAuNTQ2ODc1LDI4MiwyMDQuNSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMjc0LjYwOTM3NSwyODIsMTkwLjQzNzUsMjgyLDIzMi41MzEyNSwyODIsMjc0LjYwOTM3NSwyODIsMjY3LjU3ODEyNSwyODIsMjc0LjYwOTM3NSwyODIsMjczLjM0Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwyNzQuNjA5Mzc1LDI4MiwxNzIuMjY1NjI1LDI4MiwxMDYuMTU2MjUsMjgyLDIxOC40Njg3NSwyODIsMjc0LjYwOTM3NSwyODIsMTgzLjQwNjI1LDI4MiwxODMuNDA2MjUsMjgyLDI3NC42MDkzNzUsMjgyLDI2OC4xNzE4NzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyLDI3NC42MDkzNzUsMjgyXSJdLFsxMzAyLCJbMSwyLDMsNF0iXSxbMTQwMSwiXCJBc2lhL0Jhbmdrb2tcIiJdLFsxNDAyLCJbXCJBc2lhL0Jhbmdrb2tcIiwtNDIwLC00MjAsLTMyMDM3NTA1MjQwMDAsXCJHaeG7nSDEkMO0bmcgRMawxqFuZ1wiLFwidmlcIl0iXSxbMTQwMywiW1wiOTJBQk5YQWg5SVFoNTJaUlwiLFwiMWFcIixcImRcIixcIlJMVEVUQ1lPSVBBUkNcIl0iXSxbMTkwMSwiMTUzMDczNDU3OTAxMjUwMDMwMDAiXSxbMTkwMiwiNTciXSxbMTkwNCwiWzAsMTE0MTIsMTE0MTJdIl0sWzI0MDEsIjE4Mzc5MzAyNDQyNDE2Njk1MDAwIl0sWzI0MDIsIltcIkdvb2dsZSBJbmMuIChJbnRlbClcIixcIkFOR0xFIChJbnRlbCwgSW50ZWwoUikgSEQgR3JhcGhpY3MgKDB4MDAwMDA0MDIpIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpXCJdIl0sWzI0MDcsIjYxNzQ1NTkxNjczOTYwNzYwMDAiXSxbMjQwOCwidHJ1ZSJdLFsyNDA5LCJbMjE0NzQ4MzY0NywyMTQ3NDgzNjQ3LDQyOTQ5NjcyOTRdIl0sWzI0MTAsIlsxNiwxMDI0LDQwOTYsNywxMiwxMjAsWzIzLDEyNywxMjddXSJdLFsyNDExLCJbMzI3NjcsMzI3NjcsMTYzODQsOCw4LDhdIl0sWzI0MTIsIlsxLDEwMjQsMSwxLDRdIl0sWzI0MTMsIlsyMTQ3NDgzNjQ3LDIxNDc0ODM2NDcsMjE0NzQ4MzY0NywyMTQ3NDgzNjQ3XSJdLFsyNDE0LCJbMTYzODQsMzIsMTYzODQsMjA0OCwyLDIwNDhdIl0sWzI0MTUsIls0LDEyMCw0XSJdLFsyNDE2LCJbMjQsMjQsNjU1MzYsMjEyOTkyLDIwMDcwNF0iXSxbMjQxNywiWzE2LDQwOTYsMzAsMTYsMTYzODQsMTIwLDEyLDEyMCxbMjMsMTI3LDEyN11dIl0sWzI0MjAsIltbXCJsWFdLR2trYko1Y2lIOTJiblhXej09QUtqNWdkXCIsXCJlXCIsXCI4XCIsXCJJUVhaSkNKVkdKVFRSXCJdLFtcIkNjWjl2TkZiRGxHWTNjRnZaWHdBQ1JwSlh6alIzbUVmVG1HR0NtNGJEbXdBRG0wQWptcEF5UnlmZ2NPTDJZWmJDc0Vic3N1Ulh6U2hpVXBBQ2tKNWdkTHhnbEdFS1RIeFVSPVEwbUVmVG1wQVwiLFwiZFwiLFwiYVwiLFwiTU9aWlNTR0tHQkZWTFwiXV0iXSxbMjgwMSwiNDYzMTIyOTA4ODA3MjU4NDAwMCJdLFsyODA1LCJbWzI3NzExNDMxNDQ1MywyNzcxMTQzMTQ0NjAsMjc3MTE0MzE0NDUxLDM1NzExNDMxNDQ1NiwyNzcxMTQzMTQ0NTIsNTU0MjI4NjI4ODk4LDU3MTE0MzE0NDQzLDcxNzExNDMxNDM3MTM5MSw1NTQyMjg2Mjg4OTcsMjc3MTE0MzE0NDU2LDExMDg0NTcyNTc4NjIsMjc3MTE0MzE0NDUwLDU1NDIyODYyODkxOSwyNzcxMTQzMTQ0NjAsMjc3MTE0MzE0NDUxXSxmYWxzZV0iXSxbMzIxMCwiWzQ2NDg5NDUzMzYyLDQ2NDg5NDUzMzYyLG51bGwsbnVsbCwyMTIyNTc5OTY4LHRydWUsdHJ1ZSx0cnVlLG51bGxdIl0sWzMyMTEsIltcIjJhRG1XZ3RPeFF6bXlVRE5cIixcIjE5XCIsXCI4XCIsXCJNTEhITUZUQUtLTFdFXCJdIl0sWzM0MDEsIjI1MzA5MTc0MDQ3NTUyNDUxNDIiXSxbMzQwMywiW1tbXCJodHRwczovL25ld2Fzc2V0cy5oY2FwdGNoYS5jb20vY2FwdGNoYS92MS9kMjE3YTQ1L2hjYXB0Y2hhLmpzXCIsMCw1XV0sW1tcIipcIiw4NCw5XV1dIl0sWzM1MDEsIltbXCJpbWc6aW1ncy5oY2FwdGNoYS5jb21cIiwwLDI1LjQxODE4MjA3MDU1MjZdLFtcIm5hdmlnYXRpb246bmV3YXNzZXRzLmhjYXB0Y2hhLmNvbVwiLDI5LjY1MTUyNTUwODAwNTYsMTEuODQ4ODkzMzk5NTQ3NiwxMS45NTg4NjA0MjE1OTYxXSxbXCJzY3JpcHQ6bmV3YXNzZXRzLmhjYXB0Y2hhLmNvbVwiLDQ4LjU2NjEwOTk1NDk2OTcsNDQuMjY4NDQ1Nzg2MTg1N10sW1wieG1saHR0cHJlcXVlc3Q6aGNhcHRjaGEuY29tXCIsMCwxNzQuMzA0MTg3NTQyODA2NV1dIl0sWzM1MDIsIjIuMTU5NDUyMzMyNDU3MDAiXSxbMzUwMywiMC43MjI3ODMzMDgzNDE3MCJdLFszNTA0LCIxNjk4MDc0MzU3ODczLjQiXSxbMzgwMSwiNDUxNDkiXSxbMzgwMiwiMzE3LjU0MTcwNDk2NTQxNDgiXV0sIm1lc3NhZ2VzIjpudWxsLCJzdGFja19kYXRhIjpbXSwiZmluZ2VycHJpbnRfc3VzcGljaW91c19ldmVudHMiOltdLCJzdGFtcCI6IiIsImhyZWYiOiJodHRwczovL2Rpc2NvcmQuY29tL2ludml0ZS82dUh5ZnVBNyIsImVycnMiOnsibGlzdCI6W119LCJwZXJmIjpbWzEsMThdLFsyLDQyXV19",
    },
)

print(r.text)
n = r.text

cookies = {
    "hmt_id": "5a4e6207-3c9d-4209-a025-7b72c0ea7a15",
}

headers = {
    "authority": "api.hcaptcha.com",
    "accept": "application/json, application/octet-stream",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded",
    # 'cookie': 'hmt_id=5a4e6207-3c9d-4209-a025-7b72c0ea7a15',
    "origin": "https://newassets.hcaptcha.com",
    "referer": "https://newassets.hcaptcha.com/",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
}

task_payload = {
    "v": "540c361",
    "sitekey": "a5f74b19-9e45-40e0-b45d-47ff91b7a6c2",
    "host": "accounts.hcaptcha.com",
    "hl": "fr",
    "motionData": '{"st":1707359970521,"mm":[[302,19,1707360219794],[262,24,1707360219814],[229,30,1707360219832],[204,35,1707360219848],[185,39,1707360219864],[167,41,1707360219881],[154,42,1707360219898],[145,43,1707360219914],[136,44,1707360219931],[129,44,1707360219949],[122,45,1707360219965],[116,45,1707360219981]],"mm-mp":1.7118644067796607,"md":[[113,45,1707360220034]],"md-mp":0,"mu":[[113,45,1707360220115]],"mu-mp":0,"v":1,"topLevel":{"inv":false,"st":1707359969940,"sc":{"availWidth":3440,"availHeight":1392,"width":3440,"height":1440,"colorDepth":24,"pixelDepth":24,"availLeft":0,"availTop":0,"onchange":null,"isExtended":true},"nv":{"vendorSub":"","productSub":"20030107","vendor":"Google Inc.","maxTouchPoints":0,"scheduling":{},"userActivation":{},"doNotTrack":null,"geolocation":{},"connection":{},"pdfViewerEnabled":true,"webkitTemporaryStorage":{},"hardwareConcurrency":16,"cookieEnabled":true,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","platform":"Win32","product":"Gecko","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","language":"fr-FR","languages":["fr-FR","fr","en-US","en"],"onLine":true,"webdriver":false,"deprecatedRunAdAuctionEnforcesKAnonymity":false,"bluetooth":{},"clipboard":{},"credentials":{},"keyboard":{},"managed":{},"mediaDevices":{},"storage":{},"serviceWorker":{},"virtualKeyboard":{},"wakeLock":{},"deviceMemory":8,"login":{},"ink":{},"mediaCapabilities":{},"hid":{},"locks":{},"gpu":{},"mediaSession":{},"permissions":{},"presentation":{},"usb":{},"xr":{},"serial":{},"windowControlsOverlay":{},"userAgentData":{"brands":[{"brand":"Not A(Brand","version":"99"},{"brand":"Google Chrome","version":"121"},{"brand":"Chromium","version":"121"}],"mobile":false,"platform":"Windows"},"plugins":["internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer","internal-pdf-viewer"]},"dr":"https://www.google.com/","exec":false,"wn":[],"wn-mp":0,"xy":[],"xy-mp":0,"mm":[[433,275,1707360219751],[393,279,1707360219767],[354,282,1707360219783]],"mm-mp":18.88070175438596},"session":[],"widgetList":["0rsv4tptttxc"],"widgetId":"0rsv4tptttxc","href":"https://accounts.hcaptcha.com/demo","prev":{"escaped":false,"passed":false,"expiredChallenge":false,"expiredResponse":false}}',
    "pdc": '{"s":1707360220120,"n":0,"p":0,"gcs":70}',
    "n": n,
    "c": json.dumps(checksiteconfig.json()["c"]),
    "pst": "false",
}

response = httpx.post(
    "https://api.hcaptcha.com/getcaptcha/a5f74b19-9e45-40e0-b45d-47ff91b7a6c2",
    cookies=cookies,
    headers=headers,
    data=task_payload,
)

print(response.json())
