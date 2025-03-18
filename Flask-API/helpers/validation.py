def validate_payload(data):
  required_keys = ['name', 'type', 'note', 'stage']

  for key in required_keys:
    if key not in data:
      return False

  return True
