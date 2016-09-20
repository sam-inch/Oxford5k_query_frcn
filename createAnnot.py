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
    treeFile = file('./fasterXMLTemp.data','r')
    tree = p.load(treeFile)
    print fileNameList
    if not os.path.exists('./VOC2007'):
        os.mkdir('./VOC2007')
    annotationDir = './VOC2007/Annotations'
    if not os.path.exists(annotationDir):
        os.mkdir(annotationDir)
    for i in range(fileNum):
        fileobj = open(os.path.join(parentDir, fileNameList[i]), 'r')
        txtRead = fileobj.read()
        fileobj.close()
#        print txtRead
        # read the building name and the left-up corner right-down corner
        [label, x1, y1, x2, y2] = txtRead.split()
        tempL = label.split('_')
        print tempL
        # get the name of the picture, tempL[0] indicates the database id oxford that we can discard
        print label
        # very dangerous to use : stripPart = label.lstrip(tempL[0] + '_')
        picNameT = label.lstrip(tempL[0]).strip('_')
        picName = picNameT + '.jpg'
        # we also need to read the size of the image because no information indicate in the original annotation file
        img = Image.open(os.path.join(BASE_DIR, 'oxbuild_images', picName))
        width, height = img.size
        print 'width is : ' + str(width)
        print 'height is : ' + str(height)
        '''
            time to create xml
        '''
        # now try to use the imfomation to create the xml gt files
        # locate the node we want to modify
        tree.find('filename').text = picName
        # if want to convert into int str, then-> str(int(float(round(123.1))))
        tree.find('size/width').text = str(width)
        tree.find('size/height').text = str(height)
        tree.find('object/name').text = 'building'
        # we can change every name we want for the class, but here we want to use it for training rpn,so call it building
        tree.find('object/bndbox/xmin').text = x1
        tree.find('object/bndbox/ymin').text = y1
        tree.find('object/bndbox/xmax').text = x2
        tree.find('object/bndbox/ymax').text = y2
        xmlName = os.path.join(annotationDir , (picNameT + '.xml'))
        tree.write(xmlName)
