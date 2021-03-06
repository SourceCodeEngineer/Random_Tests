from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Chrome(executable_path="P:\Selenium\chromedriver.exe")
elem = browser.find_element_by_selector("#rcmloginuser")
ac = ActionChains(browser)
ac.move_to_element(elem).move_by_offset(x_offset, y_offset).click().perform()
