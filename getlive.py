import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

OPTIONS = Options()
OPTIONS.add_argument('--headless')

LOGIN_URL = 'https://account.nicovideo.jp/login?next_url=my&site=nicolive'
MY_URL = 'http://live.nicovideo.jp/my'

NICOLIVE_MAIL = os.environ['NICOLIVE_MAIL']
NICOLIVE_PASS = os.environ['NICOLIVE_PASS']

driver = webdriver.Chrome(options=OPTIONS, executable_path='/usr/bin/chromedriver')


def get_live():

    # ログイン処理
    driver.get(LOGIN_URL)

    driver.find_element_by_id('input__mailtel').clear
    driver.find_element_by_id('input__mailtel').send_keys(NICOLIVE_MAIL)
    driver.find_element_by_id('input__password').clear
    driver.find_element_by_id('input__password').send_keys(NICOLIVE_PASS)
    driver.find_element_by_id('login__submit').click()

    # 現在放送中の番組を取得
    driver.get(MY_URL)

    live_item_count = len(driver.find_elements_by_class_name('liveItem'))
    print(live_item_count)
    retval = []

    if 0 < live_item_count <= 3:
        for i in range(live_item_count):
            xpath = f"""//*[@id='subscribeItemsWrap']/div/div[{i + 1}]/div/h3/a"""
            live_item = driver.find_elements_by_class_name('liveItemTxt')[i].text
            live_link = driver.find_element_by_xpath(xpath).get_attribute('href')
            live_link = live_link[:-12]

            retval.append(live_item)
            retval.append('\n')
            retval.append(live_link)
            retval.append('\n\n')

    elif 3 < live_item_count:
        for i in range(3):
            live_item = driver.find_elements_by_class_name('liveItemTxt')[i].text
            live_link = driver.find_element_by_xpath().get_attribute('href')
            live_link = live_link[:-12]

            retval.append(live_item)
            retval.append('\n')
            retval.append(live_link)
            retval.append('\n\n')

    else:
        retval.append('現在放送中の番組はありません。')

    return retval

    driver.close()
    driver.quit()
