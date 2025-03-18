from enum import Enum, auto

# Enum untuk tipe update counter
class UpdateCounterType(Enum):
  INCREMENT = auto()
  DECREMENT = auto()
  RESET = auto()