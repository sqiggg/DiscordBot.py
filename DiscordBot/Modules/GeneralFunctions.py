import json
import urllib2
file = 'db.json'
url = 'http://localhost:8080/json'

def store(json_data):
    #simplely storing json data to db.json
    with open(file, "w") as json_file:
        json_file.seek(0)
        json_file.truncate()
        json.dump(json_data, json_file, indent=4)

def retrieveUrl():
    #requesting the Json from the url that has been inputed
    try:
        response = urllib2.urlopen(url)
        text = response.read()
        text = json.loads(text)
        store(text)
    except EnvironmentError:
        #error message
        print "Something was wrong with the URL"

    return retrieve()

def sendJson(values):
    #setting the json
    urlArgs = {
        "payload":{
            "jsonTxt":{},
            "edit":""
        }
    }
    #converting the json text into a payload suitable to send to the backend
    urlArgs['payload']['jsonTxt'] = json.loads(json.dumps(values))
    urlArgs['payload']['edit'] = 'override'

    #establishing connection
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    try:
        #sending the data to the json backend
        response = urllib2.urlopen(req, json.dumps(urlArgs))
        print "sent json"
        return True
    except EnvironmentError:
        return False

def retrieve():
    #simple read from file and converting to json text
    with open(file, "r+") as json_file:
        json_data = json_file.read()
        json_data = json.loads(json_data)
        return json_data
