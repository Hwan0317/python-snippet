import re
import json
import boto3

region = "ap-northeast-2"
instance_dict = {
    "instance-group": ['YOUR-INSTANCE-ID']
}
ec2 = boto3.client('ec2', region_name=region)

def instance_stop(server_group):
    ec2.stop_instances(InstanceIds=instance_dict[server_group])
    return 'stopped your instances: ' + server_group


def instance_start(server_group):
    ec2.start_instances(InstanceIds=instance_dict[server_group])
    return 'stopped your instances: ' + server_group

def instance_status(server_group):
    response = ec2.describe_instance_status(InstanceIds=instance_dict[server_group])
    return response['InstanceStatuses']

def instance_addr(server_group):
    response = ec2.describe_instances(InstanceIds=instance_dict[server_group])
    
    reservations = response['Reservations']
    if not reservations:
        return None
    
    instances = reservations[0]['Instances']
    if not instances:
        return None
    
    public_ip = instances[0].get('PublicIpAddress')
    return public_ip
