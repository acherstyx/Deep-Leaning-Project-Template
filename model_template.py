import tensorflow as tf
from .utils import mkdir


class ModelTemplate:
    def __init__(self, **kwargs):
        """>> Model Template <<
        Build tf.keras.Model, self.build() will be called automatically to build the deep learning model.

        :param config: configs you want to use in `build` method
        """
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

    @staticmethod
    def _show_summary(model, model_name, with_plot=False, with_text=True, dpi=100):
        if with_text:
            model.summary()
        if with_plot:
            tf.keras.utils.plot_model(model,
                                      to_file=model_name + ".png",
                                      show_shapes=True,
                                      dpi=dpi)

    def show_summary(self, with_plot=False, with_text=True, dpi=100, **kwargs):
        """
        show the summary of self.model

        :param with_text: show the text brief
        :param with_plot: show model in image
        :param dpi: dpi of chart
        :return: self
        """
        if self.model is None:
            raise Exception("Error: Build the models first.")

        self._show_summary(model=self.model,
                           model_name=self.__class__.__name__,
                           with_text=with_text,
                           with_plot=with_plot,
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

    def load(self, path: str, *args: object) -> None:
        """
        Load weights.

        :param path:
        :param args:
        """
        self.model: tf.keras.Model
        self.model.load_weights(path)
