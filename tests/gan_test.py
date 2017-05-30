import tensorflow as tf
import hyperchamber as hc
import numpy as np
from hypergan.discriminators.pyramid_discriminator import PyramidDiscriminator
from hypergan.ops import TensorflowOps

from unittest.mock import MagicMock

from hypergan.search.default_configurations import DefaultConfigurations

from hypergan import GAN


graph = hc.Config({
    'x': tf.constant(1., shape=[32,32,32])
})


class MockOps:
    def __init__(self):
        self.mock = True

class MockTrainer:
    def __init__(self):
        self.mock = True


class GANTest(tf.test.TestCase):
    def test_constructor(self):
        with self.test_session():
            gan = GAN(graph = graph, ops = MockOps)
            self.assertEqual(gan.graph.x, graph.x)

    def test_train(self):
        trainer = MockTrainer()
        config = {}
        config['trainer'] = trainer
        with self.test_session():
            gan = GAN(graph = graph, ops = MockOps, config = config)
            gan.train()
            self.assertEqual(gan.step, 1)

    def test_default(self):
        with self.test_session():
            gan = GAN(graph = graph, ops = TensorflowOps, config = DefaultConfigurations.get())
            gan.train()
            self.assertEqual(gan.step, 1)

if __name__ == "__main__":
    tf.test.main()
