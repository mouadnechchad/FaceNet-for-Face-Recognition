# FaceNet-for-Face-Recognition
I have implemented the FaceNet pretrained model for building a face recognition system.

## Dataset
I have collected 5 facial images for each person the system will recognize.

I have split this data into two folders: 

- **Train**: 3 images per person.
- **Test**: 2 images per person.

  Then, I have created a csv file in each folder in order to annotate each image, like:

  - Each person has a label as a number, *ex: I have labeled the first person: 1, the second: 2*
  - The csv files contain only one column where the label of each image is marked in a row respecting the order of images in the current folder.
  - 
Here is the annotation file of test image as example:

![1](https://github.com/mouadnechchad/FaceNet-for-Face-Recognition/assets/92989131/032fa201-877c-4f23-a88b-93a1e4703493)
