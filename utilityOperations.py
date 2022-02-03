# Python directory operations

# Library imports
import os
import shutil
import subprocess

from pathlib import Path

from appLogging import AppLogging

# formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')
# stream_handler = logging.StreamHandler(sys.stdout)
# stream_handler.setFormatter(formatter)
# logger = logging.getLogger()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)

logger = AppLogging('utilityOperations')


class DirectoryOperations:

    @staticmethod
    def check_directory_exists(directory_name: str) -> bool:
        """
        Check if a directory exists or not
        :param directory_name:
        :return: True, if directory exists
        """
        if os.path.isdir(directory_name):
            logger.debug('Directory exists: ' + directory_name)
            return True
        else:
            logger.error('Directory does not exist: ' + directory_name)
            return False

    @staticmethod
    def make_directory(directory_name: str) -> bool:
        """
        Make directory in current location, equivalent to mkdir in Unix
        :param directory_name: Name of the directory to create
        :return: True, if directory has been created
        """
        if not DirectoryOperations.check_directory_exists(directory_name):
            try:
                os.mkdir(directory_name)
                logger.debug('Directory created: ' + directory_name)
                return True
            except OSError:
                logger.error('Cannot create directory: ' + directory_name)
                return False

    @staticmethod
    def make_path_directory(directory_name: str) -> bool:
        """
        Make directory with paths, equivalent to mkdir -p in Unix
        :param directory_name: Name of the directory with parent paths to create
        :return: True, if directories were created
        """
        if not DirectoryOperations.check_directory_exists(directory_name):
            try:
                os.makedirs(directory_name)
                logger.debug('Directory created: ' + directory_name)
                return True
            except OSError:
                logger.error("Cannot create directory: " + directory_name)
                return False

    @staticmethod
    def delete_directory(directory_name: str) -> bool:
        """
        Delete a directory and it's contents
        :param directory_name: Directory to delete
        :return: True, if the directory has been deleted
        """
        if not DirectoryOperations.check_directory_exists(directory_name):
            logger.debug('Directory created: ' + directory_name)
            return False
        else:
            try:
                shutil.rmtree(directory_name)
                logger.debug('Directory deleted: ' + directory_name)
            except FileNotFoundError:
                logger.error("Directory not found to delete:" + directory_name)
                return False
            return True


class FileOperations:

    @staticmethod
    def check_file_exists(file_name: str) -> bool:
        """
        Check if a file exists
        :param file_name: Filename, to check for existence
        :return: True, if the file exists
        """
        if os.path.isfile(file_name):
            logger.debug('File exists: ' + file_name)
            return True
        else:
            logger.error('File does not exist: ' + file_name)
            return False

    @staticmethod
    def check_file_extension(file_name: str, file_extension: str):
        """
        Check if a file ends with an extension
        :param file_name: file to check for extension
        :param file_extension: file extensions
        :return: True, if file has the desired extension
        """
        if os.path.splitext(file_name)[1].lower() == file_extension:
            return True
        else:
            return False


class StringOperations:

    @staticmethod
    def is_empty(in_string: str) -> bool:
        if not in_string:
            logger.debug(in_string + ': null')
            return True
        else:
            return False


class ExecuteOperations:

    @staticmethod
    def exec_java_jar(jar_file: str, *java_args: list):
        """
        Executes a java jar file with args
        :param jar_file:
        :param java_args:
        :return:
        """
        java_executable = 'java'
        jar_option = '-jar'

        args_len = len(java_args)
        logger.debug('Number of JAVA args:' + str(args_len))

        if not StringOperations.is_empty(jar_file):
            exec_arr = [java_executable, jar_option, jar_file]
            if args_len > 0:
                exec_arr.extend(java_args)
                for index in range(args_len):
                    logger.debug('Arg[' + str(index) + '] = ' + java_args[index])
                logger.debug('Calling JAVA JAR with args: ' + jar_file)
                subprocess.call(exec_arr)
            else:
                logger.debug('Calling JAVA with no args: ' + jar_file)
                subprocess.call(exec_arr)
        else:
            logger.error("No valid JAR file to execute")

