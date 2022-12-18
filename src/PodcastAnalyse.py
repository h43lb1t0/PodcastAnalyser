import os
import shutil
import string
import time
from threading import Thread

import whisper

from .TransscripePodcast import TransscripePodcast as tsp
from .StopWatch import Stopwatch


class Analyse():
    """
        class that contains methods to analyze a podcast for the occurrence of selected words
    """

    def __init__(self, options: dict ={}):

        #standard options
        self.transscripe: bool = True
        self.transscript_path: str = "transscripte"
        self.audio_path: str = "podcast"
        self.whisper_model: str = "medium"
        self.delete_files: dict = {"audio" : False, "transscripts" : False}

        #get options from user if set
        self.transscripe = options.get('transscripe', self.transscripe)
        self.transscript_path = options.get('transscript_path', self.transscript_path)
        self.audio_path = options.get('audio_path', self.audio_path)
        self.whisper_model = options.get('whisper_model',self.whisper_model)
        self.delete_files["audio"] = options.get('delete_audio_files',self.delete_files.get("audio"))
        self.delete_files["transscripts"] = options.get('delete_transscript_files',self.delete_files.get("transscripts"))


        self.filterlists: list = os.listdir("filterlists")

        self.word_in_epsiode: list = []
        self.unique_words_count: list = []
        self.word_list: list = []

    def transcripe_all_epsisodes_of_podcast(self) -> None:
        """
            calls the transscription module
        """
        if self.transscripe:

            options = {
                "transscript_path" : self.transscript_path,
                "audio_path" : self.audio_path,
                "whisper_model" : self.whisper_model
            }
            
            transscripe = tsp(options)
            transscripe.transscripe()

            print("\ntranscribe finished")
        else:
            print("skipped transcribing")


    
    def convert_file_to_list(self) -> None:
        """
            converts the files with the transcripts into a list.
            removes all special characters and spaces. 
            all words are converted to lower case. 
        """
        print("start reading files")
        for episode in os.listdir(self.transscript_path):
            with open(f"transscripte/{episode}", "r") as f:
                text = f.read()
                text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
                word_list_tmp = text.split()
                for word in word_list_tmp:
                    self.word_list.append(word.strip())
        print("read all files")



    def filter_for_words(self) -> None:
        """
            checks which words from the filter lists were used in the podcast
        """
        stopwatch = Stopwatch()
        timer = Thread(target=stopwatch.printTime)
        timer.start()

        print("start filter")
        for filterlist in self.filterlists:
            with open(f"filterlists/{filterlist}", 'r') as file:
                zeilen = file.readlines()
                for wort in self.word_list:
                    for zeile in zeilen:
                        if zeile.strip().lower()  == wort:
                            self.word_in_epsiode.append(wort)
        print("\nfiltered all")

        stopwatch.stop()

    def create_unique_word_list(self) -> None:
        """
            delete all duplicates from the list of used words
        """
        print("start create_unique_word_list")
        unique_words_set = set(self.word_in_epsiode)
        self.unique_words_list = list(unique_words_set)
        print("create_unique_word_list")
    
    def count_occurance_of_words(self) -> None:
        """
            counts how often the found words from the filter lists were used in the podcast
        """
        print("start counting unique words")
        for wort in self.unique_words_list:
            count = self.word_list.count(wort.strip())
            self.unique_words_count.append((wort.strip(), count))
        print("counted all\n\n")

    def delete_project_files(self) -> None:
        try:
            if self.delete_files["audio"]:
                shutil.rmtree(self.audio_path)
            if self.delete_files["transscripts"]:
                shutil.rmtree(self.transscript_path)
        except FileNotFoundError:
            pass

    def analyze(self) -> None:
        """
            starts the process of analyzing the podcast and if selected transscripe it first
        """
        self.transcripe_all_epsisodes_of_podcast()
        self.convert_file_to_list()
        self.filter_for_words()
        self.create_unique_word_list()
        self.count_occurance_of_words()
        self.delete_project_files()



