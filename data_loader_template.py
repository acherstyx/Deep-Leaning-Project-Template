import tensorflow as tf

from .preprocessing_template import PreprocessorTemplate


class DataLoaderTemplate(PreprocessorTemplate):
    """>> Data Loader Template <<

    Generate a `tf.data.Dataset` object as dataset, and save it to `self.dataset`.
    """

    def __init__(self, config):
        """
        Init the data loader.

        :param config: configs
        """
        super(DataLoaderTemplate, self).__init__(config)

        self.config = config

        # the data will be load automatically by calling self.load()
        self.dataset = None  # take position
        self.load()

    def load(self, *args):
        """
        Load data.

        """
        raise NotImplementedError

    def get_dataset(self, *args) -> tf.data.Dataset:
        """
        return the dataset

        :return: dataset
        """
        if self.dataset is None:
            raise Exception("Error: Load data first, and save it to `self.dataset`")

        return self.dataset
