import requests
import time
import os
import pafy
import vlc
from datetime import datetime

""" Get Alerts for AC of Interest """
hot_alert_url = 'https://www.youtube.com/watch?v=-bzWSJG93P8' 
acHotList = ['LIST', 'OF-TAIL', 'NUMBERS']

last_alert_time = None

while True:
    """ Change IP below to your VRS systems IP """
    url = 'http://192.168.1.65/VirtualRadar/AircraftList.json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        ac_list = data['acList']
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        """ Print a header to the live display """
        print('                    #############################################')
        print('                    ###       Skinwalker Flight Watcher       ###')
        print('                    #############################################')
        print('Id, Reg, FSeen, Alt, Lat, Long, Spd, Trak, Sig')
        printed_lines = set()
        for ac in ac_list:
            fseen = ac.get('FSeen', None)
            if fseen is not None:
                fseen = int(fseen[6:-2]) / 1000
                fseen = datetime.fromtimestamp(fseen).strftime('%Y-%m-%d %H:%M:%S')
            line = ','.join(str(ac.get(key, '')) for key in ['Id', 'Reg', 'Alt', 'Lat', 'Long', 'Spd', 'Trak', 'Sig'])
            if line not in printed_lines:
                printed_lines.add(line)
                line += fseen if fseen is not None else ''
                print(line)
                """ The list gets dumped into the CSV defined below """
                with open('acList.csv', 'a') as f:
                    f.write(line + '\n')
            """ Alert on specific AC when detected """
            if ac.get('Reg') in acHotList:
                if last_alert_time is None or (datetime.now() - last_alert_time).total_seconds() >= 240:
                    last_alert_time = datetime.now()
                    url = hot_alert_url
                    video = pafy.new(url)
                    bestaudio = video.getbestaudio()
                    media = vlc.MediaPlayer(bestaudio.url)
                    media.play()
    else:
        print('Error: Could not retrieve data')

    time.sleep(1)