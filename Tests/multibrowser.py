from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

# Chrome driver setup
chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Firefox driver setup
firefox_service = FirefoxService(executable_path=GeckoDriverManager().install())
firefox_options = FirefoxOptions()
firefox_options.add_argument("--start-maximized")
firefox_driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

# Open a window with 3 tabs for Wikipedia, Linkedin and Yahoo
chrome_driver.get("https://www.wikipedia.org/")
chrome_driver.execute_script("window.open('https://www.linkedin.com/');")
chrome_driver.execute_script("window.open('https://www.yahoo.com/');")

# Open a window with two tabs: Nytimes, Microsoft
firefox_driver.get("https://www.nytimes.com/")
firefox_driver.execute_script("window.open('https://www.microsoft.com/');")

# Switch to Yahoo and close it
chrome_driver.switch_to.window(chrome_driver.window_handles[2])
chrome_driver.close()

# Switch to Microsoft and do something
firefox_driver.switch_to.window(firefox_driver.window_handles[1])
firefox_driver.get("https://www.microsoft.com/en-us/")

# Close Nytimes
firefox_driver.switch_to.window(firefox_driver.window_handles[0])
firefox_driver.close()

# Close first window
chrome_driver.switch_to.window(chrome_driver.window_handles[0])
chrome_driver.close()

# Close all sessions
chrome_driver.quit()
firefox_driver.quit()
