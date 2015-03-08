#!/usr/bin/python
# -*- coding: latin-1 -*-


import os,socket,sys

network = 'chat.freenode.net'
port = 6667
channel = '#avpres'
username = 'edgecodes'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM ) #create socket
irc.connect ( ( network, port ) ) #connect with the server
print irc.recv ( 4096 )
irc.send ( 'NICK ' + username + '\r\n' )
irc.send ( 'USER ' + username + ' ' + username + ' ' + username + ' :Python IRC\r\n' )
irc.send ( 'JOIN ' + channel + '\r\n' )
irc.send ( 'PRIVMSG ' + channel + ' :Edgecode: Submit queries for edge code identification.\r\n' )
irc.send ( 'PRIVMSG ' + channel + ' :Symbol key: • (circle) | ■ (square) | ▲ (triangle) | + (plus) | x (equis)\r\n' )
irc.send ( 'PRIVMSG ' + channel + ' :Query example: "square, circle, triangle" , "What is the edge code for the year 1916"\r\n' )
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
    irc.send ( 'PRIVMSG ' + channel + ' :Edgecode: Submit queries for edge code identification.\r\n' )
    irc.send ( 'PRIVMSG ' + channel + ' :Symbol key: • (circle) | ■ (square) | ▲ (triangle) | + (plus) | x (equis)\r\n' )
    irc.send ( 'PRIVMSG ' + channel + ' :Query example: "square, circle, triangle" , "What is the edge code for the year 1916"\r\n' )
  if data.find ( 'KICK' ) != -1: #When you're kicked log back in
    irc.send ( 'JOIN ' + channel + '\r\n' )

  def find_edge():
    if data.find (username + ' circle, square, equis' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ■ x (circle, square, equis) 1982\r\n' )
    elif data.find (username +  ' equis, triangle, equis' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x ▲ x (equis, triangle, equis) 1983\r\n' )
    elif data.find (username + ' triangle, square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ■ ▲ (triangle, square, triangle) 1984\r\n' )
    elif data.find (username + ' square, circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ • ▲ (square, circle, triangle) 1985\r\n' )
    elif data.find (username + ' triangle, circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ • ▲ (triangle, circle, triangle) 1986\r\n' )
    elif data.find (username + ' square, triangle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ▲ ▲ (square, triangle, triangle) 1987\r\n' )
    elif data.find (username + ' plus, plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + + ▲ (plus, plus, triangle) 1988\r\n' )
    elif data.find (username + ' equis, plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x + ▲ (equis, plus, triangle) 1989\r\n' )
    elif data.find (username + ' triangle, plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ + ▲ (triangle, plus, triangle) 1990\r\n' )
    elif data.find (username + ' equis, plus, equis' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x + x (equis, plus, equis) 1991\r\n' )
    elif data.find (username + ' square, plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ + ▲ (square, plus, triangle) 1992\r\n' )
    elif data.find (username + ' plus, triangle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + ▲ ▲ (plus, triangle, triangle) 1993\r\n' )
    elif data.find (username + ' plus, circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + • ▲ (plus, circle, triangle) 1994\r\n' )
    elif data.find (username + ' plus, square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + ■ ▲ (plus, square, triangle) 1995\r\n' )
    elif data.find (username + ' equis, circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x • ▲ (equis, circle, triangle) 1996\r\n' )
    elif data.find (username + ' equis, square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x ■ ▲ (equis, square, triangle) 1997\r\n' )
    elif data.find (username + ' equis, triangle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x ▲ ▲ (equis, triangle, triangle) 1998\r\n' )
    elif data.find (username + ' circle, equis, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • x ▲ (circle, equis, triangle) 1999\r\n' )
    elif data.find (username + ' square, square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ■ ▲ (square, square, triangle) 2000\r\n' )
    elif data.find (username + ' square, square, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ■ • (square, square, circle) 2001\r\n' )
    elif data.find (username + ' triangle, triangle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ▲ • (triangle, triangle, circle) 2002\r\n' )
    elif data.find (username + ' circle, triangle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ▲ • (circle, triangle, circle) 2003\r\n' )
    elif data.find (username + ' triangle, square, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ■ • (triangle, square, circle) 2004\r\n' )
    elif data.find (username + ' square, circle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ • • (square, circle, circle) 2005\r\n' )
    elif data.find (username + ' triangle, circle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ • • (triangle, circle, circle) 2006\r\n' )
    elif data.find (username + ' square, triangle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code:  ■ ▲ • (square, triangle, circle) 2007\r\n' )
    elif data.find (username + ' circle, circle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • • • (circle, circle, circle) 1928 1948\r\n' )
    elif data.find (username + ' plus, plus, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + + • (plus, plus, circle) 2008\r\n' )
    elif data.find (username + ' equis, plus, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: x + • (equis, plus, circle) 2009\r\n' )
    elif data.find (username + ' triangle, plus, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ + • (triangle, plus, circle) 2010\r\n' )
    elif data.find (username + ' circle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • • (circle, circle) 1919 1939 1959 1979\r\n' )
    elif data.find (username + ' square, square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ■ (square, square) 1920 1940 1960 1980\r\n' )
    elif data.find (username + ' triangle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ▲ (triangle, triangle) 1921 1941 1961 1981\r\n' )
    elif data.find (username + ' circle, square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ■ (circle, square) 1922 1942 1962\r\n' )
    elif data.find (username + ' circle, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ▲ (circle, triangle) 1923 1943 1963 \r\n' )
    elif data.find (username + ' triangle, square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ■ (triangle, square) 1924 1944 1964\r\n' )
    elif data.find (username + ' square, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ • (square, circle) 1925 1945 1965\r\n' )
    elif data.find (username + ' triangle, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ • (triangle, circle) 1926 1946 1966\r\n' )
    elif data.find (username + ' square, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ▲ (square, triangle) 1927 1947 1967\r\n' )
    elif data.find (username + ' plus, plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ++ (plus, plus) 1968\r\n' )
    elif data.find (username + ' triangle, plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ + (triangle, plus) 1930 1950 1970\r\n' )
    elif data.find (username + ' circle, plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • + (circle, plus) 1931* 1951 1971\r\n' )
    elif data.find (username + ' square, plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ + (square, plus) 1932 1952 1972\r\n' )
    elif data.find (username + ' plus, triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + ▲ (plus, triangle) 1933 1953 1973\r\n' )
    elif data.find (username + ' plus, circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + • (plus, circle) 1934 1954 1974\r\n' )
    elif data.find (username + ' plus, square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + ■ (plus, square) 1935 1955 1975\r\n' )
    elif data.find (username + ' circle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • (circle) 1916 1936 1956 1976\r\n' )
    elif data.find (username + ' square' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ (square)\r\n' )
      irc.send ( 'PRIVMSG ' + channel + ' :Years of manufacture: 1917, 1937, 1957, 1977\r\n' )
    elif data.find (username + ' triangle' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ (triangle) 1918 1938 1958 1978\r\n' )
    elif data.find (username + ' plus' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: + (plus) 1929 1949 1969\r\n' )
    elif data.find (username + ' What is the edge code for the year 1916' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • (circle) 1916\r\n' )
    elif data.find (username + ' What is the edge code for the year 1917' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ (square) 1917\r\n' )
    elif data.find (username + ' What is the edge code for the year 1918' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ (triangle) 1918\r\n' )
    elif data.find (username + ' What is the edge code for the year 1919' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • • (circle, circle) 1919\r\n' )
    elif data.find (username + ' What is the edge code for the year 1920' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ■ ■ (square, square) 1920\r\n' )
    elif data.find (username + ' What is the edge code for the year 1921' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ▲ (triangle, triangle) 1921\r\n' )
    elif data.find (username + ' What is the edge code for the year 1922' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ■ (circle, square) 1922\r\n' )
    elif data.find (username + ' What is the edge code for the year 1923' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: • ▲ (circle, triangle) 1923\r\n' )
    elif data.find (username + ' What is the edge code for the year 1924' ) != -1:
      irc.send ( 'PRIVMSG ' + channel + ' :Kodak edge code: ▲ ■ (triangle, square) 1924\r\n' )
    
  find_edge()
  print data
