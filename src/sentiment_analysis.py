import flair

classifier = None

def load_en_sentiment_classifier():
  global classifier
  classifier = flair.models.TextClassifier.load('en-sentiment')

def get_sentiment_label(text):
  if not classifier:
    load_en_sentiment_classifier()
  sentence = flair.data.Sentence(text)
  classifier.predict(sentence)
  if sentence.labels:
    return sentence.labels[0] 
  return None
