from difflib import SequenceMatcher
import numpy as np
import csv

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
txt=[]
with open('status_raw.db') as csvfile:
	reader=csv.DictReader(csvfile)
	for row in reader:	
		t=str(row['ID']),str(row['TEXT'])
		txt.append(t)

def clean():
	dop=[]
	y=1
	for i in txt:
		print (y)
		for x in txt:	
			if similar(i[1],x[1])>=0.549:
					print ('TEXT 1:',i[1])
					print ('TEXT 2:',x[1])
					if i[0]==x[0]:
						print ('CECK SAME')
					else:
						txt.remove(x)
						dop.append(x)
		y+=1
	return dop

d=clean()
if len(d)>0:
	d=clean()

with open('status_clean.db','a') as csvfile: #CREATE THE "status_clean.db" IN ADVANCE
	fieldnames = ['ID','TEXT']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	for i in txt:
		writer.writerow({'ID':str(i[0]),'TEXT':str(i[1])})
