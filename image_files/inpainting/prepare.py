import os
import numpy as np
import PIL.Image as Image
import random


os.makedirs("image", exist_ok=True)
os.makedirs("mask", exist_ok=True)
os.makedirs("masked_image", exist_ok=True)
os.makedirs("output", exist_ok=True)


image_filst = [os.path.join("./image", fn) for fn in os.listdir("./image")]
image_filst.sort()

mask_filst = [os.path.join("./mask", fn) for fn in os.listdir("./mask")]
mask_filst.sort()

for idx in range(3):
    image_path = image_filst[idx]
    mask_path = mask_filst[idx]

    image = Image.open(image_path)
    image = image.resize((256,256))
    image = image.convert("RGB")
    mask = Image.open(mask_path)
    mask = mask.resize((256,256))
    mask = mask.convert("RGB")
    masked_image = Image.fromarray(np.maximum(np.array(image), np.array(mask)))

    print("\rProgress %05d/%05d"%(idx+1, len(image_filst)), end="")
    image.save("./image/image_%05d.png"%idx)
    mask.save("./mask/mask_%05d.png"%idx)
    masked_image.save("./masked_image/masked_image_%05d.png"%idx)

