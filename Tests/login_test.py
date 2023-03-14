import os
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.LoginPage import LoginPage
from Pages.TrackerPage import TrackerPage
from time import sleep


class TestLogin(unittest.TestCase):

    @pytest.mark.first
    def test_login_user1(self):
        # Set up Chrome options to use user1 profile
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=user1_profile")

        # Set up the Chrome driver for user1 with the specified options
        driver = webdriver.Chrome(options=options)

        # Log in as user1
        driver.get("https://app.clockify.me/en/login")
        login_page = LoginPage(driver)
        login_page.enter_username("kerakof701@moneyzon.com")
        login_page.enter_password("12345678")
        login_page.click_on_login_button()
        sleep(5)
        driver.quit()

    def test_login_user2(self):
        # Set up Chrome options to use user2 profile
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=user2_profile")

        # Set up the Chrome driver for user2 with the specified options
        driver = webdriver.Chrome(options=options)

        # Log in as user2
        driver.get("https://app.clockify.me/en/login")
        login_page = LoginPage(driver)
        login_page.enter_username("gadogam658@fenwazi.com")
        login_page.enter_password("12345678")
        login_page.click_on_login_button()
        sleep(5)
        driver.quit()

    def test_switch_users(self):
        # Set up Chrome options to use user1 profile
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=user1_profile")

        # Set up the Chrome driver for user1 with the specified options
        driver = webdriver.Chrome(options=options)

        # Open clockify with user1
        driver.get("https://app.clockify.me/tracker")

        # Get the user workspace text for user1
        tracker_page = TrackerPage(driver)
        user_workspace_text = tracker_page.get_user_workspace_text()

        expected_user_workspace_text = "Kerakof701's workspace"
        self.assertEqual(user_workspace_text, expected_user_workspace_text)

        # Close the driver
        driver.quit()

        # Set up Chrome options to use user2 profile
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=user2_profile")

        # Set up the Chrome driver for user2 with the specified options
        driver = webdriver.Chrome(options=options)

        # Open clockify with user2
        driver.get("https://app.clockify.me/tracker")

        # Get the user workspace text for user2
        tracker_page = TrackerPage(driver)
        user_workspace_text = tracker_page.get_user_workspace_text()

        expected_user_workspace_text = "Gadogam658's workspace"
        self.assertEqual(user_workspace_text, expected_user_workspace_text)

        # Close the driver
        driver.quit()