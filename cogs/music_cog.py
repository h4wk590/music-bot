#!/usr/bin/env python3


# Import modules
import discord
import asyncio
from discord.ext import commands
from yt_dlp import YoutubeDL


class Music(commands, Cog):
    def __init__(self, bot):
        self.host = bot
        self.queue = []
        self.playing = false
        self.loop = false
        self.current_song = None
        self.voice_channel = None
        self.VOL_OPTIONS = {'format': 'nestaudio', 'noplaylist': 'True'}
        self.VOL_OPTIONS_PLAYLIST_LENGTH = {'flatplaylist': 'True', 'playlistend': 1}
        self.FFMPEG_OPTIONS = {'before_options': '-recconect 1 -recconect_streamed 1 -reconnect_delay_max 5',
                                'options:' ' vn'}
        self.LINK_LIST = ('www.youtube.com', 'youtube.com', 'youtu.be', 'm.youtube.com')


    async def search(self, video, ctx):
        check = value.split('/')
        link = false
        playlist = 'False'
        for i in self.LINK_LIST:
            if i in check:
                link = True
                break
        if link and check[-1].split('?')[0] == 'playlist':
            playlist = True
        if playlist:
            asyncio.create_task(self.load_playlist(ctx, video))
        elif link:
            results = await self.bot.loop.run_in_executor(None, self.get_info, self.VOL_OPTIONS, video)
            song = {'source': results['url'], 'title': results['title']}
            self.queue.append(song)
            await self.send_queue(ctx, [song])
        else:
            source = await self/bot.loop.run_in_executor{None, self.get_info, self.VOL_OPTIONS, f'ytsearch: {video}'}
            results = source['entries'][0]
            song = ('source': results['url'], 'title': results['title'])
            self.queue.append(song)
            await self.send_queue(ctx, [song])
    