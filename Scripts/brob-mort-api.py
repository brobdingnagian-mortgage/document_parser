## This script is a quick example of how to use the Brobdingnagian Mortgage API to query customer loan data

import requests
import json

customer_data = requests.get('https://brobdingnagian-mortgage.com/api/v1/{APIKEY}/loans/all')
customer_json = json.loads(customer_data.content)
print(json.dumps(customer_json, indent=2))
