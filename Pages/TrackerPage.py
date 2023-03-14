from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TrackerPage:
    USER_WORKSPACE = (By.XPATH, "//div[@class='cl-dropdown-toggle pointer cl-cut-text']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_user_workspace_text(self):
        user_workspace_element = self.wait.until(
            lambda d: d.find_element(*TrackerPage.USER_WORKSPACE)
        )
        return user_workspace_element.text
