#!/usr/bin/env python
#
# Copyright (C) 2013 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from lib import test_gui
from selenium import webdriver


class TestChrome(test_gui.TestGUI):
    @classmethod
    def _set_driver(cls):
        # ChromeDriver executable needs to be available in the path.
        # Please download from
        #   https://code.google.com/p/chromedriver/downloads/list
        driver = 'chromedriver'
        cls.driver = webdriver.Chrome(driver)


if __name__ == "__main__":
    unittest.main()