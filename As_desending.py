#"http://join.navgurukul.org/api/partners"
import requests
import json

saral_link="http://join.navgurukul.org/api/partners"
# saral link me jo data hai usko get karana hai
saral_get=requests.get(saral_link)
#get method se wo html form me aaya hai but muzhe string form mehiye
saral_get1=saral_get.json()
with open("navgurukul.json","w") as f:
    json.dump(saral_get1,f,indent=4)


list1=[]
list2=[]
serial=0
for i in saral_get1["data"]:
    name=saral_get1["data"]
    id=saral_get1["data"]
    print(serial+1,(" "),i["name"],(" "),("id:-"),i["id"])
    list1.append(i["name"])
    list2.append(i["id"])
    serial+=1

y={}
for i in range(len(list1)):
    for k in range(len(list2)):
        y[list1[i]]=(list2[i])

print(" ")
user_input =input("Do you Want to__ Asending/Desending(a/d):-")

if user_input=="a" or user_input=="asending":
    Asending=[]
    for x in y:
        a=y[x]
        Asending.append(x)
        Asending.append(a)

    n=1
    while n<len(Asending):
        j=n+2
        while j<len(Asending):
            if Asending[n]>Asending[j]:
                c=Asending[n]
                Asending[n]=Asending[j]
                Asending[j]=c
                x=a
            j+=2
        n+=2
    i=0
    m=1
    while i<len(Asending):
        print(m," ",Asending[i],Asending[i+1])
        m+=1
        i+=2
# for desending:
elif user_input=="d" or user_input=="desending":
    # list4=[]
    list1=[]

    for i in range(len(y)):
        max = 0
        for x in y:
            if max<y[x]:
                key=x
                max=y[x]
        list1.append(key)
        list1.append(max)
        y.pop(key)
    i=0
    s=1
    while i<len(list1):
        print(s,list1[i],list1[i+1])
        s+=1
        i+=2 
    Desending=[]
    for x in y:
        a=y[x]
        Desending.append(x)
        Desending.append(a)

    n=1
    while n<len(Desending):
        j=n+2
        while j<len(Desending):
            if Desending[n]>Desending[j]:
                c=Desending[n]
                Desending[n]=Desending[j]
                Desending[j]=c
                x=a
            j+=2
        n+=2
    i=0
    m=1
    while i<len(Desending):
        print(m," ",Desending[i],Desending[i+1])
        m+=1
        i+=2

   






# if user_input=="a" or user_input=="Asending":
#     Asending=[]

#     for m in d:
#         a=d[m]
#         Asending.append(m)
#         Asending.append(a)
    # n=1
    # while n<len(Asending):
    #     j=n+2
    #     while j<len(Asending):
    #         if Asending[n]>Asending[j]:
    #             c=Asending[n]
    #             Asending[n]=Asending[j]
    #             Asending[j]=c
    #             i2=a
    #         j+=2
    #     n+=2
    # i=0
    # m=1
    # while i<len(Asending):
    #     print(m," ",Asending[i],Asending[i+1])
    #     m+=1
    #     i+=2

# elif user_input=="d" or user_input=="Desending":
#     Desending=[]
# for i in range(len(d)):
#     max=0
#     for m in d:
#         if max < d[m]:
#             key=m
#             max=d[m]
#         Desending.append(key)
#         Desending.append(max)
#         d.pop(key)
#     n=1
#     s=1
#     while n<len(Desending):
#         print(s,Desending[i],Desending[i+1])
#          s+=1
    #     n+=2
    #     list1=[]
    #     for x in d:
    #         a=d[x]
    #         list1.append(x)
    #         list1.append(a)
    # n=1
    # while n<len(list1):
    #     j=n+2   
    #     while j<len(list1):
    #         if list1[n]>list1[j]:
    #             c=list1[n]
    #             list1[n]=list1[j]
    #             list1[j]=c
    #             x=a
    #         j+=2
    #     n+=2
    # i=0
    # m=1
    # while i<len(list1):
    #     print(m," ",list1[i],list1[i+1])
    #     m+=1
    #     i+=2

# y={}
# for i in range(len(list1)):
#     for k in range(len(list2)):
#         y[list1[i]]=(list2[i])

# print(" ")
# # topic=input("enter a way you want asending/desending or a/d:")

# # for asending




# # for asending

# if topic=="a" or topic=="asending":
#     list3=[]
#     for x in y:
#         a=y[x]
#         list3.append(x)
#         list3.append(a)

#     n=1
#     while n<len(list3):
#         j=n+2
#         while j<len(list3):
#             if list3[n]>list3[j]:
#                 c=list3[n]
#                 list3[n]=list3[j]
#                 list3[j]=c
#                 x=a
#             j+=2
#         n+=2
#     i=0
#     m=1
#     while i<len(list3):
#         print(m," ",list3[i],list3[i+1])
#         m+=1
#         i+=2
# # for desending

# elif topic=="d" or topic=="desending":
#     # list4=[]
#     list5=[]

#     for i in range(len(y)):
#         max = 0
#         for x in y:
#             if max<y[x]:
#                 key=x
#                 max=y[x]
#         list5.append(key)
#         list5.append(max)
#         y.pop(key)
#     i=0
#     s=1
#     while i<len(list5):
#         print(s,list5[i],list5[i+1])
#         s+=1
#         i+=2 
#     list3=[]
#     for x in y:
#         a=y[x]
#         list3.append(x)
#         list3.append(a)

#     n=1
#     while n<len(list3):
#         j=n+2
#         while j<len(list3):
#             if list3[n]>list3[j]:
#                 c=list3[n]
#                 list3[n]=list3[j]
#                 list3[j]=c
#                 x=a
#             j+=2
#         n+=2
#     i=0
#     m=1
#     while i<len(list3):
#         print(m," ",list3[i],list3[i+1])
#         m+=1
#         i+=2

   