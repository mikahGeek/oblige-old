import os
import sys
import json
import boto3
import uuid

client = boto3.client(
  'dynamodb', aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'), region_name = os.getenv('AWS_REGION')
)

dynamodb = boto3.resource(
  'dynamodb', aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'), region_name = os.getenv('AWS_REGION')
)

def log_connect_request(source, dest):
  id = str(uuid.uuid4());
  dynamodb.Table('oblige-connect-request').put_item(Item = {'uuid': id, 'source': source, 'dest': dest});
  return id;

def get_connected(source, dest):
  return dynamodb.Table('oblige-connections').get_item(Key = { "source": source, "dest": dest });

# def log_response(response, requestid):
#   dynamodb.Table('oblige_speak_request').update_item(Key = {'uuid': requestid}, UpdateExpression = "set response_text = :r", ExpressionAttributeValues={':r': response})
