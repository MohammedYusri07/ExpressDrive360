import serial
import pynmea2

def read_gps_data():
    try:
        # Open serial port
        ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return

    while True:
        try:
            # Read a line of GPS data
            gps_data = ser.readline().decode('utf-8', errors='ignore').strip()

            # Check if the data starts with '$GNRMC' (Recommended minimum specific GPS/Transit data)
            if gps_data.startswith('$GNRMC'):
                # Parse the NMEA sentence
                try:
                    msg = pynmea2.parse(gps_data)
                    # Extract latitude and longitude
                    latitude = msg.latitude
                    longitude = msg.longitude

                    # Verify latitude and longitude
                    if latitude and longitude:
                        # Print latitude and longitude
                        print("Latitude:", latitude, "Longitude:", longitude)
                except pynmea2.ParseError:
                    pass
                except Exception:
                    pass
        except Exception as e:
            pass

if __name__ == "__main__":
    read_gps_data()
