import cv2
import numpy as np
import os
import csv

def partA():
    list = ['bird.jpg', 'cat.jpg', 'flowers.jpg','horse.jpg']
    data=[]
    for i in list:
        pathv=os.path.join( os.getcwd(), '../Images', i )
        img = cv2.imread(pathv)
        height,width,Channels = img.shape
        centralpx=img[height//2,width//2]
        #print (type(i))
        #print (height)
        #print (width)
        #print(Channels)
        E,F,G = centralpx
        #data.append(i++str(height)+","+str(width)+","+str(Channels)+","+str(E)+","+str(F)+","+str(G))
        temp=[]
        temp.append(i)
        temp.append(height)
        temp.append(width)
        temp.append(Channels)
        temp.append(E)
        temp.append(F)
        temp.append(G)
        data.append(temp)
        #print(data)
        #print (type(data))
    with open('../Generated/stats.csv','a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)
    csvFile.close()


def partB():
    pathv=os.path.join( os.getcwd(), '../Images', "cat.jpg" )
    img = cv2.imread(pathv)
    b = img.copy()
    # set green and red channels to 0
    b[:, :, 0] = 0
    b[:, :, 1] = 0
    cv2.imwrite('../Generated/cat_red.jpg',b)

def partC():
    pathv=os.path.join( os.getcwd(), '../Images', "flowers.jpg" )
    b = cv2.imread(pathv)
    img = b.copy()
    b_channel, g_channel, r_channel = cv2.split(img)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 
    img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    cv2.imwrite('../Generated/flowers_alpha.jpg',img)


def partD():
    pathv=os.path.join( os.getcwd(), '../Images', "horse.jpg" )
    b = cv2.imread(pathv)
    img = rgb2gray(b);
    cv2.imwrite('../Generated/horse_gray.jpg',img)

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.3 * r + 0.59 * g + 0.11 * b

    return gray
partA()
partB()
partC()
partD()
