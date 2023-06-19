from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
import time
import asyncio
from pyrogram.types import User, Message
import sys
import re
import os

bot = Client("bot",
             bot_token= "5509916510:AAEBfGlNW7hW8a-5p9wcxG30ybsQkDfkqeg",
             api_id= 27495136,
             api_hash= "4ccc4865eec4d8fde7530e71948b3424")


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(f"Hello I am a URL DOWNLOADER BOT \nPress /link")


@bot.on_message(filters.command("noob"))
async def restart_handler(_, m):
    await m.reply_text("**STOPPED**🛑🛑", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["link"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('Send link in **Name&link** format to download the url')
    input9: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(-1001738709369, x)
        await input.delete(True)
        file_name, ext = os.path.splitext(os.path.basename(x))
        credit = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
    raw = input9.text
    name = raw.split('&')[0]
    url = raw.split('&')[1] or raw
    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    
    Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text2}```\n\n**Url :-** ```{url}```"
    prog = await m.reply_text(Show)
    
    cc = f'>> **Name :** {name}'
    
    path = f"./downloads/"

    if "youtu" in url:
        if raw_text2 in ["144", "240", "480"]:
            ytf = f'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'
        elif raw_text2 == "360":
            ytf = "18/134"
        elif raw_text2 == "720":
            ytf = "22/136/18"
        elif raw_text2 =="1080":
            ytf = "137/399"
        else:
            ytf = 18
    else:
        ytf=f"bestvideo[height<={raw_text2}]"

    if "jwplayer" in url:
        if raw_text2 in ["180", "144"]:
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = f"{out['320x180 ']}/{out['256x144 ']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
        elif raw_text2 in ["240", "270"]:
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = f"{out['480x270 ']}/{out['426x240 ']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
        elif raw_text2 == "360":
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = out['640x360 ']
            except Exception as e:
                if e == 0:
                    raw_text2=="no"
                #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
        elif raw_text2 == "480":
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = f"{out['960x540 ']}/{out['852x480 ']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
            # cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
        elif raw_text2 == "720":
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = f"{out['1280x720 ']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
            # cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
        elif raw_text2 == "1080":
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf =f"{out['1920x1080 ']}/{['1920x1056']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
        else:
            # cmd = f'yt-dlp -F "{url}"'
            # k = await helper.run(cmd)
            #out = helper.vid_info(str(k))
            # ytf = out['640x360 ']
            #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            raw_text2=="no"
#             except Exception as e:
#                 print(e)

    if ytf == f'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]':
        cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}" "{url}"'

    # elif "jwplayer" in url:# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
    #     cmd=f'yt-dlp -o "{name}.mp4" "{url}"'    
    elif "adda247" in url:# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
        cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
    elif "kdcampus" or "streamlock" in url:
        cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
    elif ".pdf" in url: #and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
    elif "drive" in url:
        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
    elif raw_text2 == "no":# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
        cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
#             elif "unknown" in ytf:
#                 cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
    elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']
             cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
    elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"
             cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
    elif  "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
                        cmd=f'yt-dlp -o "{name}.mp4" "{url}"'

    else:
        cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}+bestaudio" "{url}"'

    try:
        download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
        os.system(download_cmd)
        filename = f"{name}.mp4"
        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
        thumbnail = f"{filename}.jpg"
        dur = int(helper.duration(filename))
        await prog.delete (True)
        try:
            await m.reply_video(f"{name}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur)

        except:
            await m.reply_text("There was an error while uploading file as streamable so, now trying to upload as document.")
            await m.reply_document(f"{name}.webm",caption=cc)
        os.remove(f"{name}.mp4")
        os.remove(f"{filename}.jpg")
    except Exception as e:
        await m.reply_text(e)
        await m.reply_text("Done")    
    
bot.run()
