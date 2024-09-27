import requests 
from requests.auth import HTTPBasicAuth
import json
import JsonFactory

import yaml

# Read configuration from YAML.
with open('./yaml/jira_access.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Replace these variables with your Jira information.
jira_base_url = config['jira_base_url']
jira_filter = config['jira_filter']
max_results = config['max_results']
username = config['username']
api_token = config['api_token']

# Path to generated File.
path_to_json_file = config['path_to_json_file']

# Combine the URL and endpoint
url = jira_base_url + jira_filter + str(max_results)

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
