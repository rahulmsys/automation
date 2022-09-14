import configparser


class ConfigReader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def get_config_value(self, section, key):
        return self.config[section][key]
