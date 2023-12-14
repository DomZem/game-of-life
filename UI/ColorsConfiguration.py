import threading

class ColorsConfiguration():
    __instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
                cls.__instance.white = (255, 255, 255)
                cls.__instance.black = (0, 0, 0)
                cls.__instance.gray = (128, 128, 128)
                cls.__instance.green = (0, 255, 0)
            # lock released automatically
            return cls.__instance

