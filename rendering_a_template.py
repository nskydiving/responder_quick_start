import responder

api = responder.API()

@api.route("/hello/{who}/html")
def hello_html(req, resp, *, who):
    resp.content = api.template('hello.html', who=who)

if __name__ == '__main__':
    api.run()
