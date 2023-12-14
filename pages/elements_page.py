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
