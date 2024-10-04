import requests

PREFECT_API_KEY = "pnu_4t3M9YNXs6TytZ5PNmzIM2gcicvXQL16BZBG"
ACCOUNT_ID = "447374eb-6251-4bfb-b0c7-18f7c4be91d0"
WORKSPACE_ID = "e15c14f8-cea0-41dc-bd42-d4b2899de804"

# Correct API URL to list flow runs
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/artifacts/filter"

# Data to filter artifacts
data = {
    "sort": "CREATED_DESC",
    "limit": 5,
    "artifacts": {
        "key": {
            "exists_": True
        }
    }
}

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request
response = requests.post(PREFECT_API_URL, headers=headers, json=data)
print(response)

# Check the response status
if response.status_code != 200:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
else:
    artifacts = response.json()
    print(artifacts)
    for artifact in artifacts:
        print(artifact)