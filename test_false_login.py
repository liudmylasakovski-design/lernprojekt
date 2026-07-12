
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def test_false_login():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    chrome_options.add_argument("--disable-features=PasswordCheck,SafeBrowsingEnhancedProtection")
    chrome_options.add_argument("--no-first-run")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_123")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    error = driver.find_element(By.XPATH, '//*[@data-test="error"]')
    

    try:
         assert error.text == "Epic sadface: Username and password do not match any user in this service"
    except AssertionError:
        driver.save_screenshot("fehler_false_login.png")
        raise
    finally:
        driver.save_screenshot("false_login.png")
        driver.quit()