''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
#import Flask, render_template and request from flask package
from flask import Flask, render_template, request
#Import the emotion detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' Function for Emotion detection'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['anger'] is None:
        return "Invalid text! Please try again!"

    return "For the given statement, the system response is \
            \'anger\': "+str(response['anger'])+", \
            \'disgust\': "+str(response['disgust'])+", \
            \'fear\': "+str(response['fear'])+", \
            \'joy\': "+str(response['joy'])+" and \
            \'sadness\': "+str(response['sadness'])+". \
            The dominant emotion is "+str(response['dominant_emotion'])+"."

@app.route("/")
def render_index_page():
    ''' Function for moving to index page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
