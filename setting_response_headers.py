import responder

api = responder.API()

@api.route("/pizza")
def pizza_pizza(req, resp):
    resp.headers['X-Pizza'] = '42'

if __name__ == '__main__':
    api.run()
