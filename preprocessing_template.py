from .utils import cache_save, cache_load, cache_try_load


class PreprocessorTemplate:
    def __init__(self, config):
        """>> Preprocessor Template <<
        Do preprocess for building dataset

        :param config:
        """
        self.config = config

    @staticmethod
    def cache_save(variable, cache_file):
        """
        refer to templates.utils.cache_save

        :param variable:
        :param cache_file:
        """
        cache_save(variable, cache_file)

    @staticmethod
    def cache_load(cache_file):
        """
        refer to templates.utils.cache_load

        :param cache_file:
        """
        return cache_load(cache_file)

    @staticmethod
    def cache_try_load(cache_file, load_function, *args):
        """
        refer to templates.utils.cache_try_load

        :param cache_file:
        :param load_function:
        :param args:
        """
        return cache_try_load(cache_file, load_function, *args)
