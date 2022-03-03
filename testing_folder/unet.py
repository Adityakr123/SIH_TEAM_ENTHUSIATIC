import cv2
import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np
import pandas as pd
from segmentation_models import Unet
os.chdir('/content/drive/My Drive/Images')
lst   = os.listdir('/content/drive/My Drive/Images')
print(lst)