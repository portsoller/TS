from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from time import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import os

# t = time()
rand = random.randint(1, 10000)
rand2 = random.randint(1000000000, 1009999999)
# print(rand)
print("Created number is " + str(rand2))
# driver options
start = time.time()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/home/abramenko/Python3/chromedriver",
chrome_options=chrome_options)

# Открытие файла для взятия данных тестового UAT

with open("data.txt", "r+") as f:
    handle = [x.strip() for x in f.readlines()]
login = handle[0]
password = handle[1]
uat = handle[2]
# print(login)
# print(password)
print("Environment = " + uat + ".tsescorts.com")
f.close()

# Open page

url = "https://" + uat + ".tsescorts.com"

driver.get(url)
# assert "TS Escorts" in driver.title
print("1. Home page is opened.")
wait = WebDriverWait(driver, 2)

# Advertise button
advertise_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#navbar_menu > li:nth-child(2) > a'))).click()

# sign up button
reg_button = driver.find_element_by_css_selector('body > div.container > div.row.advertising_row > div > a').click()


# выбор страны перед номером

elem19 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#registerform > div:nth-child(1) > div > div > div > div > div.selected-dial-code'))).click()
elem20 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#iti-item-us'))).click()

# phone input

phone_field = driver.find_element_by_css_selector('#user_registration_phone_raw')
phone_field.clear()
phone_field.send_keys(rand2)

# создание телефонного номера
login = '+1' + str(rand2)
# print(login)



# username input
username = driver.find_element_by_css_selector('#user_registration_uname')
username.clear()
username.send_keys('user' + str(rand))

# password input

passw = '123456'
password = driver.find_element_by_css_selector('#user_registration_password_first')
password.send_keys(passw)

# repeat password input
password = driver.find_element_by_css_selector('#user_registration_password_second')
password.send_keys(passw)

# email input
email_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#user_registration_email'))
    )
email_field.send_keys('portsoller+' + str(rand) + '@protonmail.com')

# privacy checkbox
privacy = driver.find_element_by_css_selector('#user_registration_terms')
privacy.click()

# Create account button
create_account = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit_id')))
create_account.click()
print("2. Account created.")

# Открытие файла для записи данных логина и пароля

file_1 = open("data.txt", "w")
# file_1.write(str(login) + '\n' + str(passw))
file_1.write(str(login) + '\n' + str(passw) + '\n' + str(uat))
file_1.close()

# Поиск поля для ввода кода верификации номера
verification = driver.find_element_by_css_selector('#code')
verification.click()
verification.send_keys(1111)
print("SMS code = 1111.")

# Кнопка Submit, для создания пользователя
submit = driver.find_element_by_css_selector('#submit')
submit.click()

print("Start to create new Escort Profile.")
# Нажатие кнопки создания профиля
select_type_profile = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div.row.account_row > div.col-md-9.col-sm-9.col-xs-12 > div > div.text-center > a:nth-child(2)')))
select_type_profile.click()

# Ввод Provider name
provider_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#name')))
provider_name.click()
provider_name.send_keys("MyProfileAgency")

# Вовод поля Tagline
tagline_name = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tagline')))
tagline_name.click()
tagline_name.send_keys("MyTagline")

# Select Location
select_location = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#select2-countryId-container'))).click()


# Выбор страны
country = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')))
country.send_keys("United States", Keys.ENTER)

# Select state
select_state = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#select2-stateId-container'))).click()

# Выбор штата
state = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')))
state.send_keys("Colorado", Keys.ENTER)

# Select city
select_city = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#select2-cityId-container'))).click()

# Выбор city
city = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')))
city.send_keys("Denver", Keys.ENTER)

# Поиск поля ABOUT field и его заполнение
about_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body'))).click()
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
elem = driver.find_element_by_xpath("/html/body")
elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing")

# Switch back to the "default content" (that is, out of the iframes)
driver.switch_to.default_content()

# Поиск и отметка чек-бокса "I will not put up naked pictures or videos...."
#check_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#naked_understand')))
#check_box.click()

# Сохранение профиля
save_profile = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#save'))).click()
print("3. Escort profile in Colorado, USA created successfully.")
wait = WebDriverWait(driver, 2)
assert "Escort Profile Created" in driver.title

# Переход на экран аккаунта
wait = WebDriverWait(driver, 2)
driver.get(url + "/account")

#  Покупка мембершипа --------------------------------------------------------------

# Нажатие кнопки покупки членства
buy_membership = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div.row.account_row > div.col-md-9.col-sm-9.col-xs-12 > div > div.prof > a.btn.btn-sm.btn-danger')))
buy_membership.click()

# Выбор типа членства членства
select_type_member = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#membership_0')))
select_type_member.click()

# Поиск поля промокод и ввод промокода "hunter" для США
promo_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#promocode')))
promo_input.click()
promo_input.send_keys("hunter")

# Поиск и нажатие кнопки NEXT
next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#next')))
next_button.click()

# Оплата 0$ по промокоду
Pay_0 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#next-pay')))
Pay_0.click()


print("4. Basic membership in USA (promo Hunter) paid successfully.")


# Переход на экран аккаунта
wait = WebDriverWait(driver, 2)
driver.get(url + "/account")


# пополнение бюджета ---------------------------------------------------------

# Нажатие кнопки пополнения бюджета
try:
    recharge_budget = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div.row.account_row > div.col-md-9.col-sm-9.col-xs-12 > div > div:nth-child(3) > div:nth-child(2) > a'))).click()
except:
    recharge_budget1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.container > div.row.account_row > div.col-md-9.col-sm-9.col-xs-12 > div > div:nth-child(4) > div:nth-child(2) > a'))).click()

# Выбор суммы пополнения
budget_amount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_recharge_2')))
budget_amount.click()


# Нажатие кнопки NEXT
next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_next')))
next_button.click()

# fname of card
fname_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#firstname')))
fname_input.clear()
fname_input.send_keys("John")

# lname
lname_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#lastname')))
lname_input.clear()
lname_input.send_keys("Connor")

# Address
address_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#address')))
address_input.clear()
address_input.send_keys("15 avenue")

# city
city_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#city')))
city_input.clear()
city_input.send_keys("Denver")

# zip
zip_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#zip')))
zip_input.clear()
zip_input.send_keys("12345")

# state
state_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#state')))
state_input.clear()
state_input.send_keys("Ohio")

# Country field select
country = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#select2-country-container'))).click()

# Выбор страны
country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')))
country_select.send_keys("United States", Keys.ENTER)

# Поле email
email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#email')))
email_input.clear()
email_input.send_keys('user' + str(rand) + '@gmail.com')

# Поле card
card_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#cardno')))
card_input.clear()
card_input.send_keys('4242424242424242')

# Card Expiration (month)
month_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#expMonth'))).click()
month_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#expMonth > option:nth-child(5)')))
wait = WebDriverWait(driver, 2)
month_select.click()

# Card Expiration (year)
year_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#expYear'))).click()
year_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#expYear > option:nth-child(3)')))
wait = WebDriverWait(driver, 2)
year_select.click()

# Поле CVC
cvc_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#csc')))
cvc_input.clear()
cvc_input.send_keys('123')

# Кнопка Add Card
add2_card = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#next-pay')))
add2_card.click()

# Ожидание добавления карты
try:
    element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, 'body > div.container > div.row > div > div > h1'))
    )
except TimeoutException as ex:
            print("6. Budget recharged successfully.")

# Переход на экран аккаунта
wait = WebDriverWait(driver, 2)
driver.get(url + "/account")

# Покупка обновлений --------------------------------------------------

# Нажатие кнопки покупки обновлений
topup_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div.row.account_row > div.col-md-9.col-sm-9.col-xs-12 > div > div:nth-child(5) > div:nth-child(2) > a')))
topup_button.click()

# Раскрытие дроп-даун количества обновлений
choose_amount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_repost')))
choose_amount.click()


# Выбор количества обновлений из раскрытого меню
select_amount = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_repost > option:nth-child(2)')))
select_amount.click()

# Нажатие кнопки "оплатить с бюджета"
pay_from_budget = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form_next')))
pay_from_budget.click()
print("7. Top-up updates purchased successfully.")

# Возврат на экран аккаунта
return_to_account = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div.row > div > div > p:nth-child(7) > a:nth-child(3)')))
return_to_account.click()

# Переход на экран аккаунта
wait = WebDriverWait(driver, 2)
driver.get(url + "/account")

# Нажатие кнопки смена локации
move_ad = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.container > div.row.account_row > div.col-md-9.col-sm-9.col-xs-12 > div > div.prof > a:nth-child(8)')))
move_ad.click()

# Select state
select_state = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#select2-stateId-container'))).click()

# Выбор штата
state = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')))
state.send_keys("Maine", Keys.ENTER)

# Select city
select_city = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#select2-cityId-container'))).click()

# Выбор city
city = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')))
city.send_keys("Portland", Keys.ENTER)

# Нажатие кнопки SAVE
save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#save')))
save_button.click()
print("8. Location changed successfully.")

# Переход на экран аккаунта
wait = WebDriverWait(driver, 2)
driver.get(url + "/account")


# Ending the test
wait = WebDriverWait(driver, 2)
assert "My Account" in driver.title
print("Test finished successfully.")
end = time.time()
script_duration = end - start
print("--------------------------------------------------")
print("Script duration: ", script_duration)

