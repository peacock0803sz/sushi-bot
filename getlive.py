from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument('--headless')

url = 'http://live.nicovideo.jp/my'

driver = webdriver.Chrome()


def get_live():
    driver.get(url)

    driver.find_element_by_id('input__mailtel').clear
    driver.find_element_by_id('input__mailtel').send_keys("claude0803sz@gmail.com")
    driver.find_element_by_id('input__password').clear
    driver.find_element_by_id('input__password').send_keys("bartok0803sz")
    driver.find_element_by_id('login__submit').click()


get_live()
