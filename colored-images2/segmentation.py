import cv2
import numpy as np
 
img = cv2.imread('chips.png')

def masked_objects(img, ref, radius):
    imgc = img.copy()
    
    rmean = []
    gmean = []
    bmean = []
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            px = img[i,j,:]
            
            d = np.sqrt((px[0]-ref[0])**2 + (px[1]-ref[1])**2 + (px[2]-ref[2])**2)
            
            if d > radius:
                imgc[i,j,:] = [0,0,0]
                
            else:
                bmean.append(px[0])
                gmean.append(px[1])
                rmean.append(px[2])
                
    
    print('mean of the color segmented:')
    print("{}, {}, {}".format(np.mean(bmean), np.mean(gmean), np.mean(rmean)))
    return imgc

cv2.imshow("img", img)

blue = masked_objects(img, [249.82132471728593, 71.70080775444265, 2.2651050080775446], 30)
red =  masked_objects(img, [37.6701819140522, 21.504481940416557, 233.90825204323755], 36)
green =  masked_objects(img, [93.8636416251881, 164.18694293320985, 16.414515568931588], 60)
yellow =  masked_objects(img, [25.413721079691516, 251.0167095115681, 251.79305912596402], 45)
orange =  masked_objects(img, [16.362261380323055, 63.91013215859032, 253.00778267254037], 40)


cv2.imshow('blue', blue)
cv2.imshow('red', red)
cv2.imshow('green', green)
cv2.imshow('yellow', yellow)
cv2.imshow('orange', orange)

cv2.waitKey()
cv2.destroyAllWindows()