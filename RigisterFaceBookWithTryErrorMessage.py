from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# فتح المتصفح
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

# الضغط على Create new account
create_account_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Create new account']"))
)
create_account_btn.click()

# انتظار ظهور النموذج
wait.until(EC.visibility_of_element_located((By.NAME, "firstname")))

# تعبئة البيانات
driver.find_element(By.NAME, "firstname").send_keys("Khaled")
driver.find_element(By.NAME, "lastname").send_keys("Mohamed")

email_field = drive_
