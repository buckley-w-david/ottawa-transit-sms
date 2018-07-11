from python_ottawa_transit.api import OCTransportApi
from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

from ottawa_transit_sms.flask_pot import ot_api

sms_blueprint = Blueprint("sms_blueprint", __name__)

short_codes = {
    "grss": "get_route_summary_for_stop",
    "gnts": "get_next_trips_for_stop",
    "gntsal": "get_next_trips_for_stop_all_routes",
}


def handle_request(request: str):
    api = ot_api.api
    return str(api.get_next_trips_for_stop_all_routes(stop_no=int(request)))


@sms_blueprint.route("/sms", methods=["GET", "POST"])
def transit_request():
    body = request.values.get("body")
    response = handle_request(body)

    # Add a message
    resp = MessagingResponse()
    resp.message(response)

    return str(resp)
