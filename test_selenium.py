from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def test_login_falsch():

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("falscher_user")
    driver.find_element(By.ID, "password").send_keys("falsches_passwort")
    driver.find_element(By.ID, "login-button").click()

    fehler = driver.find_element(By.XPATH, '//*[@data-test="error"]')
    assert "Epic sadface" in fehler.text

    driver.quit()