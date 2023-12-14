import time

from locators.elements_page_locators import TabElementsPageLocators
from pages.base_page import BasePage


class TabElementsPage(BasePage):
    locators = TabElementsPageLocators()

    def tab_on_login(self):
        self.element_is_visible(self.locators.TAB_LOGIN).click()
        return self.element_is_visible(self.locators.TEXT_SPAN)

    def tab_on_email(self):
        self.element_is_visible(self.locators.TAB_EMAIL).click()
        return self.element_is_visible(self.locators.TEXT_SPAN)

    def tab_on_phone(self):
        self.element_is_visible(self.locators.TAB_PHONE).click()
        return self.element_is_visible(self.locators.TEXT_SPAN)

    def tab_on_ls(self):
        self.element_is_visible(self.locators.TAB_LS).click()
        return self.element_is_visible(self.locators.TEXT_SPAN)

    def tab_on_login_send_email(self):
        self.element_is_visible(self.locators.TAB_LOGIN).click()
        self.element_is_visible(self.locators.INPUT_PHONE).send_keys('login@domain.com')
        self.element_is_visible(self.locators.INPUT_PASSWORD).click()
        return self.element_is_visible(self.locators.FILLED_TEXT_SPAN)

    def tab_on_login_send_phone(self):
        self.element_is_visible(self.locators.TAB_LOGIN).click()
        self.element_is_visible(self.locators.INPUT_PHONE).send_keys('+79699999999')
        self.element_is_visible(self.locators.INPUT_PASSWORD).click()
        return self.element_is_visible(self.locators.FILLED_TEXT_SPAN)
