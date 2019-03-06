from medpy.io import load
import os
import itk
import skimage
import SimpleITK as sitk
from skimage.morphology import label
from skimage.io import imread, imshow, imread_collection, concatenate_images
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from keras.layers import Input, MaxoutDense
from keras.layers.core import Lambda
from keras.layers.convolutional import Conv2D, Conv2DTranspose, Conv3D
from keras.layers.pooling import MaxPooling2D
from keras.models import Model, load_model
from keras.layers.merge import concatenate
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.optimizers import Adam

from keras import backend as K

data_path = '../patients/'
IMG_H = 128
IMG_W = 128

train_ids = next(os.walk(data_path))[1]