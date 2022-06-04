from crontab import CronTab

'''
    This module is responsible for scheduling in crontab
'''

GREEN = '\033[92m[+]\033[0m'
RED = '\033[31m[*]\033[0m'

SCHEDULES_TIME = ['10:00', '11:00', '12:00', '13:00', '14:00']


def set_schedules():
    # Getting and iterating over calendar data
    for sched_time in SCHEDULES_TIME:
        hour = int(sched_time.split(':')[0])
        user_cron = CronTab(user=True)

        # command = ~/path to virtual environment ~/path to the module to be executed by crontab
        job = user_cron.new(command='/home/drakon/Documents/PROJETOS/ptax/.venv/bin/python3 '
                                    f'/home/drakon/Documents/PROJETOS/ptax/ptax/main.py -t {sched_time} >> '
                                    '/home/drakon/Documents/PROJETOS/ptax/ptax/logs/cron.log  2>&1 ')
        job.setall(f'* {hour} * * 1-5')
        user_cron.write()
    print(f'{GREEN} Scheduling done.')


if __name__ == '__main__':
    set_schedules()
