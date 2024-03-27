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

    # Decode FTP Data Chunks 8192'b, Decode as Strings and Concatenate them
    def decodeData(self, data):
        if self.decoding:
            self.json_data += data.decode()
        else:
            self.json_data = data.decode()
            self.decoding = True

    def downloadData(self):
        n_file = 0
        n_files = len(self.filenames)
        if self.login.login_status:
            for file in self.filenames:
                try:
                    # Download Data Files
                    download_command = "RETR " + file + ".json"
                    self.ftp.retrbinary(download_command, self.decodeData)
                    self.decoding = False
                    print("Downloaded File : " + file + ".json")
                except:
                    print("Failed to Download File : " + file + ".json")

                # Save Data Locally
                # filename = os.path.join(self.data_folder, file + ".json")
                # with open(filename, "w") as output_file:
                #     output_file.write(self.json_data)

                # Add Data to Dictionary
                self.data[file] = json.loads(self.json_data)

                # Update Download Progress Bar
                n_file += 1
                progress = n_file / n_files
                print(str(progress*100) + "%")
                dpg.set_value("download_progress", progress)
                time.sleep(0.5)

        # Logout of Server Temporarily
        self.login.logout()