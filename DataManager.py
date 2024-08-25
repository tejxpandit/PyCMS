# Project   : Website CMS Python
# Title     : Data Manager
# Author    : Tej Pandit
# Date      : August 2024

import os
import shutil
import time
import json
from ftplib import FTP_TLS
import dearpygui.dearpygui as dpg

class DataManager():

    def __init__(self):
        self.ftp = None
        self.login = None
        self.credentials_file = os.path.join(os.getcwd(), "credentials.py")
        self.data_folder = os.path.join(os.getcwd(), "data")
        self.upload_folder = os.path.join(os.getcwd(), "upload")
        self.upload_image_folder = os.path.join(os.getcwd(), "upload", "images")
        self.backup_folder = os.path.join(os.getcwd(), "backup")
        self.filenames = ["alumni", 
                          "labmembers", 
                          "news", 
                          "publications", 
                          "recent-publications"]
        self.server_img_folders = {"labmembers":"labmembers",
                                   "news":"news",
                                   "recent-publications":"pubs"}
        self.imagefiles = {}
        self.json_data = None
        self.decoding = False
        self.data = {}
        self.initDataFolders()
        self.initImageUploadDict()

    def initDataFolders(self):
        # Data Folder Check
        if os.path.exists(self.data_folder):
            shutil.rmtree(self.data_folder, ignore_errors=True)
        os.makedirs(self.data_folder)

        # Upload Folder Check
        if os.path.exists(self.upload_folder):
            shutil.rmtree(self.upload_folder, ignore_errors=True)
        os.makedirs(self.upload_folder)
        os.makedirs(self.upload_image_folder)

        # Backup Folder Check
        if not os.path.exists(self.backup_folder):
            os.makedirs(self.backup_folder)
        
    def initImageUploadDict(self):
        for file in self.filenames:
            self.imagefiles[file] = {}

    def initCredentials(self):
        if not os.path.exists(self.credentials_file):
            with open("credentials.py", "w") as file:
                file.write('server=""\nusername=""\npassword=""')

    def updateCredentials(self):
        if os.path.exists(self.credentials_file):
            with open("credentials.py", "w") as file:
                cred = 'server="' + self.login.server + '"\nusername="' + self.login.user + '"\npassword="' + self.login.password + '"'
                file.write(cred)

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
            self.login.change_server_directory("/data") # Enter Server Data Directory
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

        # print(self.data)
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

    def restoreBackup(self):
        for file in self.filenames:
            filename = os.path.join(self.backup_folder, file + ".json")
            with open(filename) as input_file:
                self.data[file] = json.load(input_file)
        print("Backup Data Restored")

    def copyImage(self, path, filename, file, identifier):
        try:
            shutil.copy(path, self.upload_image_folder)
            self.imagefiles[file][identifier] = filename
            # print(self.imagefiles)
        except:
            print("Failed to Fetch Image!")

    # TESTING : LOCAL DATA LOADER
    def loadLocalData(self):
        for file in self.filenames:
            local_data_folder = os.path.join(os.getcwd(), "localdata")
            filename = os.path.join(local_data_folder, file + ".json")
            with open(filename) as input_file:
                self.data[file] = json.load(input_file)

    # TESTING : DATA LOGGER
    def logData(self):
        for data_name in self.data:
            print(data_name, self.data[data_name])