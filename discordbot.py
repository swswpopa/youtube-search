# coding: utf-8
import re
import jaconv
import discord
from  discord.ext import tasks
from datetime import datetime, timedelta, timezone
import os

from urllib import request
from bs4 import BeautifulSoup
import json
JST = timezone(timedelta(hours=+9), 'JST')

    
    # 接続に必要なオブジェクトを生成
    with open("config.json","r") as f:
    TOKEN = json.load(f)["DISCORD_TOKEN"]

    default_url = "https://www.youtube.com"

    alredy_href_list = [[],[],[],[],[],[]]
    channel_list = [670181985557151745,670182016083296256,670182036417282080,670182058060152863,670182088871247883,670268190055727133]

    search_url_list = ["https://www.youtube.com/results?search_query=%E3%83%AF%E3%82%A4%E3%83%90%E3%83%BC%E3%83%B3+%E3%83%97%E3%83%AA%E3%82%B3%E3%83%8D&sp=CAI%253D",#ワイバーン
            "https://www.youtube.com/results?search_query=%E3%83%AF%E3%82%A4%E3%83%AB%E3%83%89%E3%82%B0%E3%83%AA%E3%83%95%E3%82%A9%E3%83%B3&sp=CAI%253D",#ワイルドグリフォン
            "https://www.youtube.com/results?search_query=%E3%83%A9%E3%82%A4%E3%83%87%E3%83%B3&sp=CAI%253D",#ライデン
            "https://www.youtube.com/results?search_query=%E3%83%8D%E3%83%97%E3%83%86%E3%83%AA%E3%82%AA%E3%83%B3&sp=CAI%253D",#ネプテリオン
            "https://www.youtube.com/results?search_query=%E3%82%A2%E3%82%AF%E3%82%A2%E3%83%AA%E3%82%AA%E3%82%B9&sp=CAI%253D",#アクアリオス
            "https://www.youtube.com/results?search_query=%E3%83%97%E3%83%AA%E3%82%B3%E3%83%8D&sp=CAI%253D" # プリコネ
            ]
    #guild_id = 640920770641395725

    for i,search_url in enumerate(search_url_list):
    html = request.urlopen(search_url)
    soup = BeautifulSoup(html, "html.parser")
    
    movie_list = soup.find_all("a",class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link")
    for movie in movie_list:
        if not movie["href"] in alredy_href_list[i]:
            alredy_href_list[i].append(movie["href"])

    print(alredy_href_list)

    # 60秒に一回ループ
    @tasks.loop(seconds=60)
    async def loop():
    global alredy_href_list
    print(datetime.now(JST),flush=True)
    # guild = client.get_guild(guild_id)
    print("hoge")
        for i,search_url in enumerate(search_url_list):
            html = request.urlopen(search_url)
            soup = BeautifulSoup(html, "html.parser")
        
        movie_list = soup.find_all("a",class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link")
        channel = client.get_channel(channel_list[i])
            for movie in movie_list:
                if not movie["href"] in alredy_href_list[i]:
                    alredy_href_list[i].append(movie["href"])
                    await channel.send(default_url+movie["href"])

    #ループ処理実行
    loop.start()


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
