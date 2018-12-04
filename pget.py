# -*- coding: utf-8 -*-
import os

helpmsg ='''------MCD pget插件------
!!pget [URL] -下载这个插件
--------------------------------'''

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!pget'):
      args = info.content.split(' ')
      if (len(args) == 1):
        for line in helpmsg.splitlines():
          server.tell(info.player, line)
      elif (len(args) == 2):
        result = os.system('cd plugins && wget -N ' + args[1])
        if result == 0:
          server.say('success')
        else:
          server.say('failed to download')
