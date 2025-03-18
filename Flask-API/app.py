try:
  import os

  # Disable tensorflow one dnn warning
  os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

  # Disable tensorflow warning
  os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
except ImportError as e:
  print('Error importing libraries:', e)
  print('Please install the required libraries using "pip install -r requirements.txt"')
  exit(1)

try:
  import time
  import nltk
  import joblib
  import numpy as np
  import tensorflow as tf

  from flask import Flask, request, json
except ImportError as e:
  print('Error importing libraries:', e)
  print('Please install the required libraries using "pip install -r requirements.txt"')
  exit(1)

try:
  nltk.download('punkt')
  nltk.download('stopwords')
except Exception as e:
  print('Error downloading NLTK data:', e)
  print('Please check your internet connection and try again.')
  exit(1)

try:
  # Import configuration
  import config.app as app_config
  import config.model as model_config
  import config.endpoint as endpoint_config

  # Import enum
  from enums.deal import DealStage
  from enums.label import LabelMapping
  from enums.activity import ActivityLabel

  # Import helper
  from helpers.validation import validate_payload
  from helpers.predict_label import get_predicted_label
except ImportError as e:
  print('Error importing configuration and handler:', e)
  print('Please make sure the configuration and handler files are available in the config and handler directories.')
  exit(1)

# Inisialisasi Flask app
app = Flask(__name__)

# Set root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

try:
  # Load model dan tokenizer
  model = tf.keras.models.load_model(os.path.join(ROOT_DIR, model_config.MODEL_FILE_NAME))
  tokenizer = joblib.load(os.path.join(ROOT_DIR, model_config.TOKENIZER_FILE_NAME))
except Exception as e:
  print('Error loading model and tokenizer:', e)
  print('Please make sure the model and tokenizer files are available in the models directory.')
  exit(1)

def response_json(message, status_code = 200):
  return app.response_class(
    status=status_code,
    response=json.dumps(message),
    mimetype='application/json'
  )

# Endpoint untuk prediksi
@app.route(endpoint_config.PREDICT_ENDPOINT, methods=['POST'])
def predict():
  # Check if request is not json
  if request.is_json == False: return response_json({
    'status': 'error',
    'error': 'request tidak valid, pastikan request dalam bentuk JSON.'
  }, 400)

  # Convert request to json
  data = request.get_json(force=False, silent=False)

  # Check if data is empty
  if data is None: return response_json({
    'status': 'error',
    'error': 'request tidak valid, silahkan masukkan data dalam bentuk JSON.'
  }, 400)

  # handle if data is array
  if not isinstance(data, list):
    # Check if the request is valid
    if not validate_payload(data): return response_json({
      'status': 'error',
      'error': 'request tidak valid, pastikan data memiliki kata kunci name, type, note, dan stage'
    }, 400)

    try:
      # Get predicted label
      predicted_label = get_predicted_label(model, tokenizer, data)

      return response_json({
        'status': 'success',
        'message': 'Prediksi label deal berhasil.',
        'data': {
          'name': data['name'],
          'type': data['type'],
          'note': data['note'],
          'stage': data['stage'],
          'predicted_label': predicted_label
        }
      })
    except Exception as e:
      return response_json({
        'status': 'error',
        'error': f'Gagal melakukan prediksi label deal: {str(e)}'
      }, 500)
  elif isinstance(data, list):
    result = []

    for idx, item in enumerate(data):
      # Check if the request is valid
      if not validate_payload(item): return response_json({
        'status': 'error',
        'error': f'request tidak valid, pastikan data pada index {str(idx)} memiliki kata kunci name, type, note, dan stage'
      }, 400)

      try:
        # Get predicted label
        predicted_label = get_predicted_label(model, tokenizer, item)

        result.append({
          'name': item['name'],
          'type': item['type'],
          'note': item['note'],
          'stage': item['stage'],
          'predicted_label': predicted_label
        })
      except Exception as e:
        return response_json({
          'status': 'error',
          'error': f'Gagal melakukan prediksi label deal pada index {str(idx)}: {str(e)}'
        }, 500)

    return response_json({
      'status': 'success',
      'message': 'Prediksi label deal berhasil.',
      'data': result
    })
  else:
    return response_json({
      'status': 'error',
      'error': 'request tidak valid, pastikan data dalam bentuk JSON.'
    }, 400)

# Endpoint untuk mencetak list apa saja allowed activity type
@app.route(endpoint_config.PREDICT_ENDPOINT + '/type', methods=['GET'])
def allowed_type():
  activity_types = [activity_type.value for activity_type in ActivityLabel]

  return response_json({
    'status': 'success',
    'message': 'Berikut adalah list tipe aktivitas yang diperbolehkan.',
    'data': activity_types
  })

# Endpoint untuk mencetak list apa saja allowed deal stage
@app.route(endpoint_config.PREDICT_ENDPOINT + '/stage', methods=['GET'])
def allowed_stage():
  stage_list = [deal.value for deal in DealStage]

  return response_json({
    'status': 'success',
    'message': 'Berikut adalah list status deal yang diperbolehkan.',
    'data': stage_list
  })

# Endpoint untuk mengecek berapa lama proses dalam melakukan prediksi
@app.route(endpoint_config.PREDICT_ENDPOINT + '/time', methods=['GET'])
def predict_time():
  result = []
  rand = np.random.randint(5, 10)

  try:
    for _ in range(rand):
      # Start timer
      start_time = time.time()

      # Panggil fungsi prediksi label deal
      get_predicted_label(model, tokenizer, None, True)

      # Hitung waktu yang diperlukan
      end_time = time.time()
      elapsed_time = end_time - start_time

      # Simpan waktu yang diperlukan
      result.append(elapsed_time)

    total_time = sum(result)

    return response_json({
      'status': 'success',
      'message': 'Prediksi label deal berhasil.',
      'data': {
        'total_test': rand,
        'total_time': f'{round(total_time, 3)} detik',
        'average_time': f'{round(total_time / rand, 3)} detik'
      }
    })
  except Exception as e:
    return response_json({
      'status': 'error',
      'error': f'Gagal melakukan prediksi label deal: {str(e)}'
    }, 500)

# Endpoint untuk status server
@app.route('/status', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def status():
  return response_json({
    'status': 'success',
    'message': 'Server is running.',
    'version': app_config.APP_VERSION,
    'status': {
      'model': 'loaded' if model is not None else 'something went wrong when loading the model',
      'tokenizer': 'loaded' if tokenizer is not None else 'something went wrong when loading the tokenizer'
    },
    'data': {
      'model': model_config.MODEL_METHOD,
      'tokenizer': model_config.TOKENIZER_METHOD,
      'max_sequence_length': model_config.MAX_SEQUENCE_LENGTH,
      # loop from ActivityLabel enum and get the value
      'activity_weights': {activity_type.name: activity_type.value for activity_type in ActivityLabel},
      'label_mapping': {label.name: label.value for label in LabelMapping},
    }
  })

# Make wildcard route
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@app.route('/<path:path>')
def catch_all(path):
  # cek jika path kosong
  if path == '': return response_json({
    'status': 'success',
    'message': f'selamat datang di API prediksi label deal, silahkan gunakan {endpoint_config.PREDICT_ENDPOINT} dengan metode POST untuk melakukan prediksi label deal.'
  })

  if f"/{path}" == endpoint_config.PREDICT_ENDPOINT and not request.method == 'POST': return response_json({
    'status': 'error',
    'error': f'endpoint {endpoint_config.PREDICT_ENDPOINT} hanya dapat digunakan menggunakan method POST, silahkan ganti method request anda.'
  }, 405)

  return response_json({
    'status': 'error',
    'error': f'Endpoint /{path} tidak ditemukan, pastikan method dan endpoint sesuai.'
  }, 404)

if __name__ == '__main__':
  try:
    # Run Flask app
    if app_config.APP_DEBUG: app.run(debug=app_config.APP_DEBUG, host=app_config.APP_HOST, port=app_config.APP_PORT)
    else:
      try:
        from waitress import serve
      except ImportError as e:
        print('Error importing libraries:', e)
        print('Please install the required libraries using "pip install -r requirements.txt"')
        exit(1)

      print(f'Running server in production mode on http://{app_config.APP_HOST}:{app_config.APP_PORT}')
      serve(app, host=app_config.APP_HOST, port=app_config.APP_PORT)
  except:
    print('Shutting down the server...')
    exit(0)
