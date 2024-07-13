from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
# Setup WebDriver path and options
paths = r"C:\Users\HP\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.imdb.com/search/name/")
wait = WebDriverWait(driver, 10)
driver.execute_script("window.scrollTo(500, 500);")
name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='nameTextAccordion']/div[1]/label"))).click()
driver.find_element(By.XPATH, '//input[@name="name-text-input"]').send_keys("krishanth")
credit = driver.find_element(By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label').click()
cre = driver.find_element(By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')
actions = ActionChains(driver)
actions.send_keys_to_element(cre , "Holiday")
actions.pause(2)  # Wait for suggestions to appear
actions.send_keys(Keys.DOWN)  # Navigate to the first suggestion
actions.pause(1)  # Pause briefly to ensure the selection
actions.send_keys(Keys.ENTER)  # Press the Enter key to select
actions.perform()
# Confirmation
print("Search performed successfully.")
# # Close the browser
driver.quit()
