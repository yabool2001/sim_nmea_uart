import serial
import time
import modules.my_serial as my_serial

import sys
sys.path.append ( "/Users/mzeml/python/sim_nmea_uart/modules/" )

import modules.my_serial as my_serial

nmea_source_filename = "/source/2023.10.01.22.56_L86.txt"

# Otwórz port szeregowy COM
com = serial.Serial ()
my_serial.set_serials_cfg ( com , 9600 )
my_serial.open_serial_ports ( com )

#com = serial.Serial ( 'COM9' , 9600 , timeout = 1 )

# Otwórz plik tekstowy
with open ( 'nmea_source_filename' , 'r' ) as f :
    lines = f.readlines ()
    for line in lines :
        com.write ( line.encode() )
        time.sleep ( 0.1 )
# Zamknij port szeregowy
ser.close ()