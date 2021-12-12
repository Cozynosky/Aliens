import pygame
import json


class Settings:
    RESOLUTIONS = {
        "1152 x 648": {"width": 1152, "height": 648},
        "1280 x 720": {"width": 1280, "height": 720},
        "1366 x 768": {"width": 1366, "height": 768},
        "1600 x 900": {"width": 1920, "height": 1080},
        "1920 x 1080": {"width": 1920, "height": 1080},
        "2560 x 1440": {"width": 2560, "height": 1440}
    }

    def __init__(self):
        pygame.init()
        #
        self.hardware_resolution = self.check_hardware_res()
        # load default_settings
        self.default_settings = {
            "window": {
                "native": {
                    "resolution": (self.RESOLUTIONS["1920 x 1080"]["width"], self.RESOLUTIONS["1920 x 1080"]["height"]),
                    "width": self.RESOLUTIONS["1920 x 1080"]["width"],
                    "height": self.RESOLUTIONS["1920 x 1080"]["height"],
                },
                "user": {
                    "resolution": (self.hardware_resolution["width"], self.hardware_resolution["height"]),
                    "width": self.hardware_resolution["width"],
                    "height": self.hardware_resolution["height"],
                },
                "hardware": {
                    "resolution": (self.hardware_resolution["width"], self.hardware_resolution["height"]),
                    "width": self.hardware_resolution["width"],
                    "height": self.hardware_resolution["height"],
                },
                "fullscreen": True,
                "title": "Aliens!"
            }
        }
        settings_dict = self.load_settings()
        # native resolution that game is designed for
        self.NATIVE_WINDOW_SIZE = settings_dict["window"]["native"]["resolution"]
        self.NATIVE_WINDOW_WIDTH = settings_dict["window"]["native"]["width"]
        self.NATIVE_WINDOW_HEIGHT = settings_dict["window"]["native"]["height"]
        # current window size
        self.WINDOW_SIZE = settings_dict["window"]["user"]["resolution"]
        self.WINDOW_WIDTH = settings_dict["window"]["user"]["width"]
        self.WINDOW_HEIGHT = settings_dict["window"]["user"]["height"]
        # user screen data
        self.HARDWARE_WINDOW_SIZE = settings_dict["window"]["hardware"]["resolution"]
        self.HARDWARE_WINDOW_WIDTH = settings_dict["window"]["hardware"]["width"]
        self.HARDWARE_WINDOW_HEIGHT = settings_dict["window"]["hardware"]["height"]
        # fullscren and scale for changing res
        self.FULLSCREEN = settings_dict["window"]["fullscreen"]
        self.SCALE = self.prepare_scale()
        # window title
        self.WINDOW_TITLE = settings_dict["window"]["title"]

    def check_hardware_res(self):
        display_info = pygame.display.Info()
        res = f"{display_info.current_w} x {display_info.current_h}"

        if res in self.RESOLUTIONS.keys():
            return self.RESOLUTIONS[res]

        else:
            return self.RESOLUTIONS["1280 x 720"]

    def load_settings(self):
        try:
            with open("Data/settings.json", "r") as j:
                return json.load(j)
        except (FileNotFoundError, IOError):
            return self.default_settings

    def prepare_scale(self):
        if self.WINDOW_WIDTH < self.NATIVE_WINDOW_WIDTH:
            return self.WINDOW_WIDTH / self.NATIVE_WINDOW_WIDTH
        else:
            return self.NATIVE_WINDOW_WIDTH / self.WINDOW_WIDTH

    def save_settings(self):
        settings = {
            "window": {
                "native": {
                    "resolution": self.RESOLUTIONS["1920 x 1080"],
                    "width": 1920,
                    "height": 1080,
                },
                "user": {
                    "resolution": self.WINDOW_SIZE,
                    "width": self.WINDOW_WIDTH,
                    "height": self.WINDOW_HEIGHT,
                },
                "hardware": {
                    "resolution": self.HARDWARE_WINDOW_SIZE,
                    "width": self.HARDWARE_WINDOW_WIDTH,
                    "height": self.HARDWARE_WINDOW_HEIGHT,
                },
                "fullscreen": self.FULLSCREEN,
                "title": self.WINDOW_TITLE
            }
        }
        with open("Data/settings.json", "w") as file:
            json.dump(settings, file)
