from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    webhook_url = data.get('webhookUrl')
    message = data.get('message')

    if not webhook_url or not message:
        return jsonify({"error": "Webhook URL or message missing"}), 400

    response = send_discord_message(webhook_url, message)

    if response.status_code == 200:
        return jsonify({"message": "Message sent successfully"}), 200
    else:
        return jsonify({"error": "Failed to send message"}), response.status_code

def send_discord_message(webhook_url, message):
    import requests
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        'content': message
    }
    response = requests.post(webhook_url, headers=headers, json=payload)
    return response

if __name__ == '__main__':
    app.run(debug=True)
