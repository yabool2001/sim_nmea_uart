import serial
import time
import modules.my_serial as my_serial

import sys
sys.path.append ( "/Users/mzeml/python/sim_nmea_uart/modules/" )

import modules.my_serial as my_serial

#nmea_source_filename = "source/2023.10.01.22.57_L86.txt"
nmea_source_filename = "source/2023.10.28.03_L86.bin"
#nmea_source_filename = "source/2023.10.28.04_L86.bin"

# Otwórz port szeregowy COM
com = serial.Serial ()
my_serial.set_serials_cfg ( com , 115200 , 'STLink' )
my_serial.open_serial_ports ( com )

#com = serial.Serial ( 'COM9' , 9600 , timeout = 1 )

with open ( nmea_source_filename , 'r' ) as f :
    lines = f.readlines ()
    for line in lines :
        com.write ( line.encode() )
        #com.write ( line )
        print ( line )
        time.sleep ( 0.5 )


#with open ( nmea_source_filename , 'rb' ) as f :
#    b = f.read()
#    for byte in b:
#        com.write ( byte )
#    print ( com.read () )

my_serial.close_serial_ports ( com )
