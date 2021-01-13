from nebula_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response
import json
import logging

relay = Interface()
app = Quart('image-pushed')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    event_payload = await request.get_json()

    logging.info("Received the following webhook payload: \n%s", json.dumps(event_payload, indent=4))

    if event_payload is None:
        return await make_response(jsonify(message='not a valid Docker Hub event'), 400)

    pd = event_payload['push_data']
    rd = event_payload['repository']

    relay.events.emit({
        'pushedAt': pd['pushed_at'],
        'pusher': pd['pusher'],
        'tag': pd['tag'],
        'repoName': rd['repo_name'],
        'description': rd['description'],
        'fullDescription': rd['full_description'],
        'owner': rd['owner'],
        'isOfficial': rd['is_official'],
        'isPrivate': rd['is_private'],
        'namespace': rd['namespace'],
        'repoUrl': rd['repo_url']
    })

    return await make_response(jsonify(message='success'), 200)


if __name__ == '__main__':
    WebhookServer(app).serve_forever()
