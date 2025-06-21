from flask import request


def delivery_webhook():
    data = request.get_json()
    if data["event"] == "delivered":
        email_id = data.get("email_id")
    return "OK", 200
