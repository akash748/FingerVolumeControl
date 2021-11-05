
# Finger Volume Control

Now control the volume of your laptop with the help of just your finger


## Highlights

This code uses the framework Mediapipe which is developed by Google. They have created these amazing models that allow us to get started with some of the very fundamental AI problems like Hand Detection and Face Detection. The model which we have used on this Hand Tracking which uses two main modules at the backend:

1) Palm Detection
2) Hand Landmark

.

Palm Detection - It works on complete image and provides a cropped image of the Hand.

Hand Detection - This module finds 21 different Landmarks on this cropped image.

To train this module they have annotated 30,000 images manually so the results are quite remarkable.



<p><img align = "centre"  src = "https://github.com/akash748/LinearRegGif/blob/main/handland.png" width = "800" height = "320"/></p>


## Demo


<p><img align = "centre" alt = "gif" src = "https://github.com/akash748/LinearRegGif/blob/main/Volume_Control.gif" width = "800" height = "320"/></p>


## Installation

Download the code and unzip it.
Then install the requirements file using the given code.

```python
pip Install -r requirements.txt
```

   Now run the VolumeHandControl.py file 
## References

 - [Mediapipe](https://google.github.io/mediapipe/solutions/hands)


