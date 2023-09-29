import jwt # 2 less imports (pip install pyjwt)
from datetime import datetime

def generate_hsl(jwt_token: str): # around 50 less lines of code with unnecessary hashing (I read line by line and it's all useless)
    data = jwt.decode(jwt_token, options={"verify_signature": False}) # decodes json web token to get values
    return ":".join([ #":".join to add : after every list value
     "1", # always 1
      str(data['s']), # s value in decoded JWT
  str(datetime.fromtimestamp(int(data['e'])).isoformat().replace("-", "").replace("T", "").replace(":", "")), # h0nde never used the unix timestamp provided in the decoded JWT token LOL
      data['d'], # d value in decoded JWT token
      "", # blank so .join can add two :: 
      "1" # this is the value h0nde made all that unnecessary code for 
    ])

print(generate_hsl('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiI0RXV4Nms1RVgrd2ZYcnFBclFXcVppUncwVlFuaTJNMStHZGQrZGpYSDFxKzM0aUF2ekdTc2doRElEKzVvTm0rNU1lcTNLRzZRc081ajdUd0xBOGFPZmExdGZFQUVwQnZwTGJRNTE0Z08wckZIU2xWeXJSRDhFdDRyOWQ1ZlhzL1dWUDJSZGlPZHVrZS9jM09nc29SSW9hMUt5ZVhkKy9jZnlpUWNwTC9vZTZRcXJYY3lBdjNKVlByK1E9PVZqQU8zQzJ3TmFnYkdjYjEiLCJsIjoiaHR0cHM6Ly9uZXdhc3NldHMuaGNhcHRjaGEuY29tL2MvYmY2MDBiZCIsImkiOiJzaGEyNTYtTmxDelZxSlVqYnFaWUxoYXRJKzZUVStDVzBOb3BUbVh6bGdmL21oMjk1Zz0iLCJlIjoxNjk1OTUyMzQxLCJuIjoiaHN3IiwiYyI6MTAwMH0.nZM4XuOq8p-JcIihWkQVhUdxoiusvQc_VZAvihqrCwlx367oCARbe8hWeBg-CEYYN2YgrTvzow-YyfdFSzBbexN3ZW9L0MHqlJg5djJbl71DrPAMav1IACaTljrNJOUNjUCCej336ANPOWykE2wgjW7F8ha5t-bfKt5CIXNYie0'))