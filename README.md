# Podcast Analyser
----------------------------------------------------------------
 ## What is this?
A tool to analyse which words from filter lists are used in a podcast and how often they are used. The episodes are transcribed automatically by [OpenAi Whisper](https://github.com/openai/whisper). This can take a long time depending on the hardware and size of the file. It is possible to analyse several episodes at once. It is of course also possible to analyse audio files other than a podcast.

 ## How to use it?
 1. install the requirements.txt
 (It is recommended to use a virtual environment)

```bash
  pip3 install -r requirements.txt
```
2. if you don't have ffmpeg installed, install it. Under Ubuntu/Debian:
```bash
sudo apt update && sudo apt install ffmpeg
```
for other operating systems: [How to install ffmpeg](https://www.hostinger.com/tutorials/how-to-install-ffmpeg)

3. You might have to install whisper manually:
```bash
pip3 install git+https://github.com/openai/whisper.git 
```
4. Install CUDA if your GPU is compatibale. <br/>
How to install [CUDA](https://developer.nvidia.com/cuda-downloads)

5. Put the podcast episodes in a folder called "podcast". Alternatively, you can create a folder with your own name. To be able to use it:

```Python
import src.PodcastAnalyse as pay
options = {"audio_path" : "your folder name"}
podcast_analyser = pay.Analyse(options)
```
4. Start analysing the podcast
```Python
podcast_analyser.analyze()
```
----------------------------------------------------------------
## documentation
### options:
Options as Dictionary 
```Python
options = {"option name" : "option"}
podcast_analyser = pay.Analyse(options)
```

+ ```trancripe: bool``` ```True``` is standard, ```False``` skips the part of transciping e.g. if there are already transcripted files.

+ ```transscript_path: str``` The folder in which the files with the transcribed podcast episodes will be saved. No other files should be in here!

+ ```audio_path: str``` folder containing the audio files to be transcribed. No other files should be in here!

+ ```whisper_model: str``` The model with which whisper should work. More information: [Whisper Github](https://github.com/openai/whisper)

+ ```delete_audio_files: bool``` deletes the audio files after they have been transcribed

+ ```delete_transscript_files: bool``` deletes the files with the transscripts after they have been processed

### filter lists:
You can create your own filter lists which must be placed in the folder ```filterlists```. Make sure that each word is on its own line.

----------------------------------------------------------------
## Roadmap
+ make code nice
+ download all episodes of a podcast from the RSS feed
+ Extend the standard filter lists

----------------------------------------------------------------

## why?

I created the program to analyze the german podcast Hobbylos by Rezo and Julian Bam on the frequency of the use of swear words. Hence the selection of the filter lists.