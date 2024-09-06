import requests 
from requests.auth import HTTPBasicAuth
import yaml

import JsonFactory


# Read configuration from Yaml.
with open('./yaml/jira_access.yaml', 'r') as file:
    prime_service = yaml.safe_load(file)

# Replace these variables with your Jira information.
jira_url = prime_service['jira_url']
max_results = prime_service['max_results']
username = prime_service['username']
api_token = prime_service['api_token']

# Path to generated File.
path_to_json_file = prime_service['path_to_json_file']

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
