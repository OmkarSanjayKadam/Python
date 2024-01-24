import requests
import time


start=time.strtime('%X')


for i in range(1,50):
    urls.append(f"put the urls here ")
    rawResults=requests.get(f"")
    results=rawResults.json()

    if "items" in results:
        for question in results("items"):
            if "user_id" in question["owner"] and "reputation" in question["owner"]:
                print(f"values i want are {question["owner"] ["user_id"]} [] {},{}")
        

print('program completed')
print(f"Started at "{start} and ended at {time.started('%X')}")
      






# Asynchrous code using threading:
      
import threading 
import time
 
def data_fetch(urls):
    for url in urls:
        rawResults = requests.get(url)
        results= rawresults.json()
        if "items" in results:
            for question in results["items"]:
                if "user_id" in question ["owner"] and ["reputation" in question]

def spilt_urls(urls,chunk_size):    
    split_urls= [urls[x:x+chunk_size] for x in range (0,len(urls),chunk_size)]
    return spilt_urls
 

 spilt_result=spilt_urls(urls,1())
 print(spilt_result)
  threadList = []
  for i inr range (len(spilt_result)):
    t = threading.Thread(target=data_fetch,args=(spilt_result[i],))
    t.start()
    threadList.append(t)

for each thread 



#to actiavte and create a virtual machine in python:
# py -m venv virutal1 (code to install virtual machine in python)
#cd.virtual1  (to get into the virtual machine)
#Install every necessary packages in the virtual machine needed to run the code
#pip list (to check the versions of packages in the virtual machine)
#pip freeze (code to see the list of the packages install ed on the virtual environment)
#pip freeze > requirements.txt  (always use it inside virtual code)








23rd Jan:



#await and asyncio

#.get is not a synchronous so cant use "await" with ".get" for that we need to change your package to "aiohttp" or "asyncio" which states asynchronos io
#future will help you to get a data out from a running task in the data
# with:(file should always be closed after opening it)

for i in range(0,1000):
    open("saompath")

execute some lines:  --open
pause:
some lines automatically: close

def my function():
    print("my fav function")
    yield 100
    print("automatically called")

with my_function() as value:
    print(value)
    print("inside the context")

print("outside the context")

with open() as xyz:    #xyz is the value of the file which have and with open() is open when we connect data base with your program and database has limited connection so you need to close the connection so we should use context i.e. open with()

#redis is for simple data and fast and not for large storing of adata
#structured and unsutrucred data 
#