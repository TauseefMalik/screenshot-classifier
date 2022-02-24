import sys
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

PREDICTION_KEY = "<PREDICTION-KEY>"
PUBLISH_ITERATION_NAME = "<ITERATION-NAME>"

ENDPOINT = "<PREDICTION-RESOURCE-ENDPOINT>"
PROJECT_NAME = "<CUSTOM-VISION-PROJECT-NAME>"
PROJECT_ID = "<CUSTOM-VISION-PROJECT-ID>"

def predict(img):
    print("Predicting ...")
    try:
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
        predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
        
        with open(img, mode="rb") as test_data:
            results = predictor.classify_image(PROJECT_ID, PUBLISH_ITERATION_NAME, test_data.read())

        probability = 0.0
        probable_tag = ""
        # Display the results.
        for prediction in results.predictions:
            p = prediction.probability * 100
            if p > probability:
                probability = p
                probable_tag = prediction.tag_name
            print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))
        if probability > 60:
            print("Probable category: ", probable_tag)
        else:
            print("Unable to determine category due to low probability score")
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = sys.argv[1]
        if file.endswith((".jpg", ".jpeg", ".png")):
            predict(file)
        else:
            print("Unsupported image file type")

    else:
        print("Provide an image file to predict category")
