import os
import tensorflow as tf

from datetime import datetime


class TrainerTemplate:
    def __init__(self, model, data, config):
        """>> Trainer Template <<
        Init the trainer. Use trainer to organize dataset and model, control training process.

        :param model:
        :param data: data loader
        :param config: config you want to use
        """
        self.model = model
        self.data = data
        self.config = config

        self.callbacks = []
        self.metrics = []

        self.checkpoint = None

        # timestamp for log file
        self.timestamp = "{0:%Y-%m-%dT%H-%M-%SW}".format(datetime.now())

    def train(self, *args):
        """
        Define how to train your model.
        """
        raise NotImplementedError

    @staticmethod
    def save(model, path: str) -> None:
        """
        Save the weights of model.

        :param model:
        :param path:
        """
        model: tf.keras.Model
        try:
            model.save_weights(path)
        except OSError:  # if directory not exist
            os.makedirs(os.path.join(*os.path.split(path)[:-1]))
            model.save_weights(path)

    @staticmethod
    def load(model, path: str) -> None:
        """
        Load weights.

        :param model:
        :param path:
        """
        model: tf.keras.Model
        model.load_weights(path)
