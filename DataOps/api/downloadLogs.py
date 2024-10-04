import requests

PREFECT_API_KEY="pnu_4t3M9YNXs6TytZ5PNmzIM2gcicvXQL16BZBG"
ACCOUNT_ID="447374eb-6251-4bfb-b0c7-18f7c4be91d0"
WORKSPACE_ID="e15c14f8-cea0-41dc-bd42-d4b2899de804"
FLOW_RUN_ID="701b7c9f-e6ca-4ffa-a3aa-1290359606d2"


# Correct API URL to get flow details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/flow_runs/{FLOW_RUN_ID}/logs/download"

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    with open('/tmp/response_data.txt', 'wb') as file:
        file.write(response.content)
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")