import responder
import time

api = responder.API()

# curl コマンドで json データを送信する
# curl http://127.0.0.1:5042/incoming -X POST -H "Content-Type: application/json" -d '{"key": "value"}'
@api.route("/incoming")
async def receive_incoming(req, resp):

    @api.background.task
    def process_data(data):
        """Just sleeps for three seconds, as a demo."""
        time.sleep(3)


    # Parse the incoming data as form-encoded.
    # Note: 'json' and 'yaml' formats are also automatically supported.
    data = await req.media()

    # Process the data (in the background).
    process_data(data)

    # Immediately respond that upload was successful.
    resp.media = {'success': True}

if __name__ == '__main__':
    api.run()