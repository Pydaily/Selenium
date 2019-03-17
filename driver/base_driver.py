#!/usr/bin/env python
# -*- Coding:utf-8 -*-
from selenium import webdriver


class BaseDriver:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--disable-infobars')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.douban.com/")

    def get_driver(self):
        return self.driver