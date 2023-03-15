from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

chrome_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_service)

driver.get("https://example.cypress.io/commands/actions")

clickAction = driver.find_element(By.XPATH, "//button[@class = 'btn btn-lg btn-danger action-btn']")
sleep(2)
clickAction.click()
sleep(2)

doubleClickAction = driver.find_element(By.XPATH, "//div[@class = 'action-div']")
actions = ActionChains(driver)
actions.double_click(doubleClickAction).perform()
sleep(2)

rightClickAction = driver.find_element(By.XPATH, "//div[@class = 'rightclick-action-div']")
actions.context_click(rightClickAction).perform()
sleep(2)

horizontalScroll = driver.find_element(By.ID, "scrollable-horizontal")

driver.execute_script("arguments[0].scrollIntoView(true);", horizontalScroll)
sleep(2)

# scroll up
driver.execute_script("window.scrollTo(0, 0);")
sleep(2)

# scroll down
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sleep(2)

btn = driver.find_element(By.XPATH, "//button[@class ='btn btn-danger'][1]")
driver.execute_script("arguments[0].scrollIntoView();", btn)

# Drag and drop i did not find draggable objects in the suggested URL, so created with this one
driver2 = webdriver.Chrome(ChromeDriverManager().install())
driver2.maximize_window()
driver2.get("https://jqueryui.com/resources/demos/droppable/default.html")
sleep(3)

drag = driver2.find_element(By.ID, "draggable")
drop = driver2.find_element(By.ID, "droppable")
actions = ActionChains(driver2)
actions.drag_and_drop(drag, drop).perform()


# by offset
# actions.drag_and_drop_by_offset(drag, 150, 50).perform()
sleep(3)









