import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift, ifftshift

# Thanks ChatGPT
def high_pass_filter_image(image, cutoff_frequency):
    fft_result = fft2(image)
    fft_shifted = fftshift(fft_result)
    rows, cols = image.shape
    mask = np.zeros((rows, cols))
    center = (rows // 2, cols // 2)
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 >= (cutoff_frequency ** 2)
    mask[mask_area] = 1
    fft_filtered = fft_shifted * mask
    filtered_image = ifft2(ifftshift(fft_filtered))

    return np.abs(np.array(filtered_image))


img_data = plt.imread("./blabr.png")
processed = high_pass_filter_image(img_data, 15)

plt.figure()
plt.imshow(processed)
plt.savefig("flag.png")

