## 手順

1. https://www.nicovideo.jp/my/ にアクセスする
2. ログインする
   1. 入力 input#input__mailtel
   2. 入力 input#input__password
   3. click input__login__submit
3. for: `liveItem`が
   - ある=>`a`タグのurlを返す
   - ない=>何もしない
4. 閉じる

- time/5minで
  - get_live == 0なら何もしない
  - get_live != 0ならメッセージ送信

### ToDo
- get_liveして5分前と変わって
  - るならメッセージ送信
  - ないなら何もしない

## discordログ
```
くじゃく今日 午後2時19分
今度はHerokuへのデプロイで詰まりました....
dIscord.pyのimportに失敗してるのでしょうか
➜ git push heroku master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 352 bytes | 352.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing dependencies with Pipenv 2018.5.18…
remote:        Installing dependencies from Pipfile.lock (695174)…
remote: -----> Discovering process types
remote:        Procfile declares types -> bot
remote: 
remote: -----> Compressing...
remote:        Done: 63.2M
remote: -----> Launching...
remote:        Released v14
remote:        https://secure-everglades-92240.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/secure-everglades-92240.git
   6ff590b..fd5edb7  master -> master
くじゃく今日 午後2時27分
https://gist.github.com/peacock0803sz/1cd4d2a35587bdd7ef3359979b324324#file-heroku-logs
heroku logsが長かったのでgistで失礼します

ケシゴモン今日 午後4時41分
aiohttpがダウンロードされていないっぽーい
requirement.txt(名前間違ってたらスマーン！)にdiscordって書いた？(それ書いたら自動でaiohttpも導入されるはず)

Episword今日 午後4時56分
pipfileの中身がみたいです。

Peacock今日 午後4時57分
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
selenium = "*"
discord-py = {file = "https://github.com/Rapptz/discord.py/archive/rewrite.zip"}
flake8 = "*"
chromedriver-binary = "*"

[requires]
python_version = "3.7"

Episword今日 午後5時1分
Procfileの中身もお願いします。

Peacock今日 午後5時5分
bot: python main.py

Episword今日 午後5時9分
うーん、ログ見る限りはdiscord自体のインストールはできている感じがしますね…。

Peacock今日 午後5時10分
aiohttpをpipfileに書いたほうがいいんでしょうか....?

Episword今日 午後5時13分
うーん、https経由なのが悪いのだろうか…。
...
[packages]
...
discord-py = {extras = ["voice"],git = "https://github.com/Rapptz/discord.py",ref = "rewrite"}
...

gitで指定するとどうなるんでしょうか。

Peacock今日 午後5時40分
➜ git push heroku master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 345 bytes | 345.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing dependencies with Pipenv 2018.5.18…
remote:        Your Pipfile.lock (695174) is out of date. Expected: (9ceff7).
remote:        Aborting deploy.
remote:  !     Push rejected, failed to compile Python app.
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !       Push rejected to secure-everglades-92240.
remote: 
To https://git.heroku.com/secure-everglades-92240.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/secure-everglades-92240.git'
pushすらできなくなりました....gitのオペミスもありえますが

デボン今日 午後5時48分
Pipfile.lockが更新されてないみたいです

Peacock今日 午後5時54分
https://github.com/pypa/pipenv/issues/2871
Running pipenv gives TypeError: 'module' object is not callable ·...
Issue description I just installed pipenv on a pyenv installed Python 3.7.0 interpreter. Starting in a clean directory resulted in an exception. Expected result pipenv to not crash. Actual result $...

pip,pipenvをダウングレードしてみます

デボン今日 午後5時59分
git pushの前にpipenv lockを実行して効くかも

Peacock今日 午後6時23分
gitでやらかしてherokuのbuilds limitに達したようです....orz
時間置いて再度試してみます

Peacock今日 午後6時41分
今度はChrome Web Driverのインストールでコケてるみたいです....例によってheroku logsの結果をgistで貼ります
https://gist.github.com/peacock0803sz/4606679ac014f153f31908ccf275b75d#file-1827-log
Gist
heroku logs
heroku logs. GitHub Gist: instantly share code, notes, and snippets.

Peacock今日 午後10時57分
Settings/Buildpacksに
https://github.com/heroku/heroku-buildpack-chromedriver.git
https://github.com/heroku/heroku-buildpack-google-chrome.git

を追加したら通りました、Bot自体も動作してます。
```