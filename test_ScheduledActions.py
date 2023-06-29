from datetime import datetime
from aws_wrappers import AWS_Wrappers
from utility import Utility
utility = Utility()
aws_wrappers =AWS_Wrappers()

def test_ScheduledActions(ASGName): #TestCase B: Point 1: Find the Scheduled actions of given ASG which is going to run next and calcalate elapsed in hh:mm:ss from current time.
    try:
        scheduled_action_details = aws_wrappers.get_scheduled_actions(ASGName) # Get the sheduled actions of ASG
        scheduled_actions_list = scheduled_action_details.scheduled_update_group_actions  #List of Scheduled of scheduled actions
        if len(scheduled_actions_list) == 0:
            print("No Scheduled Actions found")
            assert False

        scheduled_action_recurrence={}
        try:
            for scheduled_action in scheduled_actions_list:
                # Get the next running time from Cron Expression and get the time delta between now and cron expression time
                scheduled_action_recurrence[scheduled_action.scheduled_action_name] = (utility.get_next_schedule_from_cron(scheduled_action.recurrence)-datetime.now()).total_seconds()

            next_running_job=  min(scheduled_action_recurrence, key=scheduled_action_recurrence.get) # Get the minimum time of jobs which is nothing but latest job to run
            print("Job to Run Next : " + next_running_job)
        except KeyError:
            pass ## if job is non recurring
        try:
            ## To find elapsed time from now from previous ran all jobs
            for scheduled_action in scheduled_actions_list:
                action_name= scheduled_action.scheduled_action_name # Get all action name list
                time_elapsed = datetime.now() - utility.get_previous_schedule_from_cron(scheduled_action.recurrence) # Get time of previous run from Cron
                print("Time Elapsed: " + action_name + "  "+str(time_elapsed)) ## prints elapsed time in hh:mm:ss
                assert True
        except KeyError:
            pass  ## if job is non recurring
    except Exception as e:
        assert False

def test_ScalingDayActivity(ASGName):
    try:
        scaling_activities =  aws_wrappers.describe_scaling_activities(ASGName) # Get all scaling activities result
        today_activities= []
        for activities in scaling_activities:
            for act in activities:
                start_date =  act['StartTime'].date() # get the start time of the instance
                status = act['StatusCode']
                if start_date == datetime.now().date() and status == 'Successful': # Get the activities of today wich are success
                    today_activities.append(act['ActivityId'])
            if len(today_activities)==0:
                print("No instances Launched or Terminated today")
                assert False
            else:
                print (str(len(today_activities))+ " instances launched or terminated today")
                assert True
    except Exception as e:
        print(str(e))
        assert  False


