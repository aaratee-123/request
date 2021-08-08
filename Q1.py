import requests
import json

saral_link="http://saral.navgurukul.org/api/courses"
# saral link me jo data hai usko get karana hai
saral_get=requests.get(saral_link)
#get method se wo html form me aaya hai but muzhe string form mehiye
saral_get1=saral_get.json()
with open("meraki_courses.json","w") as f:
    json.dump(saral_get1,f,indent=4)

serial_no=0
for courses in saral_get1["availableCourses"]:
    print(serial_no+1,":-",courses["name"],courses["id"])
    serial_no+=1

user_input =int(input("Enter your courses number that you want to learn:- "))
parent_id=saral_get1["availableCourses"][user_input-1]["id"]
print(saral_get1["availableCourses"][user_input-1]["name"])

parent_data="http://saral.navgurukul.org/api/courses/"+str(parent_id)+"/exercises"
parent_url=requests.get(parent_data)
parent_url1=parent_url.json()

with open("data.json","w") as f:
    json.dump(parent_url1,f,indent=4)
no=0
for child in range(len(parent_url1["data"])):
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
    # print(url_1)
    
    
saral_api_2=("http://saral.navgurukul.org/api/courses/"+str((parent_url1["data"][user_1-1]["childExercises"][content-1]["id"]))+"/exercise/getBySlug?slug="+(parent_url1["data"][user_1-1]["childExercises"][content-1]["slug"]))

saral_data=requests.get(saral_api_2)

saral_data2=saral_data.json()

with open ("content.json","w") as f:
    json.dump(saral_data2,f,indent=4)
print(saral_data2["content"])

# else:
#     print(parent_url1["data"][user_1-1]["slug"])





