import allure
import pytest
from playwright.sync_api import Page, expect


@allure.feature('Test Baidu search')
@allure.story('Test Baidu basic search')
def test_baidu(page: Page) -> None:
    # Given the Baidu home page is displayed
    page.goto("https://baidu.com")

    # When the user searches for a phrase
    allure.attach(page.screenshot(), 'Case Success Screenshot', allure.attachment_type.PNG)


