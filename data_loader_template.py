import tensorflow as tf
import pickle


class DataLoaderTemplate:
    """
    >> Data Loader Template <<

    Generate a `tf.data.Dataset` object as dataset, and save it to `self.dataset`.
    """

    def __init__(self, config):
        """
        Init the data loader.
        :param config: configs
        """
        self.config = config

        # the data will be load automatically by calling self.load()
        self.dataset = None  # take position
        self.load()

    def load(self):
        """
        Load data.
        """
        raise NotImplementedError

    def get_dataset(self) -> tf.data.Dataset:
        """
        return the dataset
        :return: dataset
        """
        if self.dataset is None:
            raise Exception("Error: Load data first, and save it to `self.dataset`")

        return self.dataset

    def cache_save(self, cache_file, *args):
        pickle.dump(self.dataset, cache_file, 0)

    def cache_load(self, cache_file, *args):
        self.dataset = pickle.load(cache_file)
