from selenium.webdriver.common.by import By


class TabElementsPageLocators:
    INPUT_PHONE = (By.CSS_SELECTOR, "input[id='username']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    TAB_PHONE = (By.CSS_SELECTOR, "div[id='t-btn-tab-phone']")
    TAB_EMAIL = (By.CSS_SELECTOR, "div[id='t-btn-tab-mail']")
    TAB_LOGIN = (By.CSS_SELECTOR, "div[id='t-btn-tab-login']")
    TAB_LS = (By.CSS_SELECTOR, "div[id='t-btn-tab-ls']")
    TEXT_SPAN = (By.CSS_SELECTOR, "span[class='rt-input__placeholder']")
    '''
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='lastname']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "input[name='lastname']")
    EMAIL_OR_TELEPHONE =
    PASSWORD =
    PASSWORD_CONFIRMATION ='''