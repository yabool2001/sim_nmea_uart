import serial
import time

nmea_source_filename = "/source/2023.10.01.22.56_L86.txt"

# Otwórz port szeregowy COM
ser = serial.Serial ( 'COM9' , 9600 , timeout = 1 )

# Otwórz plik tekstowy
with open ( 'nmea_source_filename' , 'r' ) as f :
    lines = f.readlines ()
    for line in lines :
        ser.write ( line.encode() )
        time.sleep ( 1 )
# Zamknij port szeregowy
ser.close ()
