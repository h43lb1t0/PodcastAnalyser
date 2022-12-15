import whisper
import string
import time
import os


class Analyse():

    def __init__(self, options={}):

        self.trancripe = True
        self.transscript_path = "transscripte"
        self.audio_path = "podcast"
        self.whisper_model = "medium"

        self.trancripe = options.get('trancripe', self.trancripe)
        self.transscript_path = options.get('transscript_path', self.transscript_path)
        self.audio_path = options.get('audio_path', self.audio_path)
        self.whisper_model = options.get('whisper_model',self.whisper_model)

        self.filterlists = os.listdir("filterlists")

        self.woerter_in_folge = []
        self.unique_words_count = []
        self.woerter_liste = []
        self.all_episodes = os.listdir(self.audio_path)

    def transcripe_all_epsisodes_of_podcast(self):
        if self.trancripe:
            print("\nstart transcription")


            model = whisper.load_model("tiny")

            if (not os.path.exists(self.transscript_path)):
                os.mkdir(self.transscript_path)

            for i, episode in enumerate(self.all_episodes):
                i+= 1

                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n\ntranscribe folge {i}.wav\nTime: {current_time}\n")

                result = model.transcribe(f"{self.audio_path}/{i}.wav")

                with open(f"{self.transscript_path}/Episode{i}test.txt", 'w') as f:
                    f.writelines(result["text"].lower())

            print("transcribe finished")
        else:
            print("skipped transcribing")


    
    def extrahiere_woerter(self, dateiname='AlleEpisoden.txt'):
        for episode_no in range(1,10):
            with open(f"transscripte/Episode{episode_no}.txt", "r") as f:
                text = f.read()
                text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
                woerter_liste_tmp = text.split()
                for word in woerter_liste_tmp:
                    self.woerter_liste.append(word)
        



    def filter_for_words(self):
        for filterlist in self.filterlists:
            with open(f"filterlists/{filterlist}", 'r') as file:
                zeilen = file.readlines()
                for wort in self.woerter_liste:
                    for zeile in zeilen:
                        if zeile.strip()  == wort.strip():
                            self.woerter_in_folge.append(wort.lower().strip())



    def create_unique_word_list(self):
        unique_words = set(self.woerter_in_folge)
        self.unique_words_list = list(unique_words)

    
    def count_occurance_of_words(self):
        for wort in self.unique_words_list:
            count = self.woerter_liste.count(wort.strip())
            self.unique_words_count.append((wort.strip(), count))
        
    def analyze(self):
        self.transcripe_all_epsisodes_of_podcast()
        self.extrahiere_woerter()
        self.filter_for_words()
        self.create_unique_word_list()
        self.count_occurance_of_words()



