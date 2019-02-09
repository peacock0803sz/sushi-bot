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
    driver.find_element_by_id('input__mailtel').send_keys("claude0803.sz@gmail.com")
    driver.find_element_by_id('input__password').clear
    driver.find_element_by_id('input__password').send_keys("YdaUjtF72KyU")
    driver.find_element_by_id('login__submit').click()

    # 現在放送中の番組を取得
    driver.get(my_url)

    live_item_count = len(driver.find_elements_by_class_name('liveItemTxt'))
    if driver.find_element_by_id('sub_link1') is not None:
        driver.find_element_by_id('sub_link1').click()
    retval = []

    if 0 < live_item_count:
        for i in range(live_item_count):
            print(1)
            live_item = driver.find_elements_by_class_name('liveItemTxt')[i].text
            live_link = driver.find_element_by_xpath(f"""//*[@id='subscribeItemsWrap']
            /div/div[{1}]/div/h3/a""").get_attribute('href')

            retval.append(live_item)
            retval.append('\n')
            retval.append(live_link)
            retval.append('\n\n')

    else:
        retval.append('現在放送中の番組はありません。')

    driver.close()
    driver.quit()

    return retval
