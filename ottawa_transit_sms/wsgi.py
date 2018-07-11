import os
from ottawa_transit_sms import create_app
from ottawa_transit_sms import Environment

port = int(os.getenv("OTSMS_PORT", 5000))
environment = os.getenv("OTSMS_ENV", "production")
env = Environment.from_string(environment)
app = create_app(env)

if __name__ == "__main__":
    app.run(port=port)
