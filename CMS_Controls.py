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

    # COMMON CONTROLS
    def createCommonControls(self):
        # ListView Group
        dpg.add_group(parent=self.tab, tag=self.lv)
        dpg.add_listbox(items=["None"], num_items=10, parent=self.lv, tag=self.li, callback=self.listSelect)
        dpg.add_separator(parent=self.lv)
        # ListView : ReorderView Group
        dpg.add_text("RE-ORDER", parent=self.lv)
        dpg.add_group(horizontal=True, parent=self.lv, tag=self.rg)
        dpg.add_button(label="MOVE UP", parent=self.rg, user_data=0, callback=self.reorder)
        dpg.add_button(label="MOVE DOWN", parent=self.rg, user_data=1, callback=self.reorder)
        dpg.add_separator(parent=self.lv)
        # ListView : Manage Buttons
        dpg.add_text("MANAGE", parent=self.lv)
        dpg.add_group(horizontal=True, parent=self.lv, tag=self.cg)
        edit_button = dpg.add_button(label="EDIT", parent=self.cg, callback=self.edit)
        dpg.add_button(label="DELETE", parent=self.cg, user_data="delete", callback=self.confirmationBox)
        dpg.add_separator(parent=self.lv)
        # ListView : Create Buttons
        dpg.add_text("CREATE", parent=self.lv)
        dpg.add_button(label="+ ADD NEW", parent=self.lv, callback=self.create)
        dpg.add_separator(parent=self.lv)
        dpg.add_separator(parent=self.lv)
        # ListView : Backup Buttons
        dpg.add_text("BACKUP : Backup current saved configuration (will overwrite previous backup)", parent=self.lv)
        backup_button = dpg.add_button(label="CREATE BACKUP", parent=self.lv, user_data="backup", callback=self.confirmationBox)
        dpg.add_text("RESTORE : Restore backup and overwrite all changes since backup", parent=self.lv)
        restore_button = dpg.add_button(label="RESTORE BACKUP", parent=self.lv, user_data="restore", callback=self.confirmationBox)
        dpg.add_separator(parent=self.lv)