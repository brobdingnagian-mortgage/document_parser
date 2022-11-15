## This script is a quick example of how to use the Brobdingnagian Mortgage API to query customer loan data

import requests
import json

customer_data = requests.get('https://brobdingnagian-mortgage.com/api/v1/728a950c5c3ac65df139e59b9df5bd27/loans/all')
customer_json = json.loads(customer_data.content)
print(json.dumps(customer_json, indent=2))