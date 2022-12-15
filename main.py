import src.PodcastAnalyse as pay
options = { 'whisper_model': "tiny", 'transscript_path' : "foo"}
podcast_analyser = pay.Analyse(options)
podcast_analyser.analyze()

print(f"uniqe words with count: {sorted(podcast_analyser.unique_words_count, key = lambda x: x[1])}\n")
print(f"ammount of uniqe words: {len(podcast_analyser.unique_words_count)}\n")
print(f"total word count: {len(podcast_analyser.woerter_liste)}\n")