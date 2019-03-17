#!/usr/bin/env python
# -*- Coding:utf-8 -*-
from driver.base_driver import BaseDriver


class BasePage:

    def __init__(self):
        self.driver = BaseDriver().get_driver()

    def extend_find_element(self,locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].style.background "
                                   "= 'rgb(138,43,226 )';",
                                   element)
        return element

    def switch_frame_by_element(self,element):
        self.driver.switch_to.frame(element)

    def get_element_text(self,element):
        return element.text

    def get_table_content(self,tabel_name):
        pass

    def set_value(self,element,value):
        element.clear()
        element.click()
        element.send_keys(value)

    def click_element(self,element):
        element.click()