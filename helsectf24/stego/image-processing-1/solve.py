import numpy as np
import matplotlib.pyplot as plt

img_data = plt.imread("./ekorn.png")
ft = np.fft.fft2(img_data)
fshift = np.fft.fftshift(ft)
spectrum = np.log(np.abs(fshift))

plt.figure()
plt.imshow(spectrum)
plt.savefig("flag.png")

