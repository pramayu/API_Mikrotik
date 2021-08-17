class Config(object):
	TESTING=False
	DEBUG=False
	DEVELOPMENT=False

class Production(Config):
	pass

class Development(Config):
	TESTING=True
	DEBUG=True
	DEVELOPMENT=True