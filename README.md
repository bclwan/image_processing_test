# image_processing_test
Demo of grating generation and noise filtering


# Environment
OS: Ubuntu

Language: Python

Library:  scikit-image
          matplotlib
          numpy

# Code Introduction

## Test 1 

Code test1.py

This code contain two functions which generate 1d or 2d grating.

Control Parameters include dots per millimeter, columns and rows for the grating images


Samples:

Settings:(dpmm=5, grating_col=100, grating_row=50)

1D :
![1D](../master/doc/images/1d-grating.jpg)

2D:
![2D](../master/doc/images/2d-grating.jpg)


## Test 2

Code test2.py

This program implement 2 filters and compare their performance on noise filtering.


Comparison

Original Image
![sample](../master/doc/images/grayscale.jpg)

Noise Image
![noise](../master/doc/images/noise_img.jpg)

Filter1
![fil1](../master/doc/images/filtered_img1.jpg)

Filter2
![fil2](../master/doc/images/filtered_img2.jpg)


### Discussion
Filter1 evaluate the noise with respect to only 4 surrounding pixels. The memory access cost is low but it doesn't compare all surrounding pixels to make just filtering decision.

Filter2 compare all pixels around so from the samples above it can filter better than Filter1. Moreover, by using the mean-square-error method to evaluate the 2 filters performance, Filter2 has got a better score over Filter1. However, memory access cost is higher.

