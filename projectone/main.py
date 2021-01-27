import csv

webs = []
user = []
occur = []
ecode = []
reason = []
participant = []
evstart = []
evend = []
count = 0
flag = 0

with open('_event.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        webs.append(row[0])
        occur.append(row[1])
        ecode.append(row[2])
        reason.append(row[3])
        participant.append(row[4])
        count = count + 1
        print(count)
print (user)


for i in range(1, count):
    print(user[i]);
