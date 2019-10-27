import pymongo
import json
import argparse
import os
import html

from datetime import datetime

parser = argparse.ArgumentParser(description='Processes out messages into individual files.')
parser.add_argument('--list', action="store", dest="mailing_list", type=str)
parser.add_argument('--output', action="store", dest="output", type=str)
args = parser.parse_args()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[args.mailing_list]
mycol = mydb["messages"]

mydocs = mycol.find({})

print("Starting " + args.mailing_list)

for doc in mydocs:
    if not 'postDate' in doc:
        continue

    path  = os.path.realpath(os.path.expanduser(args.output)) + "/"
    path += args.mailing_list + "/" + datetime.utcfromtimestamp(doc["postDate"]).strftime('%Y')
    os.makedirs(path, exist_ok=True)

    filename  = path + datetime.utcfromtimestamp(doc["postDate"]).strftime('/%m-%d-')
    filename += str(doc["_id"]) + "-"
    filename += doc["from"]
    
    print(filename + ".json")
    f = open(filename + ".json", "w")
    f.write(json.dumps(doc, indent=4, separators=(',', ': ')))
    f.close()

    print(filename + ".txt")
    f = open(filename + ".txt", "w")
    f.write(html.unescape(doc["rawEmail"]))
    f.close()
