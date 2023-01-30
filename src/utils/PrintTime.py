
class PrintTime():

    def __init__(self, seconds: int, flush: bool):
        self.seconds = seconds
        self.flush = flush

    def printTime(self):
        if self.seconds >= 3600:
            hours = int(self.seconds // 3600)
            minutes = int((self.seconds % 3600) // 60)
            seconds = int(self.seconds % 60)
            if self.flush:
                print(f"duration: {hours} hour(s) {minutes} minute(s) {seconds} seconds", end='', flush=True)
            else:
                print(f"duration: {hours} hour(s) {minutes} minute(s) {seconds} seconds")
        elif self.seconds >= 60:
            minutes = int(self.seconds // 60)
            seconds = int(self.seconds % 60)
            if self.flush:
                print(f"duration: {minutes} minute(s) {seconds} seconds", end='', flush=True)
            else:
                print(f"duration: {minutes} minute(s) {seconds} seconds")
        else:
            if self.flush:
                print(f"duration: {self.seconds} seconds", end='', flush=True)
            else:
                print(f"duration: {self.seconds} seconds")