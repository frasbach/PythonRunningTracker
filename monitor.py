import psutil
from alarm_admin import telegram_bot_sendtext
import time
import datetime

run = True #hier auf true setzen, damit das Programm läuft!
print('Monitor of BeachVolleyBall-Scanner was started...')
counter = 0
while True == True:
  while run == True:
    time.sleep(60)
    process_found = False
    for pid in psutil.pids():
      p = psutil.Process(pid)
      try:
        if p.cmdline()[1] == 'src/app.py':
          process_found = True
          counter = 0
          print('Program still running at: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
      except IndexError:
        pass # Not every pid-Stream has an Array-Element  
    if process_found == False:
      counter += 1
    if counter > 30:
      print('Program has ended because counter > 30 at: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
      telegram_bot_sendtext()
      time.sleep(3600)
      telegram_bot_sendtext()
      time.sleep(7200)
      telegram_bot_sendtext()
      run = False
  time.sleep(172.800)
  print('Program has awaken again after 48h at: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))