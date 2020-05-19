from flask import Flask, request, jsonify, make_response
import requests

import os
import json
from urllib.parse import urljoin

port = os.getenv('PORT', '8080')
metadata_api = os.getenv('METADATA_API_URL')
metadata_api_events = urljoin(metadata_api, 'events')
debug = os.getenv('DEBUG', False)
app = Flask(__name__)


@app.route('/', methods=['POST'])
def handler():
    event_payload = request.get_json()

    if event_payload is None:
        return make_response(jsonify(message='not a valid dockerhub event'), 400)

    pd = event_payload['push_data']
    rd = event_payload['repository']

    relay_event = {'data': {
        'pushed_at': pd['pushed_at'],
        'pusher': pd['pusher'],
        'tag': pd['tag'],
        'name': rd['repo_name']
    }}

    request_payload = json.dumps(relay_event)

    # TODO we need to figure out how to behave when we can't successfully submit
    # an event to the metadata api. for now, we will just ignore the response.
    headers = {'Content-type': 'application/json'}
    requests.post(metadata_api_events, headers=headers, json=request_payload)

    return make_response(jsonify(message='success'), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=debug)
