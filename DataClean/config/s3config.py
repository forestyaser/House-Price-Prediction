from configparser import ConfigParser

config = ConfigParser()
config.read('/var/qindom/realmaster/DataCleanService.conf')

aws_access_key_id = config.get('s3Section', 'aws_access_key_id')
aws_secret_access_key = config.get('s3Section', 'aws_secret_access_key')
test_real_master_bucket = config.get('s3Section', 'test_real_master_bucket')
real_master_bucket = config.get('s3Section', 'real_master_bucket')
internal_real_master_bucket = config.get('s3Section', 'internal_real_master_bucket')
