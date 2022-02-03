# Python3 Executable

# Import statements
from appLogging import AppLogging
from configUtil import ConfigurationUtil
from utilityOperations import DirectoryOperations
from utilityOperations import ExecuteOperations
import sys
import json


def check_args_exist(args_length):
    if args_length > 0:
        return True
    else:
        return False


# Configure logging
logger = AppLogging('helloPython')


logger.info("HELLO Python!")
len_args = len(sys.argv)
logger.info("Python Args: " + str(len_args))
if len_args > 1:
    if check_args_exist(len_args - 1):
        logger.info("Program Args: " + str(len_args - 1))
        for each_arg in sys.argv:
            logger.info('Python Arg: ' + each_arg)

# Check directory exists
DirectoryOperations.check_directory_exists('config')

# Execute Java JAR file
java_jar = '/Users/sriramsubramaniam/IdeaProjects/helloWorld/target/helloWorld-1.0-SNAPSHOT.jar'
ExecuteOperations.exec_java_jar(java_jar)
ExecuteOperations.exec_java_jar(java_jar, 'hello', 'to', 'JAVA', 'world', 'Sriram')

# Initialize configuration files
config = ConfigurationUtil('/Users/sriramsubramaniam/PycharmProjects/python-app/config', 'env-dev.ini', 'storage.ini')
# Reading configuration
config_val = config.read_config()
# Log the configuration
logger.info(json.dumps(config_val, indent=4))

# Storage configurations
nas_mounts = config_val['storage']['nas']
s3 = config_val['storage']['s3']
logger.info("Input NAS:" + nas_mounts['in-nas'])
logger.info("DUC NAS:" + nas_mounts['duc-nas'])
s3_conn_str = s3['protocol'] + "://" + s3['username'] + ":" + s3['password'] + "@" + s3['provider'] + "/" + s3['bucket']
logger.info("S3 Connection:" + s3_conn_str)
