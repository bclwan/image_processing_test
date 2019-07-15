import numpy as np
import matplotlib.pyplot as plt
import skimage as si


def filter_Q2_1(arr):
    D0 = arr.shape[0]
    D1 = arr.shape[1]

    for i in range(D0):
        for j in range(D1):
            avg = int
      
            if i == 0:
                if j == 0:
                    avg = (int(arr[0][1]) + int(arr[1][0]))/2
                elif j == (D1-1):
                    avg = (int(arr[0][j-1]) + int(arr[1][j]))/2
                else:
                    avg = (int(arr[0][j-1]) + int(arr[1][j]) + int(arr[0][j+1]))/3
            elif i == (D0-1):
                if j == 0:
                    avg = (int(arr[i][1]) + int(arr[i-1][0]))/2
                elif j == (D1-1):
                    avg = (int(arr[i][j-1]) + int(arr[i-1][j]))/2
                else:
                    avg = (int(arr[i][j-1]) + int(arr[i-1][j]) + int(arr[i][j+1]))/3
            elif j == 0:
                avg = (int(arr[i-1][0]) + int(arr[i+1][0]) + int(arr[i][1]))/3
            elif j == (D1-1):
                avg = (int(arr[i-1][j]) + int(arr[i+1][j]) + int(arr[i][j-1]))/3
            else:
                avg = (int(arr[i-1][j]) + int(arr[i+1][j]) + int(arr[i][j-1]) + int(arr[i][j+1]))/4
        
            if np.abs(arr[i][j] - avg) > 10:
                if (avg>255):
                    arr[i][j] = 255
                else:
                    arr[i][j] = avg
        
    return arr


def map_idx_loc(i, j, idx):
    if idx == 0:
        return i-1, j-1
    elif idx == 1:
        return i, j-1
    elif idx == 2:
        return i+1, j-1
    elif idx == 3:
        return i-1, j
    elif idx == 4:
        return i, j
    elif idx == 5:
        return i+1, j
    elif idx == 6:
        return i-1, j+1
    elif idx == 7:
        return i, j+1
    elif idx == 8:
        return i+1, j+1
    else:
        return i, j
  


def filter_Q2_2(arr):
    D0 = arr.shape[0]
    D1 = arr.shape[1]
  
    for i in range(1, D0-1, 3):
        for j in range(1, D1-1, 3):
            avg = 0      

            avg = ( int(arr[i-1][j-1]) + int(arr[i][j-1]) + int(arr[i+1][j-1]) + 
                    int(arr[i-1][j]) + int(arr[i+1][j]) + 
                    int(arr[i-1][j+1]) + int(arr[i][j+1]) + int(arr[i+1][j+1]))/8

            if np.abs(arr[i][j] - avg) > 10:
                #print(i, j)

                new_avg = 0
                sub_img = {}

                sub_img[0] = arr[i-1][j-1]
                sub_img[1] = arr[i][j-1]
                sub_img[2] = arr[i+1][j-1]

                sub_img[3] = arr[i-1][j]
                sub_img[4] = arr[i][j]
                sub_img[5] = arr[i+1][j]

                sub_img[6] = arr[i-1][j+1]
                sub_img[7] = arr[i][j+1]
                sub_img[8] = arr[i+1][j+1]

                #print(sub_img)

                sorted_img = sorted(sub_img, key=lambda x: sub_img[x])
                #print(sorted_img)

                for k in range(2, 7):
                    #x, y = map_idx_loc(i, j, sorted_img[k])
                    #new_avg += arr[x][y]
                    new_avg += int(sub_img[sorted_img[k]])
            
                new_avg = int(new_avg/5)
                #print(new_avg)

                x, y = map_idx_loc(i, j, sorted_img[0])
                arr[x][y] = new_avg
                x, y = map_idx_loc(i, j, sorted_img[1])
                arr[x][y] = new_avg
                x, y = map_idx_loc(i, j, sorted_img[7])
                arr[x][y] = new_avg
                x, y = map_idx_loc(i, j, sorted_img[8])
                arr[x][y] = new_avg
            
    return arr

def main():
    img = si.util.img_as_ubyte(si.color.rgb2gray(si.io.imread("grayscale.jpg", as_gray=True)))

    noise = img.copy()
    H = noise.shape[0]
    W = noise.shape[1]
    noise_no = 3000

    #Generate noise corrupted image
    for i in range(noise_no):
        x = np.random.randint(0, H)
        y = np.random.randint(0, W)
        noise[x][y] = np.random.randint(0, 255)


    #plt.imshow(img, cmap="gray")
    #plt.show()
    #plt.imshow(noise, cmap="gray")
    #plt.show()

    si.io.imsave("noise_img.jpg", noise)

    filtered_img1 = filter_Q2_1(noise.copy())
    filtered_img2 = filter_Q2_2(noise.copy())

    si.io.imsave("filtered_img1.jpg", filtered_img1)
    si.io.imsave("filtered_img2.jpg", filtered_img2)

    # Evaluation
    noise_MSE = np.sum(np.square(img - noise))/(W*H)
    filter1_MSE = np.sum(np.square(img - filtered_img1))/(W*H)
    filter2_MSE = np.sum(np.square(img - filtered_img2))/(W*H)

    print("Noise MSE", noise_MSE)
    print("Filter1 MSE", filter1_MSE)
    print("Filter2 MSE", filter2_MSE)



if __name__ == '__main__':
    main()