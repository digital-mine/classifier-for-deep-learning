import csv

txt=[]
with open('status_clean.db') as csvfile:
	reader=csv.DictReader(csvfile)
	for row in reader:	
		t=str(str(row['TEXT']))
		txt.append(t)

label=[]
for i in txt:
	print(i)
	quest=input('Is this OK?')
	result=i,quest
	label.append(result)

with open('status_classifier.db','a') as csvfile: #CREATE THE FILE "status_classifier.db' IN ADVANCE
	fieldnames = ['TEXT','LABEL']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	for i in label:
		writer.writerow({'TEXT':i[0],'LABEL':i[1]})
