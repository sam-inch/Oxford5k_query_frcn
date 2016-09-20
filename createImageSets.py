'''
@author: SAM-ONE
'''
import os
import cPickle as p
import xml.etree.ElementTree as ET
# import cv2 to parse to read the size of the query image
from PIL import Image

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
    # load the template and craete the correct xml file for oxbuild query which have ground truth box
    print fileNameList
    imageSetsDir = './VOC2007/ImageSets/Main'
    if not os.path.exists(imageSetsDir):
        os.makedirs(imageSetsDir)
    for i in range(fileNum):
        fileobj = open(os.path.join(parentDir, fileNameList[i]), 'r')
        txtRead = fileobj.read()
        fileobj.close()
#        print txtRead
        # read the building name and the left-up corner right-down corner
        [label, x1, y1, x2, y2] = txtRead.split()
        tempL = label.split('_')
        # very dangerous to use : stripPart = label.lstrip(tempL[0] + '_')
        picName = label.lstrip(tempL[0]).strip('_') # + '.jpg'
        f = open(os.path.join(imageSetsDir, 'train.txt'), 'a')
        f.write(picName + '\n')
        f.close()
