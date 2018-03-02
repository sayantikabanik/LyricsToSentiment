from PyLyrics import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

lyricsOfSong=(PyLyrics.getLyrics('Ed Sheeran ','Perfect')) #Print the lyrics directly
lyricsList=lyricsOfSong.split()
print(lyricsOfSong)
for word in lyricsList:
	 opinion=TextBlob(str(word),analyzer=NaiveBayesAnalyzer())
	 print(word+"-------")
	 print(opinion.sentiment)
     
	
