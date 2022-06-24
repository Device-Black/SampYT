from youtubesearchpython import VideosSearch
import json
import sys

if len(sys.argv) == 1:
 print ("null data")
 exit()

Search = VideosSearch(sys.argv[1], limit = 1, region = 'BR')

for test in Search.result()['result']:
  print (test['link'])
