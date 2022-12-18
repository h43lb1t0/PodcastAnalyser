import src.PodcastAnalyse as pay
import time
start = time.time()

podcast_analyser = pay.Analyse()
podcast_analyser.analyze()

end = time.time()
print("The time of execution of above program is :", (end-start) * 10**3, "ms")

