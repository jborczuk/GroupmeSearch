import requests
from .searchFunctions import linearSearch

def callAPI(token):
    #file containing all messages with names
    searchFile = open("searchFile.txt", "w")



    url = 'https://api.groupme.com/v3/groups/<GROUP-ID???>/messages?token=%s&limit=100' %token
    r = requests.get(url)

    resp = r.json()


    while r.status_code!=304:
        for messages in resp['response']['messages']:
            id = messages['id']
            text = "%s: %s" %(messages['name'],messages['text'])
            print(text)
            searchFile.write(text+"\n")


        url = 'https://api.groupme.com/v3/groups/???/messages?token=%s&before_id=%s&limit=100' %(token,id)
        r = requests.get(url)
        if r.status_code!=304:
            resp = r.json()

    searchFile.close()

    #currently manual input for testing
#searchString = "I'll"
#linearSearch(searchString)
	
	
