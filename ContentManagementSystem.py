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

