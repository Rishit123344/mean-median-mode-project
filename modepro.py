import csv 
from collections import Counter
with open("HeightWeight.csv",newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    num = filedata[i][2]
    newdata.append(float(num))
n = len(newdata)
data = Counter(newdata)
getmode = dict(data)
mode=[]
mode1=[]
mode2=[]
for a,v in getmode.items():
    a = float(a)
    if 50<a<60 :
        if v == max(list(data.values())):
            mode.append(a)
    elif 60<a<70:
        if v == max(list(data.values())):
            mode1.append(a)
    elif 70<a<75:
        if v == max(list(data.values())):
            mode2.append(a)
if len(mode)>len(mode1)and len(mode2):
    print(mode)
elif len(mode1)>len(mode)and len(mode2):
    print(mode1)
elif len(mode2)>len(mode)and len(mode1):
    print(mode2)


