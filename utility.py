'''
Utility Class
'''
from datetime import datetime
import numpy
from cron_converter import Cron
class Utility:
    def count_value_dict(self,dict,value):
        '''

        :param dict: Any Dictionary
        :param value:  value to search
        :return: Count of occurence of the value
        '''
        count = 0
        for val in dict.values():
            if val == value:
                count += 1
        return count


    def check_unique(self,lst):
        '''

        :param lst: Any List object
        :return:  True if the list contains unique values
        '''
        unique_elements, counts = numpy.unique(lst, return_counts=True)
        return all(counts == 1)

    def get_next_schedule_from_cron(self,cronExpression):
        '''

        :param cronExpression: Any Cron Expression
        :return: DateTime Object when the job will run Next
        '''
        cron_instance = Cron(cronExpression)
        # Raw datetime without timezone info (not aware)
        reference = datetime.now()
        # Get the iterator, initialised to now
        schedule = cron_instance.schedule(reference)
        return schedule.next()

    def get_previous_schedule_from_cron(self,cronExpression):
        '''

        :param cronExpression: Any Cron Expression
        :return: DateTime Object when the job has run last
        '''
        cron_instance = Cron(cronExpression)
        # Raw datetime without timezone info (not aware)
        reference = datetime.now()
        # Get the iterator, initialised to now
        schedule = cron_instance.schedule(reference)
        return schedule.prev()

