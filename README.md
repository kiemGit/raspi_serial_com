# raspi_serial_com
send data from raspi to pc using serial communication UART GPIO raspi and converter RS232 to TTL and ATEN
# install raspi using raspi imager (Internet Requirements)

	+ click [CHOOSE DEVICE] 
	+ select [Raspberry Pi3]
	+ click [CHOOSE OS]
	+ select [Raspberry Pi OS (other)]
	+ select [Raspberry Pi OS (Legacy, 64-bit) lite]
	+ click [CHOOSE STORAGE] 
	+ select SD card you want to install raspberry pi OS
	+ select [NEXT] button 
 
# configurasi ip address

	+ sudo nano /etc/dhcpcd.conf
 	+ add script as bellow
	        interface eth0  # or wlan0 for Wi-Fi
	        static ip_address=192.168.1.100/24  # Replace with your desired static IP and subnet
	        static routers=192.168.1.1          # Replace with your router's IP address
	        static domain_name_servers=192.168.1.1 8.8.8.8  # Replace or add DNS servers (e.g., 8.8.8.8 for Google)
	 
# update rasberry pi

	sudo apt update

# "config for activate serial communication UART GPIO",
		
	+ activate serial communication UART GPIO [sudo raspi-config],
	+ select 3 Interface Options,
	+ select I6 Serial Port,
	+ Would you like a login ....., press <No>.
	+ Would you like the serial port hardware to be enabled?, press <Yes>,
	+ Select <Finish>,
	+ Reboot raspi,
 	+ check if the UART is enabled by running: [dmesg | grep tty]" output ass bellow, make sure [ttyS0] is show,
 	+ [    1.603411] fe215040.serial: ttyS0 at MMIO 0xfe215040 (irq = 37, base_baud = 62500000) is a 16550,
	+ cek serial com port status [sudo nano /boot/config.txt], val: enable_uart=1,
			
# "wiring RS232 to TTL converter to rasberry",
		
	+ "(RS232) GND  - (raspi) GND (PIN 06)",
	+ "(RS232) TXD  - (raspi) TXD0, UART (GPIO 14 - PIN 08)",
	+ "(RS232) RXD  - (raspi) RXD0, UART (GPIO 15 - PIN 10)",
	+ "(RS232) VCC  - (raspi) 3V/5V (PIN 01 or PIN 02)"
		
# "additional modules",
	
	+ "ATEN converter",
	+ "RS232 converter serial communication from RASPI"

# "test send data to pc from raspi",

	+ "connecting ATEN to RS232 converter, and USB connector from ATEN connect to PC",
	+ "open [Powershell] in windows, type [[System.IO.Ports.SerialPort]::GetPortNames()] for check COM port active",
	+ "open [Hercules] tools app, config serial [Name:COM4, Baud:9600, Data size:8, Parity:none, Handsake:OFF, Mode:Free],
 	+  install pip [sudo apt install python3-pip]
	+ "install pyserial (if you haven't already): [ pip install pyserial ]",
	+ "run python script [ptyhon3 serial_com_uart.py]"
