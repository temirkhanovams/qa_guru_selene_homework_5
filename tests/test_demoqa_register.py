import os
from selene.support.shared import browser
from selene import be, have, by, command


def test_search_none(browser_init):
    browser.element('#firstName').should(be.blank).type('Test')
    browser.element('#lastName').should(be.blank).type('Test')
    browser.element('#userEmail').should(be.blank).type('Test@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('9999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(by.text('1992')).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(by.text('December')).click()
    browser.element('.react-datepicker__month').click()
    browser.element(by.text('1')).click()
    browser.element('#subjectsInput').should(be.blank).type('Math').press_enter()
    browser.with_(timeout=browser.config.timeout * 3).element('[for="hobbies-checkbox-2"]').click()
    # browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#uploadPicture').send_keys(os.path.abspath('images/img.jpg'))
    browser.element('#currentAddress').click().type("Moscow Leninskiy av. 120")
    browser.element('#react-select-3-input').should(be.blank).type('N').press_enter()
    browser.element('#city').should(be.visible)
    browser.element('#react-select-4-input').should(be.blank).type('D').press_enter()
    browser.element('#submit').should(be.visible).press_enter()

    browser.element('#submit').execute_script('element.click()')


    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('tr td:nth-child(2)').should(have.texts
        (
        'Test Test',
        'Test@test.com',
        'Male',
        '9999999999',
        '01 December,1992',
        'Maths',
        'Reading',
        'img.jpg',
        'Moscow Leninskiy av. 120',
        'NCR Delhi'
    ))