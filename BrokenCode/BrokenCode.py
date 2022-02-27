#!/usr/bin/python3
from datetime import date
date = date.today()
today = str(date)
username = str(input('Hello User, What is your name? '))
print('Hello, '+username+' The current date is '+today)