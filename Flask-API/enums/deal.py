from enum import Enum

# Enum untuk list stage
class DealStage(Enum):
  NEW = 'NEW'
  INITIAL_MEETING = 'INITIAL MEETING'
  CALL = 'CALL'
  INITIAL_MEETING_OR_CALL = 'INITIAL MEETING / CALL'
  QUOTATION = 'QUOTATION'
  NEGOTIATION = 'NEGOTIATION'
  DEAL = 'DEAL'
  PAID = 'PAID'
  PAYMENT_IN_PROGRESS = 'PAYMENT IN PROGRESS'

  @staticmethod
  def get_stage_list():
    return [deal.value for deal in DealStage]

  @staticmethod
  def get_stage_list_string():
    return ', '.join([f'"{deal.value}"' for deal in DealStage])

  @staticmethod
  def check_stage(stage):
    return stage in DealStage.get_stage_list()

# Enum untuk list stage yang di mark as deal
class MarkedAsDeal(Enum):
  DEAL = 'DEAL'
  PAID = 'PAID'
  PAYMENT_IN_PROGRESS = 'PAYMENT IN PROGRESS'

  @staticmethod
  def get_marked_as_deal_list():
    return [deal.value for deal in MarkedAsDeal]

  @staticmethod
  def get_marked_as_deal_list_string():
    return ', '.join([f'"{deal.value}"' for deal in MarkedAsDeal])

  @staticmethod
  def check_marked_as_deal(stage):
    return stage in MarkedAsDeal.get_marked_as_deal_list()
