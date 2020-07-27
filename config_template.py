import json
from .utils import mkdir


class ConfigTemplate:
    """>> Config Templates <<

    Use __init__ to set the value of your config.

    e.g.

    class MyConfig(ConfigTemplate):
        def __init__(self, learning_rate):
            self.LEARNING_RATE = learning_rate
    """

    def dump(self, json_file: str = None) -> object:
        """
        Dump the config to json string. Use this to keep your config.

        :param json_file:  if json_file is specified, the result (json string) will be save to that file
        :return:
        """
        if json_file is not None:
            try:
                with open(json_file, "w") as f:
                    json.dump(self.__dict__, f)
            except FileNotFoundError:
                mkdir(json_file)
                with open(json_file, "w") as f:
                    json.dump(self.__dict__, f)

        return json.dumps(self.__dict__)

    @staticmethod
    def load(json_file: str) -> object:
        """
        Load config from a json file.

        :param json_file:
        :return: object with same class
        """
        print(__class__)
        with open(json_file, "r") as f:
            new_config = __class__()
            new_config.__dict__ = json.load(f)
            return new_config
