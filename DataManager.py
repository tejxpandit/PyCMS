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

    def uploadData(self):
        # Reconnect to Server
        # self.login.reconnect()
        time.sleep(1.0)

        # Upload Modified Data to Server
        dpg.set_value("publishbox_text", "Uploading to NUAI Lab Website...")
        n_file = 0
        n_files = len(self.filenames)
        if True: #self.login.login_status:
            for file in self.filenames:
                # Enter Server Data Directory
                # self.login.change_server_directory("/data")

                # Get Data from Dictionary
                self.json_data = self.data[file]

                # Save Data Locally
                filename = os.path.join(self.upload_folder, file + ".json")
                print("Uploading Data : " + filename)
                with open(filename, "w") as output_file:
                    json.dump(self.json_data, output_file)

                # Upload Files
                upload_command = "STOR " + file + ".json"
                # with open(filename, "rb") as output_file:
                #     self.ftp.storbinary(upload_command, output_file)

                # Enter Server Image Directory
                # self.login.change_server_directory("/img/" + self.server_img_folders[file])

                # Fine all Image Files to be Uploaded
                for key in self.imagefiles[file]:
                    
                    # Fetch Image Filenames
                    img = self.imagefiles[file][key]

                    # Upload Files
                    img_filename = os.path.join(self.upload_image_folder, img)
                    print("Uploading Image : " + img_filename)
                    upload_command = "STOR " + img_filename
                    # with open(img_filename, "rb") as output_img_filename:
                    #     self.ftp.storbinary(upload_command, output_img_filename)

                # Update Download Progress Bar
                n_file += 1
                progress = n_file / n_files
                print(str(progress*100) + "%")
                dpg.set_value("upload_progress", progress)
                time.sleep(0.5)

            # Logout of Server Temporarily
            # self.login.logout()

            # Display Upload Status
            dpg.set_value("publishbox_text", "Website Updated")
            dpg.hide_item("upload_progress")
            dpg.show_item("publishbox_ok")


    def backupData(self):
        for file in self.filenames:
            # Get Data from Dictionary
            self.json_data = self.data[file]
            # Save Data in Local Backup Folder
            filename = os.path.join(self.backup_folder, file + ".json")
            with open(filename, "w") as output_file:
                json.dump(self.json_data, output_file)
        print("Data Backup Created")