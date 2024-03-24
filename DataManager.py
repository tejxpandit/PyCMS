# Project   : Website CMS Python
# Title     : Data Manager
# Author    : Tej Pandit
# Date      : March 2024

import os
import time
import json
from ftplib import FTP_TLS
import dearpygui.dearpygui as dpg

class DataManager():

    def __init__(self):
        self.ftp = None
        self.login = None
        self.data_folder = os.path.join(os.getcwd(), "data")
        self.filenames = ["alumni", 
                          "labmembers", 
                          "news", 
                          "publications", 
                          "recent-publications"]
        self.json_data = None
        self.decoding = False
        self.data = {}
