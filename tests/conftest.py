from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_init():
    print('\nОткрываю браузер')
    browser.config.window_width = 1024
    browser.config.window_height = 780
    browser.open('https://demoqa.com/automation-practice-form')

    yield

    print('\nЗакрываю браузер')
    browser.quit()