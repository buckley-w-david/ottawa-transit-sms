# /usr/bin/env python
from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

sms_blueprint = Blueprint("sms_blueprint", __name__)


@sms_blueprint.route("/sms", methods=["GET", "POST"])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)
