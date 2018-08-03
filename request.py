import requests
import json
import datetime

start = datetime.datetime.now()

def add_employee(id_value,first_name,last_name):
    url = "http://35.231.235.193:5000/insert"
    payload = {'id':id_value,'first_name':first_name,'last_name':last_name}
    headers = {'content-type':"application/json"}
    try:
       r = requests.post(url,data=json.dumps(payload),headers=headers)
    except :
       print("exception in connecting to the server")
    print(r)
    print("%s" %r.json()['row'] + " rows added to table")


def update_employee(id_value,key,value):
    url = "http://35.231.235.193:5000/update"
    payload = {'id':id_value,'key':key,'value':value}
    headers = {'content-type':"application/json"}
    try:
       r = requests.post(url,data=json.dumps(payload),headers=headers)
    except :
       print("exception in connecting to the server")
    print(r)
    print("%s" %r.json()['row'] + " rows updated to table")


def delete_employee(id_value):
    url = "http://35.231.235.193:5000/delete"
    payload = {'id':id_value}
    headers = {'content-type':"application/json"}
    try:
       r = requests.post(url,data=json.dumps(payload),headers=headers)
    except :
       print("exception in connecting to the server")
    print(r)
    print("%s" %r.json()['row'] + " rows deleted")


def query_employee():
    url = "http://35.231.235.193:5000/query"
    #payload = {'id':id_value}
    headers = {'content-type':"application/json"}
    try:
       r = requests.get(url,headers=headers)
    except :
       print("exception in connecting to the server")
    print(r)
    print("%s" %r.json()['row'] + " records fetched")

#delete_employee(1)
#delete_employee(2)
#delete_employee(3)
#delete_employee(4)
add_employee(1,'jitu','kr')
#add_employee(2,'rahul','kr')
#add_employee(3,'Rohit','kr')
#add_employee(4,'Abhishek','kr')
#update_employee(2,'first_name','sunit')
query_employee()

end = datetime.datetime.now()

print("time taken:%s"%(end-start))
