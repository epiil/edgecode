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
irc.send ( 'PRIVMSG ' + channel + ' :Submit queries for edge code identification. Symbol key: • (circle) | ■ (square) | ▲ (triangle) | + (plus) | x (equis). Query example: "square, circle, triangle"\r\n' )
while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG  ' + data.split() [ 1 ] + '\r\n' ) #Response on PING, look up the IRC protocol for more info
   if data.find (username + ' go away' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :ok\r\n' )
      irc.send ( 'QUIT\r\n' )
      irc.close()
      sys.exit()
   if data.find ( 'hi ' + username ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Submit queries for edge code identification. Symbol key: • (circle) | ■ (square) | ▲ (triangle) | + (plus) | x (equis). Query example: "square, circle, triangle"\r\n' )
   if data.find ( 'KICK' ) != -1: #When you're kicked log back in
      irc.send ( 'JOIN ' + channel + '\r\n' )
   if data.find ( 'circle, square, equis' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ■ x (circle, square, equis) 1982\r\n' )
   if data.find ( 'equis, triangle, equis' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x ▲ x (equis, triangle, equis) 1983\r\n' )
   if data.find ( 'triangle, square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ■ ▲ (triangle, square, triangle) 1984\r\n' )
   if data.find ( 'square, circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ • ▲ (square, circle, triangle) 1985\r\n' )
   if data.find ( 'triangle, circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ • ▲ (triangle, circle, triangle) 1986\r\n' )
   if data.find ( 'square, triangle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ▲ ▲ (square, triangle, triangle) 1987\r\n' )
   if data.find ( 'plus, plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + + ▲ (plus, plus, triangle) 1988\r\n' )
   if data.find ( 'equis, plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x + ▲ (equis, plus, triangle) 1989\r\n' )
   if data.find ( 'triangle, plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ + ▲ (triangle, plus, triangle) 1990\r\n' )
   if data.find ( 'equis, plus, equis' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x + x (equis, plus, equis) 1991\r\n' )
   if data.find ( 'square, plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ + ▲ (square, plus, triangle) 1992\r\n' )
   if data.find ( 'plus, triangle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + ▲ ▲ (plus, triangle, triangle) 1993\r\n' )
   if data.find ( 'plus, circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + • ▲ (plus, circle, triangle) 1994\r\n' )
   if data.find ( 'plus, square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + ■ ▲ (plus, square, triangle) 1995\r\n' )
   if data.find ( 'equis, circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x • ▲ (equis, circle, triangle) 1996\r\n' )
   if data.find ( 'equis, square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x ■ ▲ (equis, square, triangle) 1997\r\n' )
   if data.find ( 'equis, triangle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x ▲ ▲ (equis, triangle, triangle) 1998\r\n' )
   if data.find ( 'circle, equis, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • x ▲ (circle, equis, triangle) 1999\r\n' )
   if data.find ( 'square, square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ■ ▲ (square, square, triangle) 2000\r\n' )
   if data.find ( 'square, square, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ■ • (square, square, circle) 2001\r\n' )
   if data.find ( 'triangle, triangle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ▲ • (triangle, triangle, circle) 2002\r\n' )
   if data.find ( 'circle, triangle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ▲ • (circle, triangle, circle) 2003\r\n' )
   if data.find ( 'triangle, square, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ■ • (triangle, square, circle) 2004\r\n' )
   if data.find ( 'square, circle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ • • (square, circle, circle) 2005\r\n' )
   if data.find ( 'triangle, circle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ • • (triangle, circle, circle) 2006\r\n' )
   if data.find ( 'square, triangle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code:  ■ ▲ • (square, triangle, circle) 2007\r\n' )
   if data.find ( 'circle, circle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • • • (circle, circle, circle) 1928 1948\r\n' )
   if data.find ( 'plus, plus, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + + • (plus, plus, circle) 2008\r\n' )
   if data.find ( 'equis, plus, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x + • (equis, plus, circle) 2009\r\n' )
   if data.find ( 'triangle, plus, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ + • (triangle, plus, circle) 2010\r\n' )
   if data.find ( 'circle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • • (circle, circle) 1919 1939 1959 1979\r\n' )
   if data.find ( 'square, square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ■ (square, square) 1920 1940 1960 1980\r\n' )
   if data.find ( 'triangle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ▲ (triangle, triangle) 1921 1941 1961 1981\r\n' )
   if data.find ( 'circle, square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ■ (circle, square) 1922 1942 1962\r\n' )
   if data.find ( 'circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ▲ (circle, triangle) 1923 1943 1963 \r\n' )
   if data.find ( 'triangle, square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ■ (triangle, square) 1924 1944 1964\r\n' )
   if data.find ( 'square, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ • (square, circle) 1925 1945 1965\r\n' )
   if data.find ( 'triangle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ • (triangle, circle) 1926 1946 1966\r\n' )
   if data.find ( 'square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ▲ (square, triangle) 1927 1947 1967\r\n' )
   if data.find ( 'plus, plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ++ (plus, plus) 1968\r\n' )
   if data.find ( 'triangle, plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ + (triangle, plus) 1930 1950 1970\r\n' )
   if data.find ( 'circle, plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • + (circle, plus) 1931* 1951 1971\r\n' )
   if data.find ( 'square, plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ + (square, plus) 1932 1952 1972\r\n' )
   if data.find ( 'plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + ▲ (plus, triangle) 1933 1953 1973\r\n' )
   if data.find ( 'plus, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + • (plus, circle) 1934 1954 1974\r\n' )
   if data.find ( 'plus, square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + ■ (plus, square) 1935 1955 1975\r\n' )
   if data.find ( 'circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • (circle) 1916 1936 1956 1976\r\n' )
   if data.find ( 'square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ (square) 1917 1937 1957 1977\r\n' )
   if data.find ( 'triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ (triangle) 1918 1938 1958 1978\r\n' )
   if data.find ( 'plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + (plus) 1929 1949 1969\r\n' )
   print data
