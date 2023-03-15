from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.play2.automationcamp.ir/")

male_rb = driver.find_element(By.ID, "male")
male_rb.click()
female_rb = driver.find_element(By.ID, "female")
female_rb.click()
sleep(2)

opt2check_box = driver.find_element(By.NAME, "option2")
opt2check_box.click()
sleep(2)
opt2check_box.click()

dropdownElement = driver.find_element(By.ID, "option")
dropdownElement.click()
sleep(2)
dropdown = Select(dropdownElement)
dropdown.select_by_visible_text("Option 3")
sleep(2)

slider = driver.find_element(By.ID, "a")
slider_width = slider.size['width']

actions = ActionChains(driver)
# Move slider to 100%
actions.click_and_hold(slider).move_by_offset(slider_width/2, 0).release().perform()

# Move slider to 0%
actions.click_and_hold(slider).move_by_offset(-slider_width/2, 0).release().perform()
sleep(2)

# alert
alertBtn = driver.find_element(By.XPATH, "//button[@onclick='alertfunction()']")
alertBtn.click()
sleep(5)
alert_popup = driver.switch_to.alert
sleep(5)
alert_popup.accept()

# tooltip
tooltipElement = driver.find_element(By.XPATH, "//div[@class='tooltip']")
actions.move_to_element(tooltipElement).perform()
print(tooltipElement.text)



driver2 = webdriver.Chrome(ChromeDriverManager().install())
driver2.get("https://www.play1.automationcamp.ir/frames.html")
sleep(2)
driver2.switch_to.frame('frame1')
driver2.find_element(By.ID, 'click_me_1').click()
sleep(2)
