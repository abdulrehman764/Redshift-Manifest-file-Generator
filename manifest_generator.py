
import boto3
import json

def list_objects_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    objects = []

    # Paginate through objects in the bucket and collect their metadata
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name):
        for obj in page.get('Contents', []):
            objects.append(obj)

    return objects

def create_manifest_file(bucket_name, table_name, objects):
    manifest = {"entries": []}
    for obj in objects:
        url = f"s3://{bucket_name}/{obj['Key']}"
        content_length = obj['Size']
        entry = {"url": url, "mandatory": True, "meta": {"content_length": content_length}}
        manifest["entries"].append(entry)
    
    # Upload manifest file to S3
    s3 = boto3.client('s3')
    bucket_name = 'abdul-test-bucket-1'
    manifest_file_key = f'{table_name}_manifest.json'
    s3.put_object(Bucket=bucket_name, Key=manifest_file_key, Body=json.dumps(manifest))

def lambda_handler(event, context):
    bucket_name = 'your_bucket_name'
    bucket_name = 'customer-io-data'
    
    tables = ['attributes', 'deliveries', 'delivery_content', 'metrics', 'outputs', 'people', 'subjects']

    for table in tables:
        objects = list_objects_in_bucket(bucket_name)
        filtered_objects = [obj for obj in objects if table in obj['Key']]
        create_manifest_file(bucket_name, table, filtered_objects)
    
    return {
        'statusCode': 200,
        'body': 'Manifest files created for all tables.'
    }
