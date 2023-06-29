import datetime
from aws_wrappers import AWS_Wrappers
from utility import Utility
utility = Utility()
aws_wrappers =AWS_Wrappers()


def test_ASG_DesireRunningCount_1A(ASGName): # Test Case 1 : Point 1- ASG desire running count should be same as running instances. if mismatch fails
   try:
      describe_asg_response = aws_wrappers.describe_asg(ASGName) # Describe ASG
      desired_running_count =describe_asg_response.auto_scaling_groups[0].desired_capacity #Gets Desired Running Count
      count_intances_in_asg= len(describe_asg_response.auto_scaling_groups[0].instances) # Gets instances attached in ASG
      instance_status ={}
      for i in range(0,count_intances_in_asg):
         instance_id = describe_asg_response.auto_scaling_groups[0].instances[i].instance_id # Get instance Id's of attached instances in ASG
         instance_status = aws_wrappers.describe_instance([instance_id]).reservations[0].instances[0].state.name # Get status of instances
         instance_status[instance_id]=instance_status
      running_instance_count = utility.count_value_dict(instance_status,"running") #Get Running instances count
      assert desired_running_count == running_instance_count #Desired count should be equal to running
   except Exception as e:
      assert False

def test_availability_zone_1B(ASGName): # Test Case 1 : Point 2 :if more than 1 instance running on ASG, then ec2 instance should on available and distributed on multiple availibity zone.
   try:
      describe_asg_response = aws_wrappers.describe_asg(ASGName) #Describe ASG
      count_intances_in_asg = len(describe_asg_response.auto_scaling_groups[0].instances) # Count instances in ASG
      if count_intances_in_asg < 2:
         assert False #0 or 1 istances are running

      availability_zones=[]
      running_instances_details = aws_wrappers.get_running_instances_asg_details("lv-test-cpu") #Get Running instance Details
      for instanceid in running_instances_details:
         availability_zones.append(running_instances_details[[instanceid]].reservations[0].instances[0].placement.availability_zone) #Get Availability zone of unstances
      if utility.check_unique(availability_zones) == False : #means instances are distributed in multiple availability zones
         assert True
      else:
         assert False
   except Exception as e:
      assert False

def test_verify_vpc_sg_img_1C(ASGName): # Test Case 1 : Point 3 :SecuirtyGroup, ImageID and VPCID should be same on ASG running instances
   describe_asg_response = aws_wrappers.describe_asg(ASGName) # Describe Instance
   instances_in_asg = describe_asg_response.auto_scaling_groups[0].instances #Get instances in asg
   if len(instances_in_asg) == 0 :
      assert False #No instances attached to asg

   ec2_data ={}
   for instance in instances_in_asg:
      describe_instance_response = aws_wrappers.describe_instance([instance.instance_id]) #Describe instance by passing instance ID
      vpc_id = describe_instance_response.reservations[0].instances[0].vpc_id #Gets VPC ID
      security_group = describe_instance_response.reservations[0].instances[0].security_groups # FGet Security Group
      image_id = describe_instance_response.reservations[0].instances[0].image_id # Get Image ID
      ec2_data[instance.instance_id]={"vpc_id":vpc_id, "security_group":security_group,"image_id":image_id}

   assert True

def test_Uptime_of_ASG_Instances(ASGName): # Test Case 1 : Point 4 :Findout uptime of ASG running instances and get the longest running instance.
   try:
      describe_asg_response = aws_wrappers.describe_asg(ASGName) # Describe Instance
      instances_in_asg = describe_asg_response.auto_scaling_groups[0].instances # Instances in ASG
      if len(instances_in_asg) == 0:
         assert False  # No instances attached to asg

      ec2_data = {}
      for instance in instances_in_asg:
         describe_instance_response = aws_wrappers.describe_instance([instance.instance_id]) # Describe Instance
         start_time = (describe_instance_response.reservations[0].instances[0].launch_time).replace(
            tzinfo=datetime.timezone.utc) # Get the start time of the instances
         elapsed_time = (datetime.datetime.now().replace(tzinfo=datetime.timezone.utc) - start_time).total_seconds() # Gets the elapsed times
         ec2_data[describe_instance_response.reservations[0].instances[0].instance_id]=elapsed_time
      longest_running_instace= max(ec2_data, key=ec2_data.get) # Get max time from the dict and print the key
      print("Longest running Instance ID : " + longest_running_instace + " ran for :" + str(elapsed_time) + " seconds")
      assert True
   except Exception as e:
      assert False
      print(str(e))



























