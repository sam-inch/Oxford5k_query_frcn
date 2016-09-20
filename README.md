### Disclaimer

The codes are used to create three documents for faster rcnn training. It transfer the query information of ground-truth box from oxford5k dataset. The code is written by Sam Weng.

# Trans *Oxford5k dataset* for Faster R-CNN

## About the python files
The original gt file for Oxford5k indicates the gt boxes only for query images. The code can automatically read the original information from ft files and images.

Three python files are included:
> The usage of files are indicated by their names

+ createAnnot.py
+ crateImageSets.py
+ createJPEG.py

## running environment
You need to change the directory which containing the oxford database.

The structure of directory should be like this:
	```

	$BASE_DIR/

	$BASE_DIR/oxbuild_gt

	$BASE_DIR/oxbuild_images

  	```
