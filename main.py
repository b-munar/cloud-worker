from flask import Flask, request
from utils.compress import compress_zip
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    try:
        envelope = request.get_json()

        pubsub_message = envelope["message"]

        print(f"Received {pubsub_message['data']!r}.")

        if int(pubsub_message['attributes']['type_task']) == 1:
            compress_zip(int(pubsub_message['attributes']['file_id']))
            
        return "", 204
    except:
        return "Page not found", 404

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0',debug=True)
