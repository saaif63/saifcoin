import sys
from os import system as os
from threading import Thread as th
from time import sleep as sl
try:
	import rainbowtext
except:
	os('pip install rainbowtext')
try:
	import pyfiglet
except:
	os('pip install pyfiglet')

try:
	import samino
except:
	os('pip install samino==1.5.3')
	os('clear')
try:
	from colorama import Fore
except:
	os('pip install colorama')
	os('clear')
So=Fore.YELLOW
print(rainbowtext.text(pyfiglet.figlet_format('Saif')))
def lol(text):
	for type in text:
		sys.stdout.write(type)
		sys.stdout.flush()
		sl(0.040)
lol(So+'!-------------------------------------!\npy saif\nAmino: http://aminoapps.com/u/saif_alhkr\n!-------------------------------------!\n\n\n')
c=samino.Client('220B50483BB71470AE607E8A0AD2834BC286F0E1AF76CF1FEAEB74BBA38CF28ED18D58EB6A0E867FF6')
sid='AnsiMSI6IG51bGwsICIwIjogMiwgIjMiOiAwLCAiMiI6ICJjYWYzMWFmYi1iNTc2LTQ4MjItODY4Zi03NWRiZjM3YWM1MTkiLCAiNSI6IDE2MzI0OTY2MjIsICI0IjogIjM3LjIzOS4xNDEuNyIsICI2IjogMTAwfcvGSZbubnaMJNUL0SPl77OfCiyX'
linko='http://aminoapps.com/p/uquks8'
c.sid_login(sid)
chatt=c.get_from_link(linko).objectId
comId=c.get_from_link(linko).comId
local=samino.Local(comId)
local.send_message(chatt,'تم تفعيل البوت')
@c.event("on_message")
def on_message(data: samino.lib.Event):
	content=data.message.content
	comId=data.ndcId
	msgId=data.message.messageId
	chatId=data.message.chatId
	msg=data.message.content
	if msg.startswith('!daily'):
		local.send_message(chatt,'بدأ ارسال القروش',replyTo=msgId)
		useerri=data.message.userId
		for _ in range(200):
			th(target=c.watch_ad,args=(useerri, )).start()
c.launch()