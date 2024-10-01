import serial

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,  # Set your desired baud rate
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

if ser.is_open:
    ser.write(b'Hello send from python raspberry 4 by SAP\n')
    print("Serial port is open.")
else:
    print("Failed to open serial port.")
