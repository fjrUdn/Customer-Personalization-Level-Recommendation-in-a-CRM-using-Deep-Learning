try:
  # Import enum
  from enums.activity import ActivityLabel
  from enums.deal import DealStage, MarkedAsDeal

  # Import handler
  from handler.processing import predict_new_data
except ImportError as e:
  print('Error importing configuration and handler:', e)
  print('Please make sure the configuration and handler files are available in the config and handler directories.')
  exit(1)

def get_predicted_label(model, tokenizer, data = None, dummy = False):
  if data is None and dummy:
    # Don't touch this, only for checking the time
    formatted_data = {
      'Deal Name': 'Deal 1',
      'Type Activity': 'TASK',
      'Note': 'Meeting dengan client untuk membahas proyek',
      'Stage': 'NEW'
    }

    # Check if data stage is marked as deal
    if MarkedAsDeal.check_marked_as_deal(formatted_data['Stage']):
      return 'DEAL'

    predicted_label = predict_new_data(formatted_data, model, tokenizer)

    return predicted_label
  elif data is None and not dummy:
    raise ValueError('Data tidak ditemukan, silahkan masukkan data yang ingin diprediksi.')

  # Check if data type is exist in the activity list
  if not ActivityLabel.check_activity(data['type'].upper()):
    raise ValueError(f'Tipe aktivitas "{data["type"]}" tidak valid, pastikan tipe aktivitas adalah salah satu dari: {ActivityLabel.get_activity_list_string()}')

  # if stage had '/' between word for example 'INITIAL MEETING/CALL' then make it 'INITIAL MEETING / CALL'
  if '/' in data['stage']:
    splitted_stage = data['stage'].split('/')
    data['stage'] = ' / '.join([stage.strip() for stage in splitted_stage])

  # Check if data stage is exist in the stage list
  if not DealStage.check_stage(data['stage'].upper()):
    raise ValueError(f'Status deal "{data["stage"]}" tidak valid, pastikan status deal adalah salah satu dari: {DealStage.get_stage_list_string()}')

  formatted_data = {
    'Deal Name': data['name'],
    'Type Activity': data['type'].upper(),
    'Note': data['note'],
    'Stage': data['stage'].upper()
  }

  # Check if data stage is marked as deal
  if MarkedAsDeal.check_marked_as_deal(formatted_data['Stage']):
    return 'DEAL'

  predicted_label = predict_new_data(formatted_data, model, tokenizer)

  return predicted_label