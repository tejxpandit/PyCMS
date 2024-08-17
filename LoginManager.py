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
