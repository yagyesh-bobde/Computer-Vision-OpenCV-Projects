# Number Plate Detection
**Task : This is a computer vision problem where we aim to be able to detect number plate from images and webcam.**
**Tools Used : Python and OpenCv

## Approach 
1. I created an instance for the image or frame in case of the webcam program and also initiated the harcascade number plate classifier.
2. I then created a gray scale image of my original image for the classifier 

Then I implemented a for loop which when detects a numper plate, shows text on the image that says "Number Plate" and if it's not found then it shows "Not Found" on the image.  
I also added a "saving" which allows you directly save the number plate that you found as jpeg. (It is stored in the Resources/Scanned/ path)

## Detector-image.py Working Screenshots

## Detector-webcam.py Implementation Video


Resources : 
1. opencv official documentation
2. [!youtube tutorial](https://www.youtube.com/watch?v=WQeoO7MI0Bs&ab_channel=Murtaza%27sWorkshop-RoboticsandAI)
