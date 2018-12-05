import responder

api = responder.API()

@api.route("/hello/{who}/json")
def hello_to(req, resp, *, who):
    resp.media = {"hello": who}

if __name__ == '__main__':
    api.run()

