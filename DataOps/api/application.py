import requests
from datetime import datetime, timedelta
import pytz


PREFECT_API_KEY="pnu_4t3M9YNXs6TytZ5PNmzIM2gcicvXQL16BZBG"
ACCOUNT_ID="447374eb-6251-4bfb-b0c7-18f7c4be91d0"
WORKSPACE_ID="e15c14f8-cea0-41dc-bd42-d4b2899de804"
DEPLOYMENT_ID="22e10c79-4d9b-4e0e-926c-f9979c089ea4"
FLOW_ID="10f32598-b16d-48da-8916-7537741c5a35"

headers = { "Authorization": f"Bearer {PREFECT_API_KEY}" }

PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}"

# endpoint URLs
DEPLOYMENT_ENDPOINT = f'{PREFECT_API_URL}/deployments/filter'
FLOW_ENDPOINT = f'{PREFECT_API_URL}/flows/filter'
FLOW_RUN_ENDPOINT = f'{PREFECT_API_URL}/flow_runs/filter'
TASK_RUN_ENDPOINT=f'{PREFECT_API_URL}/task_runs/filter'
WORK_QUEUES_ENDPOINT=f'{PREFECT_API_URL}/work_queues/filter'
SCHEDULES_ENDPOINT=f'{PREFECT_API_URL}/deployments/get_scheduled_flow_runs'
CONCURRENCY_LIMIT_ENDPOINT=f'{PREFECT_API_URL}/concurrency_limits/filter'

# Get deployments
deployments = requests.post(DEPLOYMENT_ENDPOINT, headers=headers)
deployments_json = deployments.json()

# Get flow details
flows = requests.post(FLOW_ENDPOINT, headers=headers)
flows_json = flows.json()

# Get flow run details
flow_runs = requests.post(FLOW_RUN_ENDPOINT, headers=headers)
flow_runs_json = flow_runs.json()
flow_runs_sorted_json = sorted(flow_runs_json, key=lambda x: x['start_time'] or '', reverse=True)

# Get task run details
task_runs = requests.post(TASK_RUN_ENDPOINT, headers=headers)
task_runs_json = task_runs.json()
task_runs_sorted_json = sorted(task_runs_json, key=lambda x: x['start_time'] or '', reverse=True)

# Get schedules
new_time = datetime.utcnow() + timedelta(minutes=8)
formatted_time = new_time.strftime('%Y-%m-%dT%H:%M:%SZ')
payload = {
    'deployment_ids': [ DEPLOYMENT_ID ],
    'scheduled_before': formatted_time
}
schedules = requests.post(SCHEDULES_ENDPOINT, headers=headers, json=payload)
schedules_json = schedules.json()
schedules_json_sorted = sorted(schedules_json, key=lambda x: x['created'] or '', reverse=True)

# concurrency limits
concurrency_limits = requests.post(CONCURRENCY_LIMIT_ENDPOINT, headers=headers)
concurrency_limits_json = concurrency_limits.json()


# Displaying application details
print("Deployments:")
for deployment in deployments_json:
    print(f"    ID: {deployment['id']}, Name: {deployment['name']}")
print("\n")

print("Flows:")
for flow in flows_json:
    print(f"    ID: {flow['id']}, Name: {flow['name']}")
print("\n")

print("Flow Runs:")
for flow_run in flow_runs_sorted_json[:3]:
    print(f"- ID: {flow_run['id']}, State: {flow_run['state']}")
print("\n")

print("Task Runs:")
for task_run in task_runs_sorted_json[:3]:
    #print(task_run)
    print(f"- ID: {task_run['id']}, Task Name: {task_run['name']}, State: {task_run['state']}")
print("\n")

print("Schedules:")
for schedule in schedules_json_sorted[:3]:
    utc_time = datetime.fromisoformat(schedule['expected_start_time'])
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_time = utc_time.astimezone(ist_timezone)
    print(f"    ID: {schedule['id']}, Name: {schedule['name']}, ScheduledAt: {ist_time}")
    #print(schedule)
print("\n")

print("Concurrency Limit:")
print(concurrency_limits_json)
print("\n")
