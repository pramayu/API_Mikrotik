import paramiko
from functools import wraps


def check_auth(fn):
	@wraps(fn)

	def decoration(*args, **kwargs):
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(
			kwargs['ip_address'],
			username=kwargs['username'],
			password=kwargs['password'])

		# if client login
			# exec command
		# else
			# send message error

		return fn(client, *args, **kwargs)
	return decoration