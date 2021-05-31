import keybert

extractor = None

def load_keyword_extractor():
  global extractor
  extractor = keybert.KeyBERT('distilbert-base-nli-mean-tokens')

def get_keywords(text, n=5, stop='english', kw_range=(1, 1), diversity=0.5):
  if not extractor:
    load_keyword_extractor()
  return extractor.extract_keywords(text,
                                    keyphrase_ngram_range=kw_range,
                                    top_n=n,
                                    stop_words=stop,
                                    use_mmr=True,
                                    diversity=diversity)
