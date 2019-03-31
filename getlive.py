import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

login_url = 'https://account.nicovideo.jp/login?next_url=my&site=nicolive'
my_url = 'http://live.nicovideo.jp/my'

NICOLIVE_MAIL = os.environ['NICOLIVE_MAIL']
NICOLIVE_PASS = os.environ['NICOLIVE_PASS']

driver = webdriver.Chrome(options=options)


def get_live():

    # ログイン処理
    driver.get(login_url)

    driver.find_element_by_id('input__mailtel').clear
    driver.find_element_by_id('input__mailtel').send_keys(NICOLIVE_MAIL)
    driver.find_element_by_id('input__password').clear
    driver.find_element_by_id('input__password').send_keys(NICOLIVE_PASS)
    driver.find_element_by_id('login__submit').click()

    # 現在放送中の番組を取得
    driver.get(my_url)

    live_item_count = len(driver.find_elements_by_class_name('liveItem'))
    print(live_item_count)
    retval = []

    if 0 < live_item_count <= 3:
        for i in range(live_item_count):
            live_item = driver.find_elements_by_class_name('liveItemTxt')[i].text
            live_link = driver.find_element_by_xpath(f"""//*[@id='subscribeItemsWrap']
            /div/div[{live_item_count}]/div/h3/a""").get_attribute('href')

            retval.append(live_item)
            retval.append('\n')
            retval.append(live_link)
            retval.append('\n\n')

    elif 3 < live_item_count:
        for i in range(3):
            live_item = driver.find_elements_by_class_name('liveItemTxt')[i].text
            live_link = driver.find_element_by_xpath(f"""//*[@id='subscribeItemsWrap']
            /div/div[{3}]/div/h3/a""").get_attribute('href')

            retval.append(live_item)
            retval.append('\n')
            retval.append(live_link)
            retval.append('\n\n')

    else:
        retval.append('現在放送中の番組はありません。')

    return retval

    driver.close()
    driver.quit()
