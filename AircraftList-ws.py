import websocket
import json
import csv

unique_entries = set()

def on_message(ws, message):
    try:
        data = json.loads(message)
        ac = data  # The data seems to contain information about a single aircraft

        icao_addr = ac.get('Icao_addr', '')
        reg = ac.get('Reg', '')
        tail = ac.get('Tail', '')
        alt = ac.get('Alt', '')
        lat = ac.get('Lat', '')
        lon = ac.get('Lng', '')  # Note that 'Long' was changed to 'Lng'
        speed = ac.get('Speed', '')
        track = ac.get('Track', '')
        signal_level = ac.get('SignalLevel', '')
        last_seen = ac.get('Last_seen', '')

        # Create a unique key for each entry to check for duplicates
        entry_key = (icao_addr, reg, tail, alt, lat, lon, speed, track, signal_level, last_seen)

        # Check if the entry is already in the set (duplicate)
        if entry_key not in unique_entries:
            # Add the entry to the set
            unique_entries.add(entry_key)

            # Write the extracted fields to a CSV file
            with open('acList.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Prints the following data from Stratux: ICAO_ADDR, REGISTRATION NUMBER, TAIL NUMBER, ALTITUDE, LATITUDE, LONGITUDE, SPEED, TRACK, SIGNAL_LEVEL, LAST_SEEN
                csv_writer.writerow([icao_addr, reg, tail, alt, lat, lon, speed, track, signal_level, last_seen])
    except Exception as e:
        print(f"Error processing message: {e}")

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket connection closed")

def on_open(ws):
    print("WebSocket connection established")

def main():
    # CHANGE TO YOUR STRATUX SERVER URL -- KEEP /traffic
    websocket_url = 'ws://stratux.ib.hackshack.sh/traffic'
    ws = websocket.WebSocketApp(websocket_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()

if __name__ == "__main__":
    # Write the header to the CSV file (only if the file is empty)
    with open('acList.csv', 'r', newline='') as csvfile:
        if not csvfile.read():
            with open('acList.csv', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Icao_addr', 'Reg', 'Tail', 'Alt', 'Lat', 'Long', 'Speed', 'Track', 'SignalLevel', 'Last_seen'])

    main()

