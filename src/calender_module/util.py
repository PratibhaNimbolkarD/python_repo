import calendar
import logging

logging.basicConfig(level=logging.INFO , format='%(message)s')
def calender_module():


    weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    m, d, y = map(int, input("Enter the month,date and year : ").split())
    a = calendar.weekday(y, m, d)
    logging.info(weekdays[a])