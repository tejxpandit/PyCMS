# Project   : Website CMS Python
# Title     : Common CMS Controls
# Author    : Tej Pandit
# Date      : Sept 2024

import dearpygui.dearpygui as dpg
from Custom_Themes import Custom_Themes

class CMS_Controls():

    def __init__(self):
        self.dataman = None
        self.data = None
        self.data_list = None
        self.selected_idx = 0
        self.selected_item = None
        self.item_identifier = ""
        self.file_data_identifier = ""
        self.selected_image_path = ""
        self.selected_image = ""
        self.theme = None

