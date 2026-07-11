from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def test_sortierung():

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
    driver.save_screenshot("debug.png")

    try:
        driver.switch_to.alert.accept()
    except:
        pass

    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@data-test="product-sort-container"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[text()="Name (Z to A)"]').click()
    erstes_produkt = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    print("Erstes Produkt:", erstes_produkt)


    assert erstes_produkt == "Test.allTheThings() T-Shirt (Red)"
    driver.save_screenshot("sortierung.png")

    
    driver.quit()