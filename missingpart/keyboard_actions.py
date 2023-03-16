from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# Create a Service object for the ChromeDriver executable
chrome_service = Service(ChromeDriverManager().install())

# Create a new Chrome WebDriver instance using the Service object
driver = webdriver.Chrome(service=chrome_service)

# Navigate to a webpage
driver.get("http://uitestingplayground.com/textinput")

# Find the email input field
email = driver.find_element(By.ID, "newButtonName")

# Type the text and clear
email.send_keys("yulia@google.com")
sleep(2)
email.clear()
sleep(2)


driver2 = webdriver.Chrome(service=chrome_service)

# Navigate to another webpage
driver2.get("https://en.wikipedia.org/wiki/Main_Page")

sleep(2)
search_box = driver2.find_element(By.NAME, "search")
search_box.send_keys("Spain")
search_box.send_keys(Keys.ENTER)
sleep(3)


driver3 = webdriver.Chrome(service=chrome_service)
driver3.get("https://www.google.com/")
search = driver3.find_element(By.NAME, "q")
search.send_keys("find something interesting")
search.send_keys(Keys.COMMAND + "A")
sleep(3)
search.send_keys(Keys.DELETE)
sleep(3)





