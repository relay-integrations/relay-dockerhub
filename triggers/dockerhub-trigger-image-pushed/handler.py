from nebula_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

relay = Interface()
app = Quart('image-pushed')


@app.route('/', methods=['POST'])
async def handler():
    event_payload = await request.get_json()

    if event_payload is None:
        return await make_response(jsonify(message='not a valid Docker Hub event'), 400)

    pd = event_payload['push_data']
    rd = event_payload['repository']

    relay.events.emit({
        'pushedAt': pd['pushed_at'],
        'pusher': pd['pusher'],
        'tag': pd['tag'],
        'name': rd['repo_name']
    })

    return await make_response(jsonify(message='success'), 200)


if __name__ == '__main__':
    WebhookServer(app).serve_forever()
