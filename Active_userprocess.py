def activeProcesses(lookup_user):
""" Look up how many processes a user is running """
processes_running = 0
for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
	user = line.split()[0]
	if lookup_user == user:
		processes_running+=1
	return "User %s has %s processes running" % (lookup_user, processes_running)
print activeProcesses('root')
print activeProcesses('postfix')

def activeProcesses(lookup_user, lookup_cmd):
""" Look up how many command of a particular type a user is running
"""
processes_running_all = 0
processes_running_searched = 0
for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
	user = line.split()[0]
	if lookup_user == user:
		processes_running_all+=1
		if lookup_cmd in line:
			processes_running_searched+=1
	return processes_running_all, processes_running_searched

procs_total, procs_searched = activeProcesses('root', 'aws')
print procs_total, procs_searched