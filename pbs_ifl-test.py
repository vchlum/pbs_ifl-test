import sys
import pbs_ifl

if len(sys.argv) < 2:
	print('missing argument')
	exit(1)

c = None

try:
	c = pbs_ifl.pbs_connect(sys.argv[1])
except:
	print('failed to connect to the server')
	exit(1)

try:
	server_info = pbs_ifl.pbs_statserver(c, None, None)
	print(server_info)
except:
	print('failed to get server info')
	exit(1)

try:
	queue_info = pbs_ifl.pbs_statque(c, None, None, None)
	print(queue_info)
except:
	print('failed to get queues info')
	exit(1)

try:
	node_info = pbs_ifl.pbs_statvnode(c, None, None, None)
	print(node_info)
except:
	print('failed to get nodes info')
	exit(1)

try:
	job_info = pbs_ifl.pbs_statjob(c, None, None, "xt")
	print(job_info)
except:
	print('failed to get jobs info')
	exit(1)

try:
	pbs_ifl.pbs_disconnect(c)
finally:
	c = None
