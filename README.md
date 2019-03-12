## Datasets

Link to the training dataset : https://drive.google.com/open?id=1trcGo5kQCG51j37ndBKW83bp2Alm3DdJ

Link to the CKPT dataset : https://drive.google.com/open?id=1efDRUaNzTFCTKtyauD54TshD3uauUaWg

Link to the testing dataset : https://drive.google.com/open?id=1HoosvBb-RB10GriJ-CpvSIJDupeZPRFY

Link to the testing dataset results : https://drive.google.com/open?id=17jnRslKYYKdotCPh4DkCrSIYjmrzrgUK


## Tech
  - Qwant Image Search API
  - YOLO Object detection tool
  - MongoDB
  - Tensorflow library
  - Open-cv library
  

## Approach
  - Retrieved the images through qwant image search API and stored the urls of the images directly in MongoDB
  - 500 images for Narendra Modi and 500 for Arvind Kejriwal were retrieved
  - 100 images (50-50) are sent to the testing dataset and rest to the training dataset
  - Annotated the data manually and also developed the rectangular box around the faces
  - Trained the model using YOLO object detection tool
  - Developed Results for the testing dataset
