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

    def createLoginWindow(self):
        # Login Window
        dpg.add_window(label="LOGIN", modal=True, no_close=True, no_resize=True, no_move=True, no_collapse=True, tag="window_login", width=350, height=200)
        dpg.add_input_text(label=": Server", default_value=server, parent="window_login", tag="input_server")
        dpg.add_input_text(label=": Username", default_value=username, parent="window_login", tag="input_user")
        dpg.add_input_text(label=": Password", default_value=password, password=True, parent="window_login", tag="input_password")
        dpg.add_checkbox(label="Save Login Credentials", default_value=False, parent="window_login", tag="checkbox_save_credentials")
        dpg.add_button(label="LOGIN", show=True, callback=self.login, parent="window_login", tag="login_button")
        dpg.add_text("", show=False, parent="window_login", tag="login_status")
        dpg.add_progress_bar(default_value=0.0, show=False, parent="window_login", tag="download_progress")
        dpg.add_text("", show=False, parent="window_login", tag="data_status")
        dpg.set_item_pos("window_login", [450, 200])

    def login(self):
        # Disable Login Window Temporarily
        dpg.hide_item("login_button")
        dpg.set_value("login_status", "Logging In...")
        dpg.show_item("login_status")
        # Get Login Credentials
        self.server = dpg.get_value("input_server")
        self.user = dpg.get_value("input_user")
        self.password = dpg.get_value("input_password")
        try:
            # Attempt FTP Connection
            self.ftp = FTP_TLS(self.server)
            self.ftp.login(user=self.user, passwd=self.password)
            self.ftp.prot_p()
            
            # Login Successful
            print("Login Successful!")
            dpg.set_value("login_status", "Login Successful!")
            self.login_status = True

            # Save Login Credentials if Checkbox = True
            if dpg.get_value("checkbox_save_credentials"):
                self.dataman.updateCredentials()
            time.sleep(3)
        except:
            # FTP Connection Failed
            print("Incorrect Login Credentials!")
            dpg.set_value("login_status", "Incorrect Login Credentials!")
            self.login_status = False
            self.attempts += 1
            print("Login Attempts Remaining : " + str(3-self.attempts))
            
            # Re-Enable Login Button
            time.sleep(3)
            dpg.hide_item("login_status")
            dpg.show_item("login_button")

        # If Login Successful --> Download Data
        if self.login_status:
            # Download Website Data
            dpg.set_value("login_status", "Downloading Website Data...")
            dpg.show_item("download_progress")
            self.dataman.login = self
            self.dataman.ftp = self.ftp
            self.dataman.downloadData()
            dpg.set_value("login_status", "Download Complete!")
            print("Download Complete!")
            time.sleep(1)

            # Update CMS with Data
            self.cms.data = self.dataman.data
            self.cms.updateCMSData()

            # Hide Login Window
            dpg.configure_item("window_login", show=False, modal=False)
            #dpg.show_item("login_button")

            # Proceed to CMS App
            dpg.show_item("window_cms")
            
        # Exit App after 3 Failed Login Attempts
        if self.attempts < 3:
            return(self.login_status)
        else:
            exit(1)

    def logout(self):
        if self.login_status:
            self.ftp.quit()
            self.login_status = False