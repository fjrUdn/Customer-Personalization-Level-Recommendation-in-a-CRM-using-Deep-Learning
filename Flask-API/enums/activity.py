from enum import Enum

# Enum untuk label aktivitas
class ActivityLabel(Enum):
  TASK = 'TASK'
  CALL = 'CALL'
  DEADLINE = 'DEADLINE'
  EMAIL = 'EMAIL'
  MEETING = 'MEETING'

  @staticmethod
  def get_activity_list():
    return [activity.value for activity in ActivityLabel]

  @staticmethod
  def get_activity_list_string():
    return ', '.join([f'"{activity.value}"' for activity in ActivityLabel])

  @staticmethod
  def check_activity(activity):
    return activity in ActivityLabel.get_activity_list()

# Enum untuk bobot aktivitas
class ActivityWeight(Enum):
  TASK = 1
  CALL = 2
  DEADLINE = 1
  EMAIL = 1
  MEETING = 3
