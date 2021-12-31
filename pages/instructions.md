# Raspberry Pi Software and Hardware Installation Proceedures
## Setting up Raspberry Pi Raspbian for Robots Operating System on a SSD Card
1. Take the SSD card and insert it into a Windows or Mac computer.
2. From the official Raspberry Pi website download the quick start ***Raspbian for Robots*** OS installer.
3. Once downloaded, launch the application as administrator if possible.
4. Select the operating system and SSD card to install it on.
5. Close the launcher once the operating system has successfully been flashed to the SSD.
## Enabling SSH on The Raspberry Pi
1. Secure Shell will enable us to access the Raspberry Pi without physical access.
2. Insert the SSD with an operating system installed into a Windows or Mac computer.
3. On the SSD, navigate to where the Pi OS is installed.
4. Create a blank file called ***SSH.txt***
## Inserting and Removing SSD Cards With Raspberry Pi
- When inserting or removing an SSD card great care must be taken as to not damage the board or card.
- When **inserting**, ensure that the one way pins are correctly aligned and gently press the card into the slot.
- When **removing**, grip the grooved end of the card and gently pull until the card is out.  
## Connecting Raspberry Pi to a Local Network via Ethernet
1. Using an ethernet cable, plug one end into the gateway and the other end into the Raspberry Pi.
2. Once a connection has been established, blinking lights will appear on the Pi.
3. From a windows or mac computer on the same network, open up a command prompt.
4. `ping raspberrypi.local` should return with information regarding this new device.
## Enabling Port Forwarding and Configuring Raspberry Pi for WAN Connections
1. Navigate to the control panel of your router by typing in 192.168.1.1 or 10.0.0.1 into your browser, and follow the login instructions.
2. If the password for your router is not known, look for the default credentials from the manufacturer.
3. Find connected devices menu.
4. Write down the WAN address and the LAN address for the PI.
## Enable static IP for Raspberry Pi
1. Navigate to the Port Forwarding settings.
2. (Note: These settings may be behind advanced settings.)
3. Enable port forwarding for port 22 using the Raspberry PI LAN address.
4. Configuring Raspberry Pi Network within Raspbian OS.
## Using SSH with Raspberry Pi
1. On a windows or Mac computer install PuTTY SSH software from the official PuTTY website.
2. Create a new WAN connection.
3. Enter in the WAN address and enter port 22.
4. Click connect and a window should appear.
5. Login with your Raspberry Pi credentials.
## Installing Raspberry Pi Hat Board
1. Carefully remove the Raspberry Pi Hat Board from the box.
**Note:** There are also several small screws and standoffs within this plastic bag.
2. Remove 4 standoffs and 4 screws from the plastic bag.
3. Locate the 4 mounting holes on the raspberry PI:

![](diagrams/standoff_point_locations.png)

4. Place a standoff on the top side of the pi and insert a screw from the bottom side of the board.
5. Repeat for the three other corners and tighten until secure.
6. Locate the IO pins on the PI:

![](diagrams/hat_pin_location.png)

7. Carefully align the hat board with the pins and slide the two together.
8. Screw in the final 4 screws into the top of the hat board.
## Install BME280
1. Remove the **BME280** sensor from box.

![](diagrams/bme280_blank.jpg)

2. Insert the cable into the sensor.
3. Locate the 4 wires marked: **VCC, GND, SCL/SCK,** and **SDA/MOSI.**
4. Strip the terminals off of these wires.
5. On the hat board locate terminals marked: **3v3, GND, SCL,** and **SDA.**

![](diagrams/screw_terminal_bme280_locations.jpg)

6. Unscrew the backs of these terminals.
7. Insert: **VCC** to **3v3**, **GND** to **GND**, **SCL/SCK** to **SCL** and **SDA/MOSI** to **SDA**.
8. Screw the backs of the terminals secure.

## Install MCP3008 ADC to breadboard
## Setting up Wind and Rain Gauges
1. See: Wind and Rain Sensors Hardware Guide.
2. Ensure that the mechanical components are allowed to move freely and are in an area surrounded by at least 10 feet of open air.
3. Connect one RJ11 breakout terminal to the wind speed sensor Rj11 connector.
4. Connect one RJ11 breakout terminal to the rainfall sensor Rj11 connector.
## Install RJ11 breakout for wind speed
## Install RJ11 for wind direction
## Install RJ11 for rainfall
## Install software from GitHub
## Test sensors and deliver data