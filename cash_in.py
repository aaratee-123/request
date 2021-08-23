import requests
import json
import os 

if os.path.isfile("saral.json"):
    with open("saral.json","r") as f:
         saral_get1=json.load(f)

        
else:
    saral_get=requests.get("http://saral.navgurukul.org/api/courses" )
    saral_get1=saral_get.json()
    with open("saral.json","w") as f:
        json.dump(saral_get1,f,indent=4)

serial_no=0
for courses in saral_get1["availableCourses"]:
    print(serial_no+1,":-",courses["name"],courses["id"])
    serial_no+=1
    print("")

user_input =int(input("Enter your courses number that you want to learn:- "))
parent_id=saral_get1["availableCourses"][user_input-1]["id"]
parent_name=saral_get1["availableCourses"][user_input-1]["name"]
print(saral_get1["availableCourses"][user_input-1]["name"])


if os.path.isfile("parent.json"):
    with open("parent.json","r") as f:
        parent_url1=json.load(f)

else:
    parent_data="http://saral.navgurukul.org/api/courses/"+str(parent_id)+"/exercises"
    parent_url=requests.get(parent_data)
    parent_url1=parent_url.json()

    with open("parent.json","w") as f:
        json.dump(parent_url1,f,indent=4)


no=0
for child in range(len( parent_url1["data"])):
    no+=1
    print("  ",no,parent_url1["data"][child]["name"])
user_1=int(input("enter the number"))
no_1=0
if parent_url1["data"][user_1-1]["childExercises"]!=[] :
    for i in range(len(parent_url1["data"][user_1-1]["childExercises"])):
        print(parent_url1["data"][user_1-1]["childExercises"][i]["name"])
    no_1+=1
else:
    print(parent_url1["data"][user_1-1]["slug"])


content=int(input("enter the number"))

url=(parent_url1["data"][user_1-1]["childExercises"][content-1]["id"])
url_1=(parent_url1["data"][user_1-1]["childExercises"][content-1]["slug"])

if os.path.isfile("topic.json"):
    with open("topic.json","r") as f:
        saral_data2=json.load(f)
else:
    saral_api_2=("http://saral.navgurukul.org/api/courses/"+str((parent_url1["data"][user_1-1]["childExercises"][content-1]["id"]))+"/exercise/getBySlug?slug="+(parent_url1["data"][user_1-1]["childExercises"][content-1]["slug"]))

    saral_data=requests.get(saral_api_2)

    saral_data2=saral_data.json()

    with open ("topic.json","w") as f:
        json.dump(saral_data2,f,indent=4)
print(saral_data2["content"])





