import os


class OttawaTransitSMSConfig:
    OTTAWA_TRANSIT_APP_ID = "APP_ID"
    OTTAWA_TRANSIT_API_KEY = "API_KEY"
    DEBUG = False
    TESTING = False


class TestingConfig(OttawaTransitSMSConfig):
    TESTING = True


class DevelopmentConfig(OttawaTransitSMSConfig):
    DEBUG = True


class ProductionConfig(OttawaTransitSMSConfig):
    OTTAWA_TRANSIT_APP_ID = os.environ.get("OTTAWA_TRANSIT_APP_ID")
    OTTAWA_TRANSIT_API_KEY = os.environ.get("OTTAWA_TRANSIT_API_KEY")
