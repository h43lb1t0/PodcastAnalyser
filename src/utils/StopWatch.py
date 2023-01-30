import time

import src.utils.PrintTime as pt

class Stopwatch():
    """
        indicates the duration that a function/class is already running in seconds/minutes
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
            pt.PrintTime(self.i, True).printTime()
            
            time.sleep(1)
            print('\r    \r', end='', flush=True)
            self.i += 1

    def getEndTime(self) -> int:
        """
            get the time in seconds that at the time of calling the function has elapsed

        Returns:
            int: time elapsed
        """
        return self.i
        
    def stop(self) -> None:
        """
            stop counting the time
        """
        self.run = False
        print("")
