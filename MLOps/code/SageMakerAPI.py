import boto3

# Create a low-level client representing Amazon SageMaker Runtime
sagemaker_runtime = boto3.client("sagemaker-runtime", region_name='ap-south-1')

# The endpoint name
endpoint_name = 'canvas-heart-attack-prediction-model-deployment'

# Specify the content type of the input data
content_type = 'application/json'

# Gets inference from the model hosted at the specified endpoint:
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType=content_type,
    Body=bytes('{"features": [52,0,76,109,85,227.0,0.665,0.491]}', 'utf-8')
)

# Decodes and prints the response body:
print(response['Body'].read().decode('utf-8'))

# Gets inference from the model hosted at the specified endpoint:
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=endpoint_name, 
    ContentType=content_type,
    Body=bytes('{"features": [63,0,66,160,83,160.0,1.8,0.012]}', 'utf-8')
)

# Decodes and prints the response body:
print(response['Body'].read().decode('utf-8'))

# Output = 