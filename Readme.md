# Lambda Function for Creating Manifest Files in S3

This AWS Lambda function lists objects in an S3 bucket, filters them by specific table names, and creates manifest files for each table. The manifest files are then uploaded back to S3.

## Table of Contents

- [Overview](#overview)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Function Details](#function-details)
- [Error Handling](#error-handling)
- [Deployment](#deployment)
- [Usage](#usage)

## Overview

This Lambda function performs the following tasks:

1. Lists objects in a specified S3 bucket.
2. Filters the objects based on predefined table names.
3. Creates a manifest file for each table containing the URLs and metadata of the objects.
4. Uploads the manifest files to the same S3 bucket.

## Environment Variables

- `AWS_REGION`: The AWS region where resources are deployed.

## Dependencies

The Lambda function requires the `boto3` library, which is included in the AWS Lambda runtime environment. Ensure your Lambda function has the appropriate IAM permissions to access and manage S3 objects.

## Function Details

### `list_objects_in_bucket(bucket_name)`

Lists all objects in the specified S3 bucket and collects their metadata.

#### Parameters

- `bucket_name`: The name of the S3 bucket.

#### Returns

A list of objects with their metadata.

### `create_manifest_file(bucket_name, table_name, objects)`

Creates a manifest file for the specified table and uploads it to the S3 bucket.

#### Parameters

- `bucket_name`: The name of the S3 bucket.
- `table_name`: The name of the table (used in the manifest file name).
- `objects`: The list of S3 objects to include in the manifest file.

### `lambda_handler(event, context)`

The main entry point for the Lambda function. It processes the S3 bucket and creates manifest files for each table.

#### Parameters

- `event`: The event data that triggers the Lambda function.
- `context`: The runtime information of the Lambda function.

#### Returns

A JSON response with a status code and message.

## Error Handling

The function does not include explicit error handling. Ensure that the necessary IAM permissions are correctly configured for the Lambda function to access and manage S3 objects.

## Deployment

1. Create an IAM role with the necessary permissions for S3.
2. Create a Lambda function with this code and attach the IAM role.
3. Set up the environment variables if needed.
4. Configure the Lambda trigger (e.g., S3 event notification, scheduled event).

## Usage

To use this Lambda function, ensure that it is triggered appropriately (e.g., on a schedule or by S3 events). The function will process the S3 bucket, create manifest files for the specified tables, and upload the manifest files back to the same S3 bucket.
