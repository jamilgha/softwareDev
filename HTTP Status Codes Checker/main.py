#HTTP Status Codes Checker
import urllib3
import csv


def Status_Codes_Checker(add):
    index=[]
    http=urllib3.PoolManager()
    url=http.request('Get', add)
    with open("code.csv") as csvfile:
        cvsreader=csv.reader(csvfile)
        for row in cvsreader:
            index.append(row)
    code=str(url.status)
    col=[x[0] for x in index]
    if code in col:
        for x in range(0,len(index)):
            if code==index[x][0]:
                print(f"The {add} Https Status Codes: ",index[x])
    else:
        print("fuck")
Addresss=input("Pls Enter Url:")
Status_Codes_Checker(Addresss)