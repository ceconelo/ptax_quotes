
# Scraping Ptax Quotes

Basically the project consists of 4 stages

1. Crontab starts main.py at the scheduled times (10:00, 11:00 and 12:00)
2. Search for ptax quotes on the bacen site
2. Validation of quotes
2. Posting of the quotes on twitter




## Step by step

E.g: schedule 10:00

A. Crontab starts main.py by passing an argument (--time ) which in this case is 10:00.

B. Main calls the module responsible for fetching the quotes

C. When the module returns the object(json) we do some validations.

	-> If it is empty a 5 min timer will be triggered starting a looping and after 
        that new attempts will be made until the quote is available on the site.
	-> If the object (json) comes with data we will use the --time argument 
        (which in the example is 10:00) as a validation condition for the next steps
		-> We take the time of the last line of the object and check if it is greater 
            or equal to the time of the passed argument (10:00)
			-> If it is bigger it means that the quote is new
			-> If it is lesser it means that a new quote was not available yet, then a 
            5 min. timer will be activated starting a looping and after that new attempts 
            will be made until the quote is available on the site.

D. When the quote is new we take the object that contains the quotes, format it and send it 

to the module responsible for posting it on twitter.



## How to use

1. Create the virtual environment


For project package management I am using poetry but if you want to use pip I am 

leaving the file requirements.txt for installing the dependencies.


-> How to install poetry (Linux)
```python

#Install
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

# To configure your current shell run
source $HOME/.poetry/env
```

By default poetry creates virtual environments in a temporary folder outside the 
project folder. 

To change this behavior by having poetry create the virtual 
environment folder inside the project folder run:

```python
poetry config virtualenvs.in-project true
```


With poetry installed on your machine and inside on your project folder run the 

command below to install all project dependencies.


```python
poetry install
```

1. In the settings.ini file


```ini
###########################
### Twitter Credentials ###
###########################

[credentials]
api_key = fill
api_key_secret = fill
bearer_token = fill
access_token = fill
access_token_secret = fill

###############
### Logging ###
###############

[handler_FileHandler]
args = ('fill in the absolute path to the log file, 'a')
```
2. In the file create_schedules.py

```python
# set the schedules
SCHEDULES_TIME = ['10:00', '11:00', '12:00']

# set paths
job = user_cron.new(
    command='~/path to virtual environment/ptax/.venv/bin/python3 '
           f'~/path to the module to be executed by crontab/ptax/ptax/main.py -t {sched_time} >> '
            '~/path to log file/ptax/ptax/logs/cron.log  2>&1 ')

```
To create the schedules

```python
python3 create_schedules.py
```