# PatchMatch for inpainting

![](https://img.shields.io/badge/build-passing-green)  ![](https://img.shields.io/badge/opencv-3.x-green)  ![](https://img.shields.io/badge/cmake-%3E2.8-orange)  ![](https://img.shields.io/badge/Lisence-MIT-yellow)

## Introduction

This repository borrows most of the code from [younesse-cv](https://github.com/younesse-cv/PatchMatch).  However that repository is C style, which cannot be compiled using `opencv 3.x`.  What I did is wrapping the code using `opencv 3.x` API in C++ style. Thanks [zvezdochiot](https://github.com/zvezdochiot) for suggestion.



## Dependencies

- cmake > 2.8
- opencv 3.x
- g++-4.7



## How to use

- Download this repository

  ```bash
  git clone https://github.com/ZQPei/patchmatch_inpainting.git
  ```

- Compile

  ```bash
  mkdir build
  cd build
  cmake ..
  make
  cd ..
  ```

- Run  
  As what does in `run.sh`.

  ```bash
  for i in 0 1 2; do
    ./build/patchmatchs image_files/inpainting/image/image_0000$i.png \
                        image_files/inpainting/mask/mask_0000$i.png \
                        image_files/inpainting/output/output_0000$i.png \
                        image_files/inpainting/metrics.log \
                        $i;
  done
  ```

  Or simple:
  ```sh
    ./build/patchmatch image_files/forest/forest.bmp \
                       image_files/forest/forest_mask.png \
                       image_files/forest/forest_inpaint.png
  ```


## Demo

| mask                                                  | masked image                                                 | inpainting image using PatchMatch                                                  | origin image                                                 |
| ----------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------ |
| ![](./image_files/inpainting/mask/mask_00001.png)     | ![](./image_files/inpainting/masked_image/masked_image_00001.png) | ![](./image_files/inpainting/output/output_00001.png)     | ![](./image_files/inpainting/image/image_00001.png) |






## References

https://github.com/younesse-cv/PatchMatch

