# SQS = Simple Queue Service

#Boto3 is the name of the Python SDK (Software development kit) for AWS
import boto3

#Service resource
sqs = boto3.resource("sqs")

#Queue creation

queue = sqs.create_queue(QueueName = "ProjWK16")

#Prints out identifier(s)
print(queue.url)