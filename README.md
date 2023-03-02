# flight-watcher

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
