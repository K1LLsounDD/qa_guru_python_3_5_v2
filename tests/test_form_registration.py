from selene.support.shared import browser
from locators.locators_elements import TestFormLocators
import os


browser.config.hold_browser_open = True
def test_student_registration_form():
    browser.open('/automation-practice-form')

    #user's characters
    TestFormLocators.FIRSTNAME.type('Sergey')
    TestFormLocators.LASTNAME.type('Golichenko')
    TestFormLocators.EMAIL.type('example@.com')
    TestFormLocators.GENDER_MEN.click()
    TestFormLocators.NUMBER.type('880055355')

    #birthday
    TestFormLocators.BIRTH_INPUT.click()
    TestFormLocators.BIRTH_MONTH.click()
    TestFormLocators.BIRTH_MONTH_VALUE.click()
    TestFormLocators.BIRTH_YEAR.click()
    TestFormLocators.BIRTH_YEAR_VALUE.click()
    TestFormLocators.BIRTH_MONTH_DAY.click()

    #hobbies
    TestFormLocators.SUBJECT.type('Maths').press_enter()
    TestFormLocators.HOBBIES_SPORTS.click()
    TestFormLocators.HOBBIES_MUSIC.click()
    TestFormLocators.PICTURE_UPLOAD.set_value(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir, 'upload/AQA.png'
    )))

    #adress
    TestFormLocators.ADDRESS.type('улица Пушкина, Дом Колотушкина')


