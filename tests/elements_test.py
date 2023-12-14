from pages.elements_page import TabElementsPage
from conftest import driver


class TestTabElements:
    def test_tab_login(self, driver):
        tab_page = TabElementsPage(driver, 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=901d071d-502a-4087-a677-b63f45d09a91&theme&auth_type')
        tab_page.open()
        text = tab_page.tab_on_login()
        assert text.text == 'Логин'

    def test_tab_email(self, driver):
        tab_page = TabElementsPage(driver, 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=901d071d-502a-4087-a677-b63f45d09a91&theme&auth_type')
        tab_page.open()
        text = tab_page.tab_on_email()
        assert text.text == 'Электронная почта'

    def test_tab_phone(self, driver):
        tab_page = TabElementsPage(driver, 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=901d071d-502a-4087-a677-b63f45d09a91&theme&auth_type')
        tab_page.open()
        text = tab_page.tab_on_phone()
        assert text.text == 'Мобильный телефон'

    def test_tab_ls(self, driver):
        tab_page = TabElementsPage(driver, 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=901d071d-502a-4087-a677-b63f45d09a91&theme&auth_type')
        tab_page.open()
        text = tab_page.tab_on_ls()
        assert text.text == 'Лицевой счёт'