## Enabling Port Forwarding and Configuring Raspberry Pi for WAN Connections
1. See [WikiHow Tutorial for Port Forwarding](./wikihow.md)
2. If the password for your router is not known, search for the default credentials from the manufacturer's website. Note the serial number of your router.
3. Inside the router control panel, find and write down the IPV4 WAN address of the gateway. This will be the address used by computers outside of the network to communicate with your internal network.
3. Find the connected devices menu.
4. Write down the LAN IPV4 address for the PI (raspberrypi).
5. Navigate to the Port Forwarding settings. (Note: These settings may be hidden behind advanced settings.)
6. Enable port forwarding for port 22 using the Raspberry PI LAN address.