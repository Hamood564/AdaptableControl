import snap7
from snap7.util import get_int
from snap7.util import set_int


def write_int(plc, db_number, start_address, value):
    data = bytearray(2) #2 bytes for an integer
    set_int(data,0,value)
    plc.db_write(db_number, start_address, data)
    print(f"Written {value} to DB {db_number} at address {start_address}")



PLC_IP = "192.168.115.180"
RACK= 0
SLOT= 1


#Connecting to the PLC
plc = snap7.client.Client()
plc.connect(PLC_IP,RACK,SLOT)

#check if the plc is connected
if plc.get_connected():
    print("Connected to the PLC")

    #Read Data Block (DB)
    db_number = 1
    start_address = 0
    size = 2 # Reading 2 bytes (16-bit integer)

    data = plc.db_read(db_number,start_address,size)
    value = get_int(data,0)

    print(f"Read Value from DB{db_number}:{value}")

    write_int(plc,db_number,start_address,value=1234)

    #Disconnect
    plc.disconnect()

else:
    print("Failed to Connect to PLC")

