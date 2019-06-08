import requests
import pprint
import 	json
import os 
import pathlib
url= "https://www.giveindia.org/certified-indian-ngos"
url1=requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(url1.text,"html.parser")
main_data=soup.find("div",class_="container")
table_data=main_data.find("table",class_="jsx-697282504 certified-ngo-table")

tr=table_data.find_all("tr",class_="jsx-697282504")
td=table_data.find_all("td",class_="jsx-697282504 nonprofit-name-desktop")
def NGO_full_list(): 
    list1=[]
    list2=[]
    list3=[]
    for i in td:
        dic={}
        Name_list=i.find("div",class_="col")
        Name_list_data=Name_list.get_text()
        list1.append(Name_list_data)
    dic["name"]=list1
    cause_list=table_data.find_all("td",class_="jsx-697282504")
    a=len(cause_list)
    for j in range(1,a,3):
        m=cause_list[j]
        #print m
        dic1={}
        d=m.get_text()
        list2.append(d)
    dic["cause"]=list2
    for z in range(2,a,3): 
        m1=cause_list[z]
        dic2={}
        d1=m1.get_text()
        
        list3.append(d1)
    dic["city"]=list3
    return dic
dic_list=NGO_full_list() 
def arrage_name(data):
    dic1={}
    new_city_list=[]
    Name_list=data["name"]
    City_list=data["city"]
    
    for i in City_list:
        
        if i not in new_city_list:
            new_city_list.append(i)
    for j in new_city_list:
        name1=[]
        z=0
        for k in City_list:
            if j  in  k:
                m=Name_list[z]
                name1.append(m) 
            z=z+1
        dic1[j]=name1
    pprint.pprint (dic1)               
arrage_name(dic_list)    

