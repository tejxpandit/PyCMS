# Project   : Website CMS Python
# Title     : Content Management System
# Author    : Tej Pandit
# Date      : March 2024

import dearpygui.dearpygui as dpg

from CMS_Members import CMS_Members
from CMS_Alumni import CMS_Alumni
from CMS_News import CMS_News
from CMS_Publications import CMS_Publications
from CMS_RecentPubs import CMS_RecentPubs

class ContentManagementSystem():

    def __init__(self):
        self.dataman = None
        self.data = None
        self.cms_members = CMS_Members()
        self.cms_alumni = CMS_Alumni()
        self.cms_news = CMS_News()
        self.cms_pubs = CMS_Publications()
        self.cms_rpubs = CMS_RecentPubs()

    def centerPosition(self, tag):
        vw = dpg.get_viewport_client_width()
        vh = dpg.get_viewport_client_height()
        ww = dpg.get_item_width(tag)
        wh = dpg.get_item_height(tag)
        print([(vw / 2) - (ww / 2), (vh / 2) - (wh / 2)])
        dpg.set_item_pos(tag, [(vw / 2) - (ww / 2), (vh / 2) - (wh / 2)])

    def createCMSWindow(self):
        # CMS Window
        dpg.add_window(label="NUAI Lab : Content Management System", width=1100, height=600, show=False, tag="window_cms")
        dpg.add_tab_bar(parent="window_cms", tag="tab_bar_cms")
        dpg.add_tab(label="Team Members", parent="tab_bar_cms", tag="tab_members")
        dpg.add_tab(label="Alumni", parent="tab_bar_cms", tag="tab_alumni")
        dpg.add_tab(label="News", parent="tab_bar_cms", tag="tab_news")
        dpg.add_tab(label="Publications", parent="tab_bar_cms", tag="tab_pubs")
        dpg.add_tab(label="Featured Pubs", parent="tab_bar_cms", tag="tab_feat_pubs")
        dpg.add_tab(label="Sponsors", parent="tab_bar_cms", tag="tab_sponsors")
        dpg.set_item_pos("window_cms", [30, 30])

        # Confirmation Box
        dpg.add_window(label="Confirmation", modal=False, show=False, tag="confirmation_box", no_title_bar=True)
        dpg.add_text("Are you sure you want to " + " ?", parent="confirmation_box", tag="confirmationbox_text")
        dpg.add_separator(parent="confirmation_box")
        dpg.add_group(horizontal=True, parent="confirmation_box", tag="confirmation_box_controls")
        dpg.add_button(label="Yes", width=75, user_data="", parent="confirmation_box_controls", tag="confirmationbox_yes", callback=None)
        dpg.add_button(label="Cancel", width=75, user_data="", parent="confirmation_box_controls", tag="confirmationbox_cancel", callback=None)
        dpg.set_item_pos("confirmation_box", [450, 250])

        # Publish Box
        dpg.add_window(label="Publishing to Website", modal=False, show=False, tag="publish_box", no_title_bar=True)
        dpg.add_text("Publishing to NUAI Lab Website...", parent="publish_box", tag="publishbox_text")
        dpg.add_progress_bar(default_value=0.0, show=False, parent="publish_box", tag="upload_progress")
        dpg.add_button(label="OK", show=False, parent="publish_box", tag="publishbox_ok", callback=lambda: dpg.configure_item("publish_box", show=False, modal=False))
        dpg.set_item_pos("publish_box", [450, 250])