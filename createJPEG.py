'''
@author: SAM-ONE
'''
import os
import cPickle as p
# import cv2 to parse to read the size of the query image
from PIL import Image
import shutil

BASE_DIR = $PATH_BASE

def fileFilter(directory = os.path.join(BASE_DIR, 'oxbuild_gt')):
    # scan the file in the specific directory and filter split
    fileNeed = []
    filelist = os.listdir(directory)
    for filename in filelist:
        portion = os.path.splitext(filename)
        prefixSplit = portion[0].split('_')
        if prefixSplit[-1] == 'query':
            fileNeed.append(filename)
    return(len(fileNeed), fileNeed, directory)

if __name__ == '__main__':
    fileNum, fileNameList, parentDir = fileFilter()
    if not os.path.exists('./VOC2007'):
        os.mkdir('./VOC2007')
    jpegDir = './VOC2007/JPEGImages'
    if not os.path.exists(jpegDir):
        os.mkdir(jpegDir)
    for i in range(fileNum):
        fileobj = open(os.path.join(parentDir, fileNameList[i]), 'r')
        txtRead = fileobj.read()
        fileobj.close()
#        print txtRead
        # read the building name and the left-up corner right-down corner
        [label, x1, y1, x2, y2] = txtRead.split()
        tempL = label.split('_')
        # get the name of the picture, tempL[0] indicates the database id oxford that we can discard
        # very dangerous to use : stripPart = label.lstrip(tempL[0] + '_')
        picName = label.lstrip(tempL[0]).strip('_') + '.jpg'
        # we nedd the name of the training image with bnd box
        # shutil.copyfile(os.path.join(BASE_DIR, 'oxbuild_images', picName),os.path.join(BASE_DIR, '2007/JPEGImages', picName))
        print os.path.join(BASE_DIR, 'oxbuild_images', picName)
        print os.path.join(jpegDir, picName)
        shutil.copyfile(os.path.join(BASE_DIR, 'oxbuild_images', picName), os.path.join(jpegDir, picName))
