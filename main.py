import time

import src.PodcastAnalyse as pay
import src.utils.PrintTime as pt

start = time.time()



podcast_analyser = pay.Analyse()
podcast_analyser.analyze()

end = time.time()
pt.PrintTime(end - start, False).printTime()