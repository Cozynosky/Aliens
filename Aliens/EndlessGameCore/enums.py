from enum import Enum


class GameState(Enum):
    STARTING = 0
    GAME_ON = 1
    NEXT_WAVE = 2
    GAME_OVER = 3
    GAME_OFF = 4


class UIState(Enum):
    SHOWED = 0
    SHOWING_UP = 1
    HIDE = 2
    HIDING = 3