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
modedatarange = {
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurance in data.items():
    if 50<float(height)<60:
        modedatarange['50-60']+= occurance
    elif 60<float(height)<70:
        modedatarange['60-70']+= occurance
    elif 70<float(height)<80:    
        modedatarange['70-80']+= occurance
moderange,modeoccurance = 0,0
for range,occurance in modedatarange.items():
    if occurance>modeoccurance :
        moderange,modeoccurance = [int(range.split('-')[0]),int(range.split('-')[1])],occurance
mode= float((moderange[0]+moderange[1])/2)            
print(mode)                 