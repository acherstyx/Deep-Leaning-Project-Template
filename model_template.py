import os
import tensorflow as tf
from .utils import mkdir


class ModelTemplate:
    def __init__(self, config):
        """>> Model Template <<
        Build tf.keras.Model, self.build() will be called automatically to build the deep learning model.

        :param config: configs you want to use in `build` method
        """
        self.config = config
        self.model = None

        self.build()

    def build(self, *args):
        """
        build the deep learning models here.
        """
        raise NotImplementedError

    def get_model(self, *args) -> tf.keras.Model:
        """
        return self.model

        :return:
        """
        if self.model is None:
            raise Exception("Error: Build the models first.")

        return self.model

    def show_summary(self, with_plot=False, with_text=True, dpi=100, *args):
        """
        show the summary of self.model

        :param with_text: show the text brief
        :param with_plot: show model in image
        :param dpi: dpi of chart
        :return: self
        """
        if self.model is None:
            raise Exception("Error: Build the models first.")

        if with_text:
            self.model.summary()
        if with_plot:
            tf.keras.utils.plot_model(self.model,
                                      to_file=self.__class__.__name__ + ".png",
                                      show_shapes=True,
                                      dpi=dpi)
        return self

    def save(self, path: str, args: object) -> None:
        """
        Save the weights of model.

        :param path:
        :param args:
        """
        self.model: tf.keras.Model
        try:
            self.model.save_weights(path)
        except OSError:  # if directory not exist
            mkdir(path)
            self.model.save_weights(path)

    def load(self, path: str, args: object) -> None:
        """
        Load weights.

        :param path:
        :param args:
        """
        self.model: tf.keras.Model
        self.model.load_weights(path)
