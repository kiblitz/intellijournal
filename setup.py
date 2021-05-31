import src.sentiment_analysis
import src.keyword_extraction

if __name__ == '__main__':
  src.sentiment_analysis.load_en_sentiment_classifier()
  src.keyword_extraction.load_keyword_extractor()
