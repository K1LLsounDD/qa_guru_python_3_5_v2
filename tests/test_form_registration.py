from selene.support.shared import browser
from locators.locators_elements import TestFormLocators
import os


browser.config.hold_browser_open = True
def test_student_registration_form():
    browser.open('/automation-practice-form')

    #user's characters
    TestFormLocators.UserCharacters.FIRSTNAME.type('Sergey')
    TestFormLocators.UserCharacters.LASTNAME.type('Golichenko')
    TestFormLocators.UserCharacters.EMAIL.type('example@.com')
    TestFormLocators.UserCharacters.GENDER_MEN.click()
    TestFormLocators.UserCharacters.NUMBER.type('880055355')

    #birthday
    TestFormLocators.Birthday.BIRTH_INPUT.click()
    TestFormLocators.Birthday.BIRTH_MONTH.click()
    TestFormLocators.Birthday.BIRTH_MONTH_VALUE.click()
    TestFormLocators.Birthday.BIRTH_YEAR.click()
    TestFormLocators.Birthday.BIRTH_YEAR_VALUE.click()
    TestFormLocators.Birthday.BIRTH_MONTH_DAY.click()

    #hobbies
    TestFormLocators.Hobbies.SUBJECT.type('Maths').press_enter()
    TestFormLocators.Hobbies.HOBBIES_SPORTS.click()
    TestFormLocators.Hobbies.HOBBIES_MUSIC.click()
    TestFormLocators.Hobbies.PICTURE_UPLOAD.set_value(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir, 'upload/AQA.png'
    )))

    #adress
    TestFormLocators.Address.ADDRESS.type('улица Пушкина, Дом Колотушкина')


