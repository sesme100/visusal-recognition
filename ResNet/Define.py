
IMAGE_CHANNEL = 3
IMAGE_WIDTH = 32
IMAGE_HEIGHT = 32

CLASSES = 10

MAX_EPOCHS = 300
BATCH_SIZE = 128
MAX_ITERS = MAX_EPOCHS * int(50000 / BATCH_SIZE)

LEARNING_RATE = 1e-4

#CIFAR10 - ResNet
CONV_FILTERS = [32, 64, 128, 256]