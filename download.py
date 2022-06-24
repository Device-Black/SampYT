from youtubesearchpython import VideosSearch
import sys, json, random
from time import time
from os import system

args = open("args.txt").readlines()

Search = VideosSearch(args[0], limit = 1)

for test in Search.result()['result']:
  """ ------------------- """
  """ verificar a duracao """
  """ ------------------- """
  duracao = test['duration']

  if len(duracao) > 5:
    print ("invalid duration")
    exit()

  tempo = duracao.split(":")
  m = int(tempo[0]) * 60
  s = int(tempo[1]) + m

  if s > 420:
    print ("invalid duration")
    exit()


  """ -------------- """
  """ gerar id unico """
  """ -------------- """
  uniqueid = args[1]


  """ --------------------------------- """
  """ baixar e extrair o audio do video """
  """ --------------------------------- """
  comando = "yt-dlp -x --audio-format mp3 --audio-quality 10 " + test['link'] + " -o Video/" + uniqueid + ".mp3"
  system (comando)


  """ ------------------------------- """
  """ mover o audio para a pasta Audio """
  """ ------------------------------- """
  timer = int(time()) + (s + 10)
  config = uniqueid + ".mp3=" + str(timer)

  system ("echo 'Audio/" + config + "' >> config.ini")
  system ("mv Video/"+ uniqueid + ".mp3 Audio/")
  system ("clear")
  
