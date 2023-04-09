# flight-watcher
# AI Written Introduction:
This is a Python script that retrieves aircraft data from a Virtual Radar Server (VRS) and displays it in a live display. It also writes the data to a CSV file and alerts the user when a specific aircraft is detected.

The script uses the requests library to make HTTP requests to the VRS server and retrieve the aircraft data in JSON format. It then parses the JSON data and extracts the relevant information such as the aircraft ID, registration, altitude, latitude, longitude, speed, track, and signal strength.

The script also uses the os library to clear the screen and print a header to the live display. It uses the datetime library to format the last seen time of each aircraft and to calculate the time elapsed since the last alert.

The script maintains a set of printed lines to ensure that each line is unique and avoids duplicate entries in the live display and CSV file. It also checks if a specific aircraft is in the hot list and alerts the user with an audio notification if it is detected.

Overall, this script provides a simple and effective way to monitor aircraft activity in real-time and alert the user when specific aircraft are detected.

My Introduction:
Flight Watcher is designed to watch the AircraftList.json file from an active Virtual Radar Server setup and retrieve the following information as a CSV list:
```
ID# : Unique number representing each aircraft
Reg : Aircraft Registration Number
Alt : Altitude of the aircraft
Lat : Latitude of the aircraft
Long: Longitude of the aircraft
Spd : Speed of the aircraft
Trak: Track/Heading of the aircraft
Sig : Signal Strength of the aircraft ADS-B beacon
Last: Time and Date aircraft was last seen.
```

Just run:
```
$ python3 ./AircraftList.py
```

Active traffic will appear in the terminal and all unique events will appear in ./acList.csv like the following:
```
11290903,,4200,32.51367,-117.0813,215.0,228.0,2023-03-02 00:13:41
11243277,N844DN,25200,33.5508,-117.32895,450.0,82.0,2023-03-02 00:12:55
854322,XA-VLL,35000,33.37784,-116.83048,525.0,139.0,2023-03-02 00:08:34
854118,XA-VLE,31125,32.49081,-116.8609,529.0,123.0,2023-03-02 00:08:07
```
