import requests
import json


def add_employee(id_value,first_name,last_name):
    url = "http://127.0.0.1:5000/insert"
    payload = {'id':id_value,'first_name':first_name,'last_name':last_name}
    headers = {'content-type':"application/json"}
    try:
       r = requests.post(url,data=json.dumps(payload),headers=headers)
    except :
       print("exception in connection")
    print(r)
    print("%s" %r.json()['row'] + " rows added to table")
    #print(type(r))
    #print(r.json())
    #print(r.text)
    #print(r.status_code)


def delete_employee(id_value):
    url = "http://127.0.0.1:5000/delete"
    payload = {'id':id_value}
    headers = {'content-type':"application/json"}
    try:
       r = requests.post(url,data=json.dumps(payload),headers=headers)
    except :
       print("exception in connection")
    print(r)
    print("%s" %r.json()['row'] + " rows deleted")

#delete_employee(1)
#delete_employee(2)
#delete_employee(3)
#delete_employee(4)
add_employee(1,'jitu','kr')
add_employee(2,'rahul','kr')
add_employee(3,'Rohit','kr')
add_employee(4,'Abhishek','kr')
