import csv
file=file=open("TitanicSurvival.csv","r")
data = list(csv.reader(file,delimiter=","))
file.close()

changer=data[-1]
changer[4]='1st'
changer.append('Good Person')
print(data)