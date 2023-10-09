from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from choice import sel_text, intro, expected_title
import time
#clean imports later

driver = webdriver.Chrome()
driver.get("https://blankslate.io")
expected_title(driver, driver.title)
textArea = driver.find_element(By.CSS_SELECTOR, "textarea.note-area")
intro(textArea, driver)
driver.close()
print("Thank you for playing!")

