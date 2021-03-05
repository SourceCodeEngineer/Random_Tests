import time
from selenium import webdriver

web = webdriver.Chrome(executable_path="P:\Selenium\chromedriver.exe")
web.get("https://www.swagbucks.com/surveys")

time.sleep(1)

email = web.find_element_by_xpath('//*[@id="sbxJxRegEmail"]')
email.send_keys("s.pircher@gmx.net")
time.sleep(1)
password = web.find_element_by_xpath('//*[@id="sbxJxRegPswd"]')
password.send_keys("Gamertag132")
time.sleep(1)
login = web.find_element_by_xpath('//*[@id="loginBtn"]')
login.click()
time.sleep(60)

i = 1
while i < 100000:
    survey_option = web.find_element_by_xpath(
        '//*[@id="middleInner"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/span[2]')
    survey_option.click()

    time.sleep(0.5)

    answer = web.find_element_by_xpath(
        '//*[@id="middleInner"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/span[1]')
    answer.click()

    time.sleep(0.5)

    send = web.find_element_by_xpath('//*[@id="middleInner"]/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/button')
    send.click()

    time.sleep(0.5)

    web.refresh()

    time.sleep(0.5)

else:
    web.close()
