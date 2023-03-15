from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Create a Service object for the ChromeDriver executable
chrome_service = Service(ChromeDriverManager().install())

# Create a new Chrome WebDriver instance using the Service object
driver = webdriver.Chrome(service=chrome_service)

# Navigate to a webpage
driver.get("https://en.wikipedia.org/wiki/Main_Page")

sleep(2)

# Open another page in order to perform Back/Forward actions
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Spain")
search_box.send_keys(Keys.ENTER)

sleep(2)

# Back/Forward/Refresh
driver.back()
sleep(1)
driver.forward()
sleep(1)
driver.refresh()


"""
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://www.youtube.com/")
"""

driver.execute_script("window.open('https://www.linkedin.com/');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
sleep(1)

# Open a new window
driver2 = webdriver.Chrome(service=chrome_service)
driver2.get("https://www.youtube.com/")
driver2.execute_script("window.open('https://www.nytimes.com/');")
sleep(5)


# Switch between windows/tabs
driver.switch_to.window(driver.window_handles[1])
sleep(5)

driver2.switch_to.window(driver2.window_handles[0])
sleep(5)

# Get  window size
size = driver.get_window_size()
print(f"Window size: {size}")

# Set the window size
driver.set_window_size(800, 600)
sleep(1)

# Minimize the window
driver.minimize_window()
sleep(1)
# Maximize the window
driver.maximize_window()
sleep(1)
# Full screen mode
driver.fullscreen_window()
sleep(1)

driver2.switch_to.window(driver2.window_handles[0])
driver.close()
sleep(5)

driver.quit()
driver2.quit()




