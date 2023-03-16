from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.play1.automationcamp.ir/expected_conditions.html")
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("Wait Conditions"))  # wait tilll page load

trigger = driver.find_element(By.ID, "enabled_trigger")
target = driver.find_element(By.ID, "enabled_target")

trigger.click()

# wait.until(EC.attribute_contains(target, "class", "btn btn-success"))  was trying to wait till attribute value change
wait.until(EC.element_to_be_clickable(target))  # wait till element enabled
assert target.is_enabled()
assert target.text == "Enabled Button"

triggerVisibility = driver.find_element(By.ID, "visibility_trigger")
targetVisibility = driver.find_element(By.ID, "visibility_target")

triggerVisibility.click()

wait.until(EC.visibility_of(targetVisibility)) # wait visibility
assert targetVisibility.is_displayed()
assert targetVisibility.text == "Click Me"

triggerInvisibility = driver.find_element(By.ID, "invisibility_trigger") # wait invisibility
targetInvisibility = driver.find_element(By.ID, "invisibility_target")

triggerInvisibility.click()

wait.until(EC.invisibility_of_element_located(targetInvisibility))
assert not targetInvisibility.is_displayed()
