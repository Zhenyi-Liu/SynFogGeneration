import numpy as np
import scipy.io as scio
from PIL import Image


airlight = 0.5836308088117068
A = np.array([airlight, airlight, airlight])
beta = 0.1

depth_path = 'F:/Blender/20230324/depth.mat'
depth = scio.loadmat(depth_path)['depth']

path = './0324/test.png'
img = np.array(Image.open(path))

I0 = img / 255.0
I1 = np.zeros(shape=(depth.shape[0], depth.shape[1], 3), dtype=np.float32)
transmission = np.zeros(shape=(depth.shape[0], depth.shape[1]), dtype=np.float32)

for c in range(3):  
    transmission = np.exp(-beta*depth)
    I1[:, :, c] = I0[:, :, c] * transmission + A[c] * (1 - transmission)

Image.fromarray((I1 * 255).astype(np.uint8)).save('./0324/foggy_0_1.png')