import responder

api = responder.API()

@api.route("/hello/{who}")
def hello_to(req, resp, *, who):
    resp.text = f"hello, {who}!"

if __name__ == '__main__':
    api.run()
