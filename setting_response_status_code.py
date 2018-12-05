import responder

api = responder.API()

@api.route("/416")
def teapot(req, resp):
    resp.status_code = api.status_codes.HTTP_416   # ...or 416

if __name__ == '__main__':
    api.run()
