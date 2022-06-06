import os

from crontab import CronTab

'''
    This module is responsible for scheduling in crontab
'''

GREEN = '\033[92m[+]\033[0m'
RED = '\033[31m[*]\033[0m'

# set the schedules
SCHEDULES_TIME = ['10:00', '11:00', '12:00']


def set_schedules():
    venv = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.venv/bin/python3'))
    module_main = os.path.abspath(os.path.join(os.path.dirname(__file__), 'main.py'))
    path_log = os.path.abspath(os.path.join(os.path.dirname(__file__), 'logs/cron.log'))

    # Getting and iterating over calendar data
    for sched_time in SCHEDULES_TIME:
        hour = int(sched_time.split(':')[0])
        user_cron = CronTab(user=True)

        # command = ~/path to virtual environment ~/path to the module to be executed by crontab ~/path to log file
        job = user_cron.new(command=f'{venv} {module_main} -t {sched_time} >> {path_log} 2>&1')

        job.setall(f'01 {hour} * * 1-5')
        user_cron.write()
    print(f'{GREEN} Scheduling done.')


if __name__ == '__main__':
    set_schedules()
