IMG_PATH = "../datasets/images/"
IMG_HEIGHT = 512  # The images are already resized here
IMG_WIDTH = 512  # The images are already resized here

SEED = 42
TRAIN_RATIO = 0.75
VAL_RATIO = 1 - TRAIN_RATIO
SHUFFLE_BUFFER_SIZE = 100

LEARNING_RATE = 1e-3
EPOCHS = 20
TRAIN_BATCH_SIZE = 2  # My GPU memory is too small to support larger batch_size
TEST_BATCH_SIZE = 2
FULL_BATCH_SIZE = 2

###### Train and Test time #########

DATA_PATH = "../datasets/images/"
AUTOENCODER_MODEL_PATH = "baseline_autoencoder.pt"
ENCODER_MODEL_PATH = "../data/models/deep_encoder.pt"
DECODER_MODEL_PATH = "../data/models/deep_decoder.pt"
EMBEDDING_PATH = "../data/models/data_embedding_f.npy"
EMBEDDING_SHAPE = (1, 256, 16, 16)
# TEST_RATIO = 0.2

###### Test time #########
NUM_IMAGES = 10
TEST_IMAGE_PATH = "../datasets/images/11668747ua_tools_f2l.jpg"
