# Project   : Website CMS Python
# Title     : Website CMD Main
# Author    : Tej Pandit
# Date      : March 2024

import dearpygui.dearpygui as dpg
from LoginManager import LoginManager
from ContentManagementSystem import ContentManagementSystem
from DataManager import DataManager

# Create Viewport [App Window]
dpg.create_context()
dpg.create_viewport(title='NUAI Lab Website Manager', width=1200, height=700)

# Initialize Components
cms = ContentManagementSystem()
dataman = DataManager()
login = LoginManager()

# Initilialize CMS and Data Manager Objects
login.dataman = dataman
login.cms = cms
cms.dataman = dataman

# TESTING : LOAD LOCAL DATA
# dataman.loadLocalData()

# Create CMS Window
cms.createCMSWindow()

# Create Login Window
login.createLoginWindow()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()