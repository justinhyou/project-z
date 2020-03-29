from datetime import datetime

def parseDate(dateString):
    return datetime.strptime(dateString, '%Y-%m-%d').date()

def workspace():
	return "/Users/hyobinyou/Desktop/project-z"

def cronJobName():
	return 'covid-data-refresh';