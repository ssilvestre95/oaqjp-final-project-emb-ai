from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)