
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def test_warenkorb():

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
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)

    try:
        driver.switch_to.alert.accept()
    except:
        pass

    time.sleep(1)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    time.sleep(1)
    badge = driver.find_element(By.XPATH, '//*[@data-test="shopping-cart-badge"]')
    assert badge.text == "2"
    badge.click()
    time.sleep(1)

    try:
         assert "cart" in driver.current_url 
    except AssertionError:
        driver.save_screenshot("fehler_warenkorb.png")
        raise
    finally:
        driver.save_screenshot("check_warenkorb.png")
        driver.quit()