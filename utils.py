import os
import pickle
import logging

logger = logging.getLogger(__name__)


def mkdir(file_path, root=""):
    """
    make directory to solve FileNotFoundError while writing a file

    :param file_path: path to a file you want to write (not a directory)
    :param root: root directory (usually do not need to change)
    """
    directory = os.path.split(file_path)[0]

    if not os.path.exists(directory):
        os.makedirs(directory)


def cache_save(variable, cache_file):
    """
    create cache for variable using pickle

    :param variable: variable need to be cached
    :param cache_file: path to cache file
    """
    try:
        with open(cache_file, "wb") as f:
            pickle.dump(variable, f, 0)
    except FileNotFoundError:
        mkdir(cache_file)
        with open(cache_file, "wb") as f:
            pickle.dump(variable, f, 0)
    logger.info("Cache is saved to %s", cache_file)


def cache_load(cache_file):
    """
    recover variable from cache file

    :param cache_file: path to cache file
    :return: recovered variable
    """
    with open(cache_file, "rb") as f:
        variable = pickle.load(f)
    logger.info("Cache is loaded from %s", cache_file)
    return variable


def cache_try_load(cache_file, load_function, *args):
    """
    try to load variable from cache file.
    if not exist, call `load_function`.

    :param cache_file:
    :param load_function:
    :param args:
    :return:
    """
    try:
        return cache_load(cache_file)
    except FileNotFoundError:
        variable = load_function(*args)
        cache_save(variable, cache_file)
        return variable


# test case
if __name__ == '__main__':
    mkdir("hello/world/file_name")
    cache_save("hello, world!", "hello/world/a/cache_file")
