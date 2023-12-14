import time

from selenium.webdriver.common.by import By
from pages.elements_page import TabElementsPage
from conftest import driver


def test(driver):
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=901d071d-502a-4087-a677-b63f45d09a91&theme&auth_type')
    time.sleep(3)
    text = driver.find_element(By.CSS_SELECTOR, "span[class='rt-input__placeholder']").text
    assert text == 'Мобильный телефон'
