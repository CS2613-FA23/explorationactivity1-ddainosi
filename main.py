from selenium import webdriver
from selenium.webdriver.common.by import By
from functions import intro, expected_title

driver = webdriver.Chrome()
driver.get("https://blankslate.io")
expected_title(driver, driver.title)
textArea = driver.find_element(By.CSS_SELECTOR, "textarea.note-area")
intro(textArea, driver)
driver.close()
print("Thank you for playing!")

