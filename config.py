import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    VIP_USER = os.environ.get('VIP_USERS', '7490234582').split(',')
    VIP_USERS = [int(user_id) for user_id in VIP_USER]
