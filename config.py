# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "12380656"))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
BOT_TOKEN = getenv("BOT_TOKEN", "7363815658:AAFgCXWm96WM-qP0wvbMzmYz4oxIFmcmNRk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7825510422").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sunnylona:jUmDmuPK98tyB1T9@cluster0.tonrs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002441594756")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002270567487"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
