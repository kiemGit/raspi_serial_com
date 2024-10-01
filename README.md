# raspi_serial_com
send data from raspi to pc using serial communication UART GPIO raspi and converter RS232 to TTL and ATEN

# "config for activate serial communication UART GPIO",
		
	"1": activate serial communication UART GPIO [sudo raspi-config],
	"2": select 3 Interface Options,
	"3": select I6 Serial Port,
	"4": Would you like a login ....., press <No>.
	"5": Would you like the serial port hardware to be enabled?, press <Yes>,
	"6": Select <Finish>,
	"7": Reboot raspi,
 	"8": check if the UART is enabled by running: [dmesg | grep tty]" output ass bellow, make sure [ttyS0] is show,
 	"9": [    1.603411] fe215040.serial: ttyS0 at MMIO 0xfe215040 (irq = 37, base_baud = 62500000) is a 16550,
	"10": cek serial com port status [sudo nano /boot/config.txt], val: enable_uart=1,
			
# "wiring RS232 to TTL converter to rasberry",
		
	"1": "(RS232) GND  - (raspi) GND (PIN 06)",
	"2": "(RS232) TXD  - (raspi) TXD0, UART (GPIO 14 - PIN 08)",
	"3": "(RS232) RXD  - (raspi) RXD0, UART (GPIO 15 - PIN 10)",
	"4": "(RS232) VCC  - (raspi) 3V/5V (PIN 01 or PIN 02)"
		
# "additional modules",
	
	"1": "ATEN converter",
	"2": "RS232 converter serial communication from RASPI"

# "test send data to pc from raspi",

	"1": "connecting ATEN to RS232 converter, and USB connector from ATEN connect to PC",
	"2": "open [Powershell] in windows, type [[System.IO.Ports.SerialPort]::GetPortNames()] for check COM port active",
	"3": "open [Hercules] tools app, config serial [Name:COM4, Baud:9600, Data size:8, Parity:none, Handsake:OFF, Mode:Free],
	"4": "install pyserial (if you haven't already): [ pip install pyserial ]",
	"5": "run python script [ptyhon3 serial_com_uart.py]"
