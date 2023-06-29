'''
Wrapper class for AWS actions
'''
import json
import os
import sys
import boto3
from utility import Utility
from DTO.AutoScalingResponseDTO import AutoScalingResponseParser
from DTO.DescribeInstanceDTO import DescribeInstanceResponseParser
from DTO.ScheduledActionsResponseDTO import ScheduledActionsResponseParser
utility = Utility()
asgdto = AutoScalingResponseParser()
instdto= DescribeInstanceResponseParser()
sardto = ScheduledActionsResponseParser()

class AWS_Wrappers:

    def get_aws_client(self,service_ofering):
        '''

        :param service_ofering: service offering eg: ec2, asg
        :return: AWS BOTO3 Client object
        '''
        try:
            aws_access_key_id = os.environ['TestAccessKey']
            aws_secret_access_key = os.environ['TestSecretKey']
            if aws_access_key_id != None and aws_access_key_id !="" and aws_secret_access_key !=None and aws_secret_access_key!= "":
                if service_ofering.lower()=="ec2":
                    return boto3.client('ec2',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name='ap-south-1')
                elif service_ofering.lower()=="asg":
                    return boto3.client('autoscaling', aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key, region_name='ap-south-1')
                else:
                    raise Exception("Service offering is not valid")
            else:
                sys.exit("ERROR: Access Key or Secret Key is not valid. Check environment variables")
        except Exception as e:
            sys.exit("ERROR in Getting AWS client : " + str(e))

    def describe_asg(self,asgname):
        '''

        :param asgname: Auto scaling Group Name
        :return: Serialised class of the Describe Auto Scaling Response
        '''
        describe_response = json.dumps(self.get_aws_client('asg').describe_auto_scaling_groups(AutoScalingGroupNames=[asgname]),sort_keys=True, default=str)
        return asgdto.autoScalingResponseParsed(json.loads(describe_response))


    def describe_instance(self,instanceIds):
        '''

        :param instanceIds: List of Instance IDs
        :return:Serialised class of the Describe Instance Response
        '''
        response = json.dumps(self.get_aws_client("ec2").describe_instances(
            InstanceIds=instanceIds,
        ),sort_keys=True,default=str)
        return instdto.describeInstanceResponseParsed(json.loads(response))


    def get_status_of_instances(self,instanceId):
        '''

        :param instanceId: list of ec2 Instance IDs
        :return: State of the Instance eg: Stpped, Running etc
        '''
        describeInstances= self.describe_instance(instanceId)
        return describeInstances.reservations[0].instances[0].state.name

    def get_running_instances_asg_details(self,asgname):
        '''

        :param asgname: Auto scaling group name
        :return: Returns the status of instances running on ASG
        '''
        describe_asg_response= self.describe_instance(asgname)
        count_intances_in_asg = len(describe_asg_response.auto_scaling_groups[0].instances)
        instance_status = {}
        for i in range(0, count_intances_in_asg):
            instance_id = describe_asg_response.auto_scaling_groups[0].instances[i].instance_id
            instance_status = self.describe_instance([instance_id]).reservations[0].instances[0].state.name
            if instance_status == "running":
                instance_status[instance_id]=self.describe_instance([instance_id])
        return instance_status


    def get_scheduled_actions(self,asgname):
        '''

        :param asgname:  Auto scaling Group Name
        :return:   Resturns serialised class of the describe scheduled action response
        '''
        scheduledActions_response= json.dumps(self.get_aws_client('asg').describe_scheduled_actions(AutoScalingGroupName= asgname),sort_keys=True,default=str)
        return sardto.describeScheduledActionsResponseParsed(json.loads(scheduledActions_response))


    def describe_scaling_activities(self,asgname):
        '''

        :param asgname: Auto scaling group Name
        :return: returns list of scaling activites in the ASG
        '''
        scaling_activities_all = []
        paginator = self.get_aws_client('asg').get_paginator('describe_scaling_activities')
        for page in paginator.paginate(AutoScalingGroupName=asgname):
            scaling_activities_all.append(page['Activities'])
        return scaling_activities_all
























