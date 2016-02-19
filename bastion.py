import os
import json

from pprint import pprint

menu = []
config=None
with open('config.json') as data_file:
    data = json.load(data_file)
    config = data["config"]
    for instance in data["servers"]:
        #print(instance["name"])
        #print(instance["ip"])
        #print(instance["port"])
        #print(instance["localport"])
        menu.append(instance)

for i in range(0, len(menu)):
    print i,"- ssh to "+menu[i]["name"]

id = input("your choice: ")

req = "ssh -f -N -L:"+menu[id]["localport"]+":"+menu[id]["ip"]+":"+menu[id]["port"]+" "+config["login"]+"@"+config["bastion"]
print req
os.system(req)
os.system("ssh -p +"+menu[id]["localport"]+" "+menu[id]["username"]+"@localhost")
