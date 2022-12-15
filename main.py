import whisper
import string
import pprint
import torch
import time


class Analyse:

    def __init__(self):
        self.woerter = None
        self.woerter_in_folge = []
        self.unique_words_count = []


    def transcripe_podcast(output_file_name="AlleEpisoden.txt", do=True):
        if do:
            print("\nstart transcription")

            DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

            model = whisper.load_model("medium", device=DEVICE)
            options = {"language": "de"}

            for i in range(1,10):

                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n\ntranscribe folge {i}.wav\nTime: {current_time}\n")

                result = model.transcribe(f"{i}.wav")
                with open(f"transscripte/Episode{i}.txt", 'w') as f:
                    f.writelines(result["text"].lower())

            print("transcribe finished")
        else:
            print("skipped transcribing")

    #transcripe_podcast(do=False)

    
    def extrahiere_woerter(self, dateiname='AlleEpisoden.txt'):
        with open(dateiname, "r") as f:
            text = f.read()
            text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
            self.woerter_liste = text.split()
        



    

    def find_insults(self):
        with open('insults.txt', 'r') as file:
            zeilen = file.readlines()
            for wort in self.woerter_liste:
                for zeile in zeilen:
                    if zeile.strip()  == wort.strip():
                        self.woerter_in_folge.append(wort.lower().strip())

    def find_schimpfwoerter(self):
        with open('schimpfwoerter.txt', 'r') as file:
            zeilen = file.readlines()
            for wort in self.woerter_liste:
                for zeile in zeilen:
                    if zeile.strip()  == wort.strip() :
                        self.woerter_in_folge.append(wort.lower().strip())




    def create_unique_word_list(self):
        unique_words = set(self.woerter_in_folge)
        self.unique_words_list = list(unique_words)

    
    def count_occurance_of_words(self):
        for wort in self.unique_words_list:
            count = self.woerter_liste.count(wort.strip())
            self.unique_words_count.append((wort.strip(), count))
        

    


hobbylos = Analyse()
hobbylos.transcripe_podcast()
""" hobbylos.extrahiere_woerter()
hobbylos.find_insults()
hobbylos.find_schimpfwoerter()
hobbylos.create_unique_word_list()
hobbylos.count_occurance_of_words()
print(hobbylos.unique_words_count) """
