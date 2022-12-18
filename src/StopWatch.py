import time

class Stopwatch():
    """
        indicates the duration that a function/class is already running in seconds
    """
    def __init__(self):
        self.i = 1
        self.run = True
    
    def printTime(self) -> None:
        """
            do the printing
        """
        time.sleep(1)
        while self.run:
            print(f"duration: {self.i}", end=' sec', flush=True)
            time.sleep(1)
            print('\r    \r', end='', flush=True)
            self.i += 1

    def stop(self) -> None:
        """
            stop counting the time
        """
        self.run = False
        print("")
