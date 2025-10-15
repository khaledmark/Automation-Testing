from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.facebook.com/")

wait = WebDriverWait(driver, 15)

# Click Create new account
create_account = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@data-testid,'open-registration-form-button')]"))
)
create_account.click()

# First name
first_name = wait.until(
    EC.presence_of_element_located((By.NAME, "firstname"))
)
first_name.send_keys("Khaled")

# last name
last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys("Mohamed")

# mobile or email
email = driver.find_element(By.NAME, "reg_email__")
email.send_keys("khaled@example.com")

# password
password = driver.find_element(By.NAME, "reg_passwd__")
password.send_keys("Test@12345")

# اختار يوم الميلاد من dropdown
day = driver.find_element(By.ID, "day")
day.send_keys("5")

month = driver.find_element(By.ID, "month")
month.send_keys("Feb")

year = driver.find_element(By.ID, "year")
year.send_keys("1990")

# اختار gender
gender = driver.find_element(By.XPATH, "//input[@value='2']")
gender.click()

# (اختياري) تضغط زر Sign Up
sign_up = driver.find_element(By.NAME, "websubmit")
sign_up.click()
