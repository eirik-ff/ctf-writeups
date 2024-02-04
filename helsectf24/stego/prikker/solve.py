import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence

gif_path = "./prikker.gif"

plt.figure(figsize=(10, 2))

target_color = [139, 0, 0]

accum = np.array([])
with Image.open(gif_path) as gif:
    for frame_number, frame in enumerate(ImageSequence.Iterator(gif)):
        frame = np.array(frame)
        if frame_number == 0:
            accum = np.zeros((*frame.shape, 3), dtype=frame.dtype)
            continue

        include = all(c in frame[:, :, i] for i, c in enumerate(target_color))
        if include:
            accum = accum + frame

plt.imshow(accum)
plt.title("Flag")
plt.savefig("flag.png")

