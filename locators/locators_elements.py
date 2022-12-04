from selene.support.shared import browser




class TestFormLocators:

    FIRSTNAME = browser.element('#firstName')
    LASTNAME = browser.element('#lastName')
    EMAIL = browser.element('#userEmail')
    GENDER_MEN = browser.element('[for="gender-radio-1"]')
    NUMBER = browser.element('#userNumber')

    BIRTH_INPUT = browser.element('#dateOfBirthInput')
    BIRTH_MONTH = browser.element('.react-datepicker__month-select')
    BIRTH_MONTH_VALUE = browser.element('[value="6"]')
    BIRTH_YEAR = browser.element('.react-datepicker__year-select')
    BIRTH_YEAR_VALUE = browser.element('[value="1999"]')
    BIRTH_MONTH_DAY = browser.element('.react-datepicker__day--008')

    SUBJECT = browser.element('#subjectsInput')
    HOBBIES_SPORTS = browser.element('[for="hobbies-checkbox-1"]')
    HOBBIES_MUSIC = browser.element('[for="hobbies-checkbox-3"]')
    PICTURE_UPLOAD = browser.element('#uploadPicture')

    ADDRESS = browser.element('#currentAddress')
    STATE = browser.element('#state')
    STATE_VALUE = browser.element('#react-select-3-input')
    CITY = browser.element('#city')
    CITY_VALUE = browser.element('#react-select-4-input')