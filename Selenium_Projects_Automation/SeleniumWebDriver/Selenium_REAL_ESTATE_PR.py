
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

print(driver.find_element(By.LINK_TEXT, 'California Real Estate').get_attribute("href"))
print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))
assert "California Real Estate" in driver.title
print("California Real Estate", driver.title)

driver.find_element(By.ID, "send-us-a-message")
driver.find_element(By.XPATH, "//div[@class='bottom-sticky__ad-close-btn']").click()
driver.find_element(By.ID, "g2-name").send_keys("Anastasia")
driver.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("anastasia123@yahoo.com")
driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Hello!\n"
"Please provide me support , i am having  system error.\nBest regards\nAnastasia")

driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").send_keys('\n')
print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))
driver.quit()