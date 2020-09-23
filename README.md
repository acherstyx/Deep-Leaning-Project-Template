# Deep Leaning Project Template

深度学习项目模板。

本项目针对为Tensorflow V2环境之下编写深度学习的项目提供一个统一的模板类，将整一个深度学习的项目概括为以下部分组成：

- Preprocessor：对数据进行一定程度的预处理。（可选）
- Dataloader：创建一个用于加载数据的加载器，在V2中主要指了创建一个`tf.data.Dataset`类。
- Model：定义一个深度神经网络，最终的结果应该是创建一个`tf.keras.Model`类。
- Trainer：主要负责定义一个具体的训练过程中，如何使用数据集和模型，内部应该定义具体的训练策略。
- Config：Config类是作为参数来使用的，用于在以上的各个类中传递深度学习所需的超参数、配置参数等。

## 获取与使用

推荐通过Git的submodule来添加这一个项目为一个子模块。
但如果在子模块内对这一Template项目做了更改，这些修改只能提交到子模块所属的Git项目中。（详见关于git submodule的相关介绍，推荐先详细阅读submodule的使用指南）因此如果有修改需要，推荐先Fork一份来自用。

submodule的添加使用以下shell命令：

```shell
git submodule add git@github.com:AcherStyx/Deep-Leaning-Project-Template.git templates
```

执行后会新增一个`.gitmodules`文件和`templates`文件夹，提交更改的时候把两者的更改一起提交即可。

在其他Python代码中，通过执行：

```python
from templates import *
```

即可导入所有的模板。

## 模板类

### ConfigTemplate

Config类没有给出明确的定义，一个Config的创建方式应该是通过其`__init__`的参数提供具体的配置取值。

```python
class XXX_TrainerConfig(ConfigTemplate):
    def __init__(learning_rate, epoch):
        self.LR = learning_rate
        self.EPOCH = epoch
```

在之后的所有类中，初始化时大多都需要提供一个Config来传递配置，并赋值到`self.config`，所以通过`self.config.XXX`即可访问到对应的配置。

### DataLoaderTemplate和PreprocessorTemplate

无论是DataLoader还是Preprocessor都是用于数据加载的，DataLoaderTemplate也是继承自PreprocessorTemplate。
主要的区别在于DataLoader是用于最终创建一个Dataset的，准确地说应该创建一个可以直接使用的`tf.data.Dataset`类，因此多了`load()`方法，并且需要注意的是`load()`在`__init__()`中自动进行了调用，必须复写`load()`方法。在`load()`中需要定义完整的数据加载的代码，并最终将创建好的数据集赋值给`self.dataset`。  

```python
class XXX_DataLoader(DataLoaderTemplate):
    def load():
        ...
        self.dataset = tf.data.Dataset.from_tensor_slice((image, label))
```

通过`get_dataset()`方法返回self.dataset变量。

### ModelTemplate

Model中应该给出一个Tensorflow下网络模型的具体定义的代码，通过Keras的API创建一个`tf.keras.Model`类。（具体创建方法可参考官方文档，[keras函数式API](https://www.tensorflow.org/guide/keras/functional)）
创建完成的model应该赋值给`self.model`。

### TrainerTemplate

一个Trainer主要负责定义训练的过程，因此Trainer初始化时需要将Model和Dataset都传入。在Trainer中定义模型该怎样从Dataset中取出数据，并提供给Model训练。

## 参考项目示例

-  https://github.com/AcherStyx/DDoS-DeepLearning-Approach
