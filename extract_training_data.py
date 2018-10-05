import tweepy #You need to install tweepy#
import re
import time
import csv

###twitter
auth = tweepy.OAuthHandler([YOUR TWITTER API KEY], [YOUR TWITTER API KEY])
auth.set_access_token([YOUR TWITTER API KEY], [YOUR TWITTER API KEY])
api = tweepy.API(auth)
###
status=[]
no_status=[]
def DB():
	new_status=[]
	txt=[]
	text_=api.search(q='#bitcoin',lang='en',show_user='True')
	id_=re.findall("'id_str': '(.+?)'",str(text_))
	y=1
	for i in id_:
		try:
			text_=api.get_status(i,tweet_mode='extended')
			if i not in status:
				status.append(str(i))
				new_status.append(i)
				text=re.findall("'full_text': '(.+?)'",str(text_))
				#print (y)
				try:
					texto=str(text[0])
					texto=texto.replace('"','')
					#print (text[0])
					txt.append(texto)
				except Exception as e:
					#print (e)
					#print('void')	
					txt.append('VOID')
				y+=1
		except Exception as e:
			#print (e)
			if 'Rate limit exceeded' in str(e):
				print ('Rate limit exceeded')
			if i not in no_status:
				no_status.append(i)
	x=0
	with open('status_raw.db','a') as csvfile:
			fieldnames = ['ID','TEXT']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			for i in new_status:
				writer.writerow({'ID':str(i),'TEXT':txt[x]})
				x+=1
	
Z=1
while True:
	print ('ROUND:',Z)
	DB()	
	print ('LEN STATUS:',len(status))	
	print ('LEN NO STATUS:',len(no_status))
	print('___________________')
	time.sleep(900)#15 minutes wait, not to overload the twitter API
	Z+=1
