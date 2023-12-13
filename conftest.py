import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='function')
def driver():
    """
    Фикстура для инициализации веб-драйвера Chrome с помощью Selenium и WebDriver Manager.

    Возвращает экземпляр веб-драйвера, максимизирует окно браузера и закрывает его после завершения теста.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
