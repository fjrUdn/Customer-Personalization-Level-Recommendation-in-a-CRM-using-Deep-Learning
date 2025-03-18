try:
  import re
  import numpy as np
  import pandas as pd

  from nltk.corpus import stopwords
  from nltk.tokenize import word_tokenize
  from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
  from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
except ImportError as e:
  print('Error importing libraries:', e)
  print('Please install the required libraries using "pip install -r requirements.txt"')
  exit(1)

try:
  # Import configuration
  import config.model as model_config

  # Import enum
  from enums.label import LabelMapping
  from enums.activity import ActivityWeight
except ImportError as e:
  print('Error importing configuration and handler:', e)
  print('Please make sure the configuration and handler files are available in the config and handler directories.')
  exit(1)

def preprocess_text(text):
  factory = StemmerFactory()
  stemmer = factory.create_stemmer()
  stop_words = set(stopwords.words(model_config.STOP_WORDS_LANG))

  text = str(text)
  text = re.sub(r"\d+", " ", text)
  text = text.lower()
  text = re.sub(r"\n", " ", text)
  text = re.sub(r"[^\w\s]", " ", text)
  tokens = word_tokenize(text)
  tokens = [word for word in tokens if word not in stop_words]
  tokens = [stemmer.stem(word) for word in tokens]

  return " ".join(tokens)

def calculate_activity_score(activity_type):
  return ActivityWeight[activity_type].value

def preprocess_new_data(new_data):
  new_df = pd.DataFrame([new_data])
  new_df.fillna({"Note": ""}, inplace=True)

  # Apply text preprocessing to the "Note" column
  new_df["Note"] = new_df["Note"].apply(preprocess_text)

  # Calculate activity scores
  new_df["Activity Score"] = new_df["Type Activity"].apply(calculate_activity_score)

  return new_df

def extract_new_features(new_df, tokenizer):
  # Tokenisasi dan padding
  sequences = tokenizer.texts_to_sequences(new_df['Note'])
  padded_sequences = pad_sequences(sequences, maxlen=model_config.MAX_SEQUENCE_LENGTH)

  X_new = np.hstack((new_df[['Activity Score']].values, padded_sequences))
  return X_new

def calculate_label_mapping(prediction):
  return LabelMapping(prediction).name

def predict_new_data(new_data, model, tokenizer):
  new_df = preprocess_new_data(new_data)
  X_new = extract_new_features(new_df, tokenizer)

  y_pred = model.predict(X_new)
  y_pred_class = np.argmax(y_pred, axis=1)

  predicted_label = calculate_label_mapping(y_pred_class[0])

  return predicted_label
