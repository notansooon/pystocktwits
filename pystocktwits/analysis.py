
import scipy.special
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
import numpy as np
import scipy
import torch




tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")


def analyze_sentiment(text) ->  tuple[float, float, float, str]:
    """
    Analyze the sentiment of a given text using FinBERT.

    Args:
        text (str): The text to analyze.

    Returns:
        str: The sentiment label ("positive", "negative", or "neutral").
    """
    
    sentiment_labels = ["negative", "neutral", "positive"]
    inputs = tokenizer(text, return_tensors="pt", padding=True, max_length=512
           ) 
    output = model(**inputs)
    logits = output.logits
    
    score = {
           key : value 
           for key, value in  zip(sentiment_labels, scipy.special.softmax(logits.numpy().squeeze()))
           
    }
    
    predicted_label =  max(score, key=score.get)
    return predicted_label

           






