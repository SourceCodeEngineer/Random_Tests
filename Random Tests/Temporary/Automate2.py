import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome(executable_path="P:\Selenium\chromedriver.exe")
browser.get("http://webmail.duroflex.com")

login_username = "info@duroflex.com"
login_password = "Flex,6134,inf"

email = browser.find_element_by_xpath('//*[@id="rcmloginuser"]')
email.send_keys(login_username)

password = browser.find_element_by_xpath('//*[@id="rcmloginpwd"]')
password.send_keys(login_password)

login_button = browser.find_element_by_xpath('//*[@id="rcmloginsubmit"]')
login_button.click()

i = 0
while i < 6:
    weiter_button = browser.find_element_by_xpath('//*[@id="rcmbtn116"]')
    weiter_button.click()
    i = i + 1

    if i < 3:
        time.sleep(1)
    else: time.sleep(5)

actions = ActionChains(browser)
actions.move_to_element_with_offset(browser.find_element_by_tag_name('body'), 0,0)
actions.move_by_offset(10, 10).click().perform()

#todo Move the offset to the right position