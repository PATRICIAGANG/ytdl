import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", ""))

    API_HASH = os.environ.get("API_HASH", "")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://telegra.ph/file/d2372fe42ccf8c9273088.jpg")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://telegra.ph/file/d2372fe42ccf8c9273088.jpg")

    UPDATES_CHANNEL = os.environ.get(" UPDATES_CHANNEL", "tgbotzxd") 
