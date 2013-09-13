from mysite.credits.models import Student

def logfile_handler(rawfile):
	


for line in rawfile:
	[time, ID, status, s] = line.split(',')
	if status == 'STOP_RUNNING':
		print ID,status
raw_input()
