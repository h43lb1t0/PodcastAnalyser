import os
import time
from threading import Thread
from .StopWatch import Stopwatch


import whisper


class TransscripePodcast:
    """
        class with amethod to transcripe audio
    """

    def __init__(self, options: dict):
        self.transscript_path: str = options.get('transscript_path')
        self.audio_path: str = options.get('audio_path')
        self.whisper_model: str = options.get('whisper_model')
        self.all_episodes: list = os.listdir(self.audio_path)
        print(self.audio_path)
        
        

    def check_if_folder_exists(self) -> None:
        if (not os.path.exists(self.transscript_path)):
                os.mkdir(self.transscript_path)

    def transscripe(self) -> None: 
        """
            transcribes all episodes of a podcast that are stored in the order defined by 'audio_path'
        """
        print("\n\nstart transcription")

        self.check_if_folder_exists()

        model = whisper.load_model(self.whisper_model)


        # iterates over ech episode transcripe it and save it in an numeric named file
        for i, episode in enumerate(self.all_episodes, start=1):
            
            stopwatch = Stopwatch()
            timer = Thread(target=stopwatch.printTime, args=())
            timer.start()

            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"\ntranscribe Episode {episode} -> no: {i}/{len(self.all_episodes)}\nTime: {current_time}")

            result = model.transcribe(f"{self.audio_path}/{episode}")
            
            with open(f"{self.transscript_path}/episode{i}.txt", 'w') as f:
                    f.writelines(result["text"].lower())
            stopwatch.stop()