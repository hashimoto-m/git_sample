import csv

with open("a.csv") as f:
    #print(f.read())
    reader = csv.reader(f)
    l=[row for row in reader]
       
    print(l)
def  csv (subject_number):
    print(l[subject_number][1:])
    r=l[subject_number][1:]
    x=[int(v) for v in r]
    print(sum(x)/len(x))
csv(2)
    
    