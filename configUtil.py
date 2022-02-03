# Python external executables

# Library imports
import configparser
import logging
import os
import platform
from utilityOperations import DirectoryOperations, StringOperations
from utilityOperations import FileOperations
from appLogging import AppLogging

logger = AppLogging('configUtil')


class ConfigurationUtil:
    config = configparser.ConfigParser()
    valid_cfg_files = []
    config_dict = {}

    def __init__(self, config_directory, *config_files):
        config_filetype = '.ini'
        if len(config_files) < 1:
            logger.error('No config file found for application initialization')
        else:
            if DirectoryOperations.check_directory_exists(config_directory):
                for config_file in config_files:
                    os.chdir(config_directory)
                    if FileOperations.check_file_exists(config_file) and FileOperations.check_file_extension(config_file, config_filetype):
                        self.valid_cfg_files.append(config_file)
                        logger.info('Config file found: ' + config_file)
                    else:
                        logger.error('Config file not found: ' + config_file)
            else:
                logger.error('Config source directory not found: ' + config_directory)

    def read_config(self):
        if len(self.valid_cfg_files) > 0:
            for cfg_file in self.valid_cfg_files:
                cfg_file.index('.ini')
                logger.debug('Reading config:' + cfg_file)
                self.config.read(cfg_file)
                cfg = os.path.splitext(cfg_file)[0]
                self.config_dict[cfg] = {}
                for section in (self.config.sections()):
                    self.config_dict[cfg][section] = {}
                    for config_key in (self.config[section]):
                        config_value = self.config[section][config_key]
                        self.config_dict[cfg][section][config_key] = config_value
                        # logger.debug(cfg_file + ':' + section + ':' + config_key + ':' + config_value)
        return self.config_dict
