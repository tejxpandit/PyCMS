# Project   : Website CMS Python
# Title     : Login Manager
# Author    : Tej Pandit
# Date      : Aug 2024

import time
import dearpygui.dearpygui as dpg
from ftplib import FTP_TLS
try:
    from credentials import server, username, password
except:
    server = ""
    username = ""
    password = ""

class LoginManager():

    def __init__(self):
        self.server = server
        self.user = username
        self.password = password
        self.ftp = None
        self.dataman = None
        self.cms = None
        self.login_status = False
        self.attempts = 0