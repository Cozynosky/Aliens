import pygame
import os.path
from Aliens import SETTINGS
from enum import Enum


class EasyEnemyBulletState(Enum):
    ALIVE = 0
    DEAD = 1

