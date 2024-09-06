import requests 
from requests.auth import HTTPBasicAuth
import json
import JsonFactory



# Read configuration from Json.
f = open('./json/conf.json')
conf = json.load(f)

# Replace these variables with your Jira information.
jira_url = conf['jira_url']
max_results = conf['max_results']
username = conf['username']
api_token = conf['api_token']

# Path to generated File.
path_to_json_file = conf['path_to_json_file']

# Combine the URL and endpoint
url = jira_url + max_results

# Send the request
response = requests.get(url, auth=HTTPBasicAuth(username, api_token))

# Check if the request was successful
if response.status_code == 200:
    print('Convert the response to JSON and print it')
    
    #print(response._content)
    jData = JsonFactory.convertRawdataToJson(response.content)
    JsonFactory.writeJsonFile(jData, path_to_json_file)

    #issue = response.json()
    #print(issue)
else:
    # 401-Autorisierung erforderlich
    print(f"Failed to get issue: {response.status_code}",response)

#print(issue['fields']['summary'])
print("Finished successfully!")
