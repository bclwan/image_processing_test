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

2D:


## Test 2

Code test2.py

This program implement 2 filters and compare their performance on noise filtering.


Comparison

Original Image

Noise Image

Filter1

Filter2


### Discussion
Filter1 evaluate the noise with respect to only 4 surrounding pixels. The memory access cost is low but it doesn't compare all surrounding pixels to make just filtering decision.

Filter2 compare all pixels around so from the samples above it can filter better than Filter1. Moreover, by using the mean-square-error method to evaluate the 2 filters performance, Filter2 has got a better score over Filter1. However, memory access cost is higher.

