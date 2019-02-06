from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

login_url = 'https://account.nicovideo.jp/login?next_url=my&site=nicolive'
my_url = 'http://live.nicovideo.jp/my'

driver = webdriver.Chrome(options=options)


def get_live():

    # ログイン処理
    driver.get(login_url)

    driver.find_element_by_id('input__mailtel').clear
    driver.find_element_by_id('input__mailtel').send_keys("claude0803sz@gmail.com")
    driver.find_element_by_id('input__password').clear
    driver.find_element_by_id('input__password').send_keys("bartok0803sz")
    driver.find_element_by_id('login__submit').click()

    # 現在放送中の番組を取得

    driver.get(my_url)

    live_item_count = len(driver.find_elements_by_class_name('liveItemTxt'))

    retval = []

    if 0 < live_item_count:
        for i in range(live_item_count):
            live_item = driver.find_elements_by_class_name('liveItemTxt')[i].text
            live_link = driver.find_element_by_xpath(f"""//*[@id='subscribeItemsWrap']
            /div/div[{live_item_count}]/div/h3/a""").get_attribute('href')

            retval.append(live_item)
            retval.append(live_link)
            retval.append('\n')

    else:
        retval.append('現在放送中の番組はありません。')

    return retval

    driver.close()
    driver.quit()
