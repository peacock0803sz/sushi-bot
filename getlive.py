import os

import requests
from bs4 import BeautifulSoup
from discord.ext import commands

LOGIN_URL = 'https://account.nicovideo.jp/login?next_url=my&site=nicolive'
MY_URL = 'http://live.nicovideo.jp/my'


def get_live_list():
    session = requests.session()
    url = 'https://account.nicovideo.jp/login/redirector'
    url_parm = '?show_button_twitter=1&site=nicolive&show_button_facebook=1&next_url=my'
    login_info = {'mail_tel': os.environ['NICOLIVE_MAIL'], 'password': os.environ['NICOLIVE_PASS']}
    r = session.post(url + url_parm, data=login_info)

    soup = BeautifulSoup(r.content, 'lxml')
    live_item_txt = soup.find_all('div', class_='liveItemTxt')
    start_times = [live.find('p', class_='start_time').get_text().strip() for live in live_item_txt]
    links = [live.find('h3').find('a').get('href')[:-12].strip() for live in live_item_txt]
    titles = [live.find('h3').find('a').get('title').strip() for live in live_item_txt]
    channels = [live.find_all('p')[1].get('title').strip() for live in live_item_txt]
    lives = []
    for i in range(len(live_item_txt)):
        lives.append({'title': titles[i], 'channel': channels[i], 'link': links[i], 'start_time': start_times[i]})
    return lives


class Live(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def now(self, ctx):
        text = []
        for s in get_live_list():
            text.append(f'{s["start_time"]}\n番組名: {s["title"]}\nチャンネル: {s["channel"]}\nURL: {s["link"]}\n')
        await ctx.send('\n\n'.join(text))


if __name__ == '__main__':
    import json
    [print(json.dumps(live, ensure_ascii=False)) for live in get_live_list()]
