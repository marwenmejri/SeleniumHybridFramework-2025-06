import configparser

config = configparser.RawConfigParser()
config.read('Configuration/config.ini')


def get_username():
	return config.get('common info', 'username')


def get_password():
	return config.get('common info', 'password')


def get_url():
	return config.get('common info', 'base_url')