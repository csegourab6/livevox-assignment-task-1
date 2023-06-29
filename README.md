## Project Details ##
This Test project is  developed in python using the pytest framework

### Requirements: ###
1. Python 3.x
2. PIP
3. Run: pip install -r requirements.txt 
4. Environment Variable Setup:
    * Key: TestAccessKey  Value: <<Your access key>>
    * Key: TestSecretKey  Value: <<Your secret key>>
    * Key: TestASGName    Value: <<Auto Scaling Group Name>>

### Running Project ###
 To Run the project use command:
    $ pytest -v --report.html

### Some Notes/ Explanations ##
1. This project is done using the pytest framework
2. The ASG that is provided doesnot have any attached instances and desired count is 0 and also the keys provided doesnot have access to create/ attach instances to ASG 
    Hence some of the test cases will fail where it asks atleast one instance is running
3. Two Test Cases that are given are present in two python files respectively:
   * Test Case A is present in test_AutoScale.py
   * Test Case B is present in test_ScheduledActions.py
    