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