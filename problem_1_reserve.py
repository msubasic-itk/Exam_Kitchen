from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('http://10.15.1.204:3000/reserve')


# INPUT VALUES

# name = 'Milos'
# email = 'pera@detlic.com'
# phone = '333000'
# date_for_assertion = '1997-08-29'
# time = '1155PM'
# time_for_assertion = '23:55'
# persons = '2'
#
#
# values_list = [name, email, phone, time, persons]
# values_assertion_list = [name, email, phone, date_for_assertion, time_for_assertion]

locators_and_values = {
    'name': 'Milos',
    'email': 'pera@detlic.com',
    'phone': '333000',
    'time': '1155PM',
    'persons': '2',
    'parking': 'switch-label',
    'date': {
        'day': '29',
        'month': 'Aug',
        'year': '1997'
    }
}


# OUTCAST SELECTORS

input_date_selector = (By.ID, 'date')
button_submit_selector = (By.ID, 'submitForm')


# EXECUTION

for key, value in locators_and_values.items():
    if key == 'parking':
        locator = (By.CLASS_NAME, value)
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(locator)).click()
    elif key == 'date':
        locator = (By.ID, key)
        element_date = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(locator)
        )
        element_date.send_keys(value['day'])
        element_date.send_keys(value['month'])
        element_date.click()
        element_date.send_keys(['year'])
    else:
        locator = (By.ID, key)
        WebDriverWait(browser, 20).until(EC.presence_of_element_located(locator)).send_keys(value)



element_submit = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located(button_submit_selector)
)

element_submit.click()

# element_name = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located(input_name_selector)
# )
# element_name.send_keys(name)
#
# element_email = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located(input_email_selector)
# )
# element_email.send_keys(email)
#
# element_phone = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located(input_phone_selector)
# )
# element_phone.send_keys(phone)
#
#
# element_date = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located(input_date_selector)
# )
#
# element_date.send_keys('29')
# element_date.send_keys('Aug')
# element_date.click()
# element_date.send_keys('1997')
#
#
# element_time = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located(input_time_selector)
# )
# element_time.send_keys(time)
#
#
#
# element_persons = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located(select_persons_selector)
# )
# Select(element_persons).select_by_value(persons)
#
# element_parking = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located(label_parking_selector)
# )
# element_parking.click()
#
# element_submit = WebDriverWait(browser, 20).until(
#     EC.presence_of_element_located(button_submit_selector)
# )
#
# element_submit.click()
#
# # EXECUTION
#
# assert browser.execute_script('return window.localStorage.getItem(arguments[0]);', 'name') == name
# assert browser.execute_script('return window.localStorage.getItem(arguments[0]);', 'email') == email
# assert browser.execute_script('return window.localStorage.getItem(arguments[0]);', 'phone') == phone
# assert browser.execute_script('return window.localStorage.getItem(arguments[0]);', 'date') == date_for_assertion
# assert browser.execute_script('return window.localStorage.getItem(arguments[0]);', 'time') == time_for_assertion
# assert browser.execute_script('return window.localStorage.getItem(arguments[0]);', 'person') == persons
# assert browser.execute_script('return window.localStorage.getItem(arguments[0]);', 'parking') == 'on'