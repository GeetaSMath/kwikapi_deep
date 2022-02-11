import json

from kwikapi import API, MockRequest, BaseRequestHandler

class Calc(object):
   # Type information must be specified
  def user(self, username: str, password: str) -> str:
      return username + password

api = API()
api.register(Calc(), "G1") # `v1` is the version of this example

req1 = MockRequest(url="/api/G1/user?username=geeta&password=gsm")

res = json.loads(BaseRequestHandler(api).handle_request(req1).decode('utf-8'))
print(res)
