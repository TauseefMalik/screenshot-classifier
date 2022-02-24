# screenshot-classifier
Classify your screenshots into a category and de-clutter your gallery using Azure powered AI

Ever taken a screenshot of an important transaction to share with your friend? Or maybe to capture an important map, articles, invoice, medical report, funny meme, or a conversation. Be it anything, eventually, after a while, we tend to forget to remove these images from our phones and as they gather dust and clutter our gallery, they also become dangerous weapons when in the wrong hands.

It's always a good to categorise the images in your gallery and delete what is unncessary. Our main objective in this app, will be to train a model that can identify personally identifiable information(PII) data from rest of the clutter and then use our console application to predict the image category for our convenience.

Pre-requisites -

You will need an azure account to setup a Azure custom vision project.
Train sample data of image with tags of major categories that you observe in your gallery e.g. food, nature, bills, conversations etc.

Required packages -

`pip install azure.cognitiveservices.vision.customvision.prediction`

Execution -

![sample-prediction-output](https://github.com/TauseefMalik/screenshot-classifier/blob/main/unsample-data-prediction-2.PNG)



Note - you are free to modify the code to read entire directory of images and categorise all of them or use a library to change file attributes to add most probable tag.
