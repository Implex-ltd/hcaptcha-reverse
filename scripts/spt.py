import jwt
from datetime import datetime

# {'f': 0, 's': 2, 't': 'w', 'd': '4Eux6k5EX+wfXrqArQWqZiRw0VQni2M1+Gdd+djXH1q+34iAvzGSsghDID+5oNm+5Meq3KG6QsO5j7TwLA8aOfa1tfEAEpBvpLbQ514gO0rFHSlVyrRD8Et4r9d5fXs/WVP2RdiOduke/c3OgsoRIoa1KyeXd+/cfyiQcpL/oe6QqrXcyAv3JVPr+Q==VjAO3C2wNagbGcb1', 'l': 'https://newassets.hcaptcha.com/c/bf600bd', 'i': 'sha256-NlCzVqJUjbqZYLhatI+6TU+CW0NopTmXzlgf/mh295g=', 'e': 1695952341, 'n': 'hsw', 'c': 1000}
# "{"f":0,"t":1000.0,"c":"1:2:2023-09-29:4Eux6k5EX+wfXrqArQWqZiRw0VQni2M1+Gdd+djXH1q+34iAvzGSsghDID+5oNm+5Meq3KG6QsO5j7TwLA8aOfa1tfEAEpBvpLbQ514gO0rFHSlVyrRD8Et4r9d5fXs/WVP2RdiOduke/c3OgsoRIoa1KyeXd+/cfyiQcpL/oe6QqrXcyAv3JVPr+Q==VjAO3C2wNagbGcb1::1ndCnZSy","d":2}"

c = {
    "f": 0,
    "t": 1000.0,
    "c": "1:2:2023-09-29:Uxya27uBQtzrwuI3MMyjn8Pk9Ct88UOfkxvu6PxaF400IXQTDkvMiigif819Y4ONOlEFapvsz24Cox4mJArhQwyLdOB+/H4vWgmZAtGXtVrBt1uTJ8UG/XeH5CdFYlxBm8VFb7AlHol09TIK9BwQm8NyUkX1W6xt6IfGQIypokLN0OVjLldSfO0lhQ==x4efgtIWrLISbFsc::6x2mKeXA",
    "d": 2,
}


def stamp():
    return "jCHhnRMq"


def generate_stamp(jwt_token: str):
    data = jwt.decode(jwt_token, options={"verify_signature": False})
    # 1:2:2023-09-29:jwt_data::jCHhnRMq:1

    return ":".join(
        [
            "1",
            str(data["s"]),
            datetime.fromtimestamp(data["e"]).strftime("%Y-%m-%d"),
            "::".join([data["d"], stamp()]),
            "1",
        ]
    )


for _ in range(1):
    r = generate_stamp(
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiI0RXV4Nms1RVgrd2ZYcnFBclFXcVppUncwVlFuaTJNMStHZGQrZGpYSDFxKzM0aUF2ekdTc2doRElEKzVvTm0rNU1lcTNLRzZRc081ajdUd0xBOGFPZmExdGZFQUVwQnZwTGJRNTE0Z08wckZIU2xWeXJSRDhFdDRyOWQ1ZlhzL1dWUDJSZGlPZHVrZS9jM09nc29SSW9hMUt5ZVhkKy9jZnlpUWNwTC9vZTZRcXJYY3lBdjNKVlByK1E9PVZqQU8zQzJ3TmFnYkdjYjEiLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvYmY2MDBiZCIsImkiOiJzaGEyNTYtTmxDelZxSlVqYnFaWUxoYXRJKzZUVStDVzBOb3BUbVh6bGdmL21oMjk1Zz0iLCJlIjoxNjk1OTUyMzQxLCJuIjoiaHN3IiwiYyI6MTAwMH0.nZM4XuOq8p-JcIihWkQVhUdxoiusvQc_VZAvihqrCwlx367oCARbe8hWeBg-CEYYN2YgrTvzow-YyfdFSzBbexN3ZW9L0MHqlJg5djJbl71DrPAMav1IACaTljrNJOUNjUCCej336ANPOWykE2wgjW7F8ha5t-bfKt5CIXNYie0"
    )
    print(r)
