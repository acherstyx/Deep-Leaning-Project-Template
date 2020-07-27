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

    def save(self, path: str, *args) -> None:
        """
        Save the weights of model.

        :param path:
        :param args:
        """
        self.model: tf.keras.Model
        try:
            self.model.save_weights(path)
        except OSError:  # if directory not exist
            os.makedirs(os.path.join(*os.path.split(path)[:-1]))
            self.model.save_weights(path)

    def load(self, path: str, *args) -> None:
        """
        Load weights.

        :param path:
        :param args:
        """
        self.model: tf.keras.Model
        self.model.load_weights(path)
