from os import system as shell
from os.path import exists
from time import time, sleep

def checkTemporaryFiles():
  config = exists("config.ini")
  if config:
    print ("config.ini founded!")
  else:
    return 0

  text = open("config.ini").readlines()
  write = ""

  for i in range(len(text)):
    info = text[i].split("=")
    if len(info) < 2:
      continue

    tempo1 = int(info[1])
    tempo2 = int(time())

    if tempo1 < tempo2:
      shell("rm " + info[0])
    else:
      write += info[0] + "=" + info[1]

  shell("rm config.ini")
  shell("echo '" + write + "' >> config.ini")

while True:
  shell("clear && echo 'running'")
  checkTemporaryFiles()
  sleep(10)
