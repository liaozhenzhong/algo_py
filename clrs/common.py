import enum
import math

class Color(enum.Enum):
    WHITE = enum.auto()
    GRAY = enum.auto()
    BLACK = enum.auto()

class Node(object):
    def __init__(self, key, value=None):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.color = Color.WHITE
        self.start_time = 0
        self.end_time = 0
        self.rank = 0
