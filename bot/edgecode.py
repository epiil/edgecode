#!/usr/bin/python
# -*- coding: latin-1 -*-


import os,socket,sys

network = 'chat.freenode.net'
port = 6667
channel = '#avpres'
username = 'edgecodebot'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM ) #create socket
irc.connect ( ( network, port ) ) #connect with the server
print irc.recv ( 4096 )
irc.send ( 'NICK ' + username + '\r\n' )
irc.send ( 'USER ' + username + ' ' + username + ' ' + username + ' :Python IRC\r\n' )
irc.send ( 'JOIN ' + channel + '\r\n' )
irc.send ( 'PRIVMSG ' + channel + ' :Submit queries for edge code identification. Symbol key: • (circle), ■ (square), ▲ (triangle), + (plus), x (equis). Example: "square, circle, triangle"\r\n' )
while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG  ' + data.split() [ 1 ] + '\r\n' ) #Response on PING, look up the IRC protocol for more info
   if data.find (username + ' go away' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Fine, if you do not want me\r\n' )
      irc.send ( 'QUIT\r\n' )
      irc.close()
      sys.exit()
   if data.find ( 'hi ' + username ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :I already said hi...\r\n' )
   if data.find ( 'KICK' ) != -1: #When you're kicked log back in XD
      irc.send ( 'JOIN ' + channel + '\r\n' )
   if data.find ( 'circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • (circle) 1916\r\n' )
   if data.find ( 'square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ (square) 1917\r\n' )
   if data.find ( 'triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ (triangle) 1918\r\n' )
   if data.find ( 'circle+circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • • (circle, circle) 1919\r\n' )
   if data.find ( 'square+square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ■ (square, square) 1920\r\n' )
   if data.find ( 'triangle+triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ▲ (triangle, triangle)' )
   print data