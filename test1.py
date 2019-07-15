import matplotlib.pyplot as plt
import numpy as np

#dpmm - DOts per millimeter
#grating_col - no. of column
#grating)row - no. of row


def gen_1D_grating(dpmm=30, grating_col=10, grating_row=20):
    single_patch_black = [255] * dpmm
    single_patch_white = [0] * dpmm
    single_patch = single_patch_black + single_patch_white
    single_line = single_patch * grating_col
    full_grating = np.array([single_line] * grating_row * dpmm * 2)

    plt.imsave("1d-grating.jpg", full_grating, cmap="Greys")


def gen_2D_grating(dpmm=30, grating_col=10, grating_row=20):
    single_patch_black = [255] * dpmm
    N = len(single_patch_black)
    for i in range(N):
        single_patch_black[i] = int(single_patch_black[i]*np.sin(2*np.pi*0.5*i/N))
    single_patch_white = [0] * dpmm
    single_patch = single_patch_black + single_patch_white
    single_line_v = single_patch * grating_col
    full_grating_v = np.array([single_line_v] * grating_row * dpmm * 2)
    #print(full_grating_v.shape)

    single_line_h = single_patch * grating_row
    full_grating_h = np.array([single_line_h] * grating_col * dpmm * 2).T
    #print(full_grating_h.shape)

    plt.imsave("2d-grating.jpg", full_grating_v | full_grating_h, cmap='Greys')

def main():
    gen_1D_grating(5, 100, 50)
    gen_2D_grating(5, 100, 50)

if __name__ == '__main__':
    main()