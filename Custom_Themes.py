# Project   : Website CMS Python
# Title     : Custom Themes
# Author    : Tej Pandit
# Date      : Sept 2024

from typing import List, Any, Callable, Union
import dearpygui.dearpygui as dpg

class Custom_Themes():

    def __init__(self):
        pass
    
    # THEME : Edit Button
    def EditTheme(self) -> Union[str, int]:
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Text                   , (30, 30, 30, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button                 , (83, 204, 105, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (182, 247, 194, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (83, 204, 105, 150))
        return theme
    
    # THEME : Backup and Restore Buttons
    def BackupRestoreTheme(self) -> Union[str, int]:
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Text                   , (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button                 , (76, 37, 115, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (135, 80, 189, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (76, 37, 115, 150))
        return theme
    
    # THEME : Publish Button
    def PublishTheme(self) -> Union[str, int]:
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Text                   , (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button                 , (138, 20, 60, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (209, 35, 94, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (138, 20, 60, 150))
        return theme
    
    # THEME : Save Button
    def SaveTheme(self) -> Union[str, int]:
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Text                   , (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button                 , (22, 107, 38, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (30, 158, 53, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (22, 107, 38, 150))
        return theme
    
    # THEME : Cancel Button
    def CancelTheme(self) -> Union[str, int]:
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Text                   , (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button                 , (153, 50, 35, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (222, 75, 54, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (153, 50, 35, 150))
        return theme
    
    # THEME : Image Button
    def ImageTheme(self) -> Union[str, int]:
        with dpg.theme() as theme:
            with dpg.theme_component(0):
                dpg.add_theme_color(dpg.mvThemeCol_Text                   , (50, 50, 50, 255))
                dpg.add_theme_color(dpg.mvThemeCol_Button                 , (200, 200, 200, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered          , (255, 255, 255, 255))
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive           , (200, 200, 200, 150))
        return theme
    
    def ApplyControlThemes(self, backup_button, restore_button, publish_button):
        backup_restore_theme = self.BackupRestoreTheme()
        dpg.bind_item_theme(backup_button, backup_restore_theme)
        dpg.bind_item_theme(restore_button, backup_restore_theme)
        publish_theme = self.PublishTheme()
        dpg.bind_item_theme(publish_button, publish_theme)

    def ApplyEditThemes(self, edit_button):
        edit_theme = self.EditTheme()
        dpg.bind_item_theme(edit_button, edit_theme)

    def ApplySaveCancelThemes(self, save_button, cancel_button):
        save_theme = self.SaveTheme()
        dpg.bind_item_theme(save_button, save_theme)
        cancel_theme = self.CancelTheme()
        dpg.bind_item_theme(cancel_button, cancel_theme)
    
    def ApplyEditImageThemes(self, image_upload_button):
        image_theme = self.ImageTheme()
        dpg.bind_item_theme(image_upload_button, image_theme)