# Computer Vision Fruit Inspection Project

## Overview

This project focuses on automating fruit inspection using computer vision techniques. The primary goals include fruit segmentation, defect detection, color analysis, and image manipulation.

## Tasks

### Task 1: Fruit Segmentation and Defect Detection

In this task, the objective is to segment fruits from images and detect defects and imperfection on fruits. Key steps include:

- **Image Preprocessing:** Applying blur and thresholding techniques to enhance fruit features.
- **Contour Detection:** Locating contours of fruits within the images.
- **Defect Identification:** Implementing algorithms to identify defects based on contours.

Relevant code files: `Task1.ipynb` `utils.py` 
![image](https://github.com/AxelCenteno/FruitAnalysisProject/assets/34460585/0ab3ad68-8c45-445a-8288-70da9290faf5)


### Task 2: Russet Detection (Color Analysis and Mahalanobis Distance)

This task involves color analysis using Mahalanobis distance for defect detection. Steps include:

- **Color Space Conversion:** Converting images to different color spaces such as HSV, HLS, and LUV.
- **Mahalanobis Distance Calculation:** Computing Mahalanobis distance for each pixel in the image.
- **Thresholding:** Setting a threshold to identify defective regions.

Relevant code files: `Task2.ipynb` `utils.py` 
#### First set of images
![image](https://github.com/AxelCenteno/FruitAnalysisProject/assets/34460585/f20bb949-fa47-44a0-9533-8d15192aaf56)
#### Second set of images
![image](https://github.com/AxelCenteno/FruitAnalysisProject/assets/34460585/05466211-9ba6-4d7d-bac8-2e9e3a80fc50)

#### Both set of images
![image](https://github.com/AxelCenteno/FruitAnalysisProject/assets/34460585/c286252b-bb10-48f5-b904-432fd173fc97)
![image](https://github.com/AxelCenteno/FruitAnalysisProject/assets/34460585/a54a5fca-1a5c-41f3-885d-e9857cfccbda)

### Final challenge: Kiwi Inspection

This task aims to identify a bunch of images of a Kiwi and identify the defective one having images with backgrounds that could interfer with the analysis

- **Morphological Operations:** Utilizing operations like opening and dilation to enhance segmentation.
- **Contour Filtering:** Selecting specific contours based on size or characteristics.
- **Visualization:** Displaying the final results with highlighted regions of interest.

Relevant code files: `Task3.ipynb` `utils.py` 
![image](https://github.com/AxelCenteno/FruitAnalysisProject/assets/34460585/72120a47-3064-445d-be7b-79f34462f09a)
