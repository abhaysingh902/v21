import os

class Config(object):
    BOT_TOKEN = os.environ.get("7474534383:AAHw01F5saTV_H7uIEGXjBxbboafE4lTHrk")
    API_ID = int(os.environ.get("25228502"))
    API_HASH = os.environ.get("5973b28ff479dddaa1dc1c351e1bd370")
    VIP_USER = os.environ.get('VIP_USERS', '7490234582').split(',')
    VIP_USERS = [int(user_id) for user_id in VIP_USER]
