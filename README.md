# 🛡️ Python Network Packet Sniffer

## 📌 Project Overview

The **Python Network Packet Sniffer** is a basic network monitoring tool developed using Python and the Scapy library. It captures live network packets and analyzes their structure to understand how data travels across a network.

The program identifies different network protocols, extracts source and destination IP addresses, displays port numbers, and provides packet payload analysis.

This project helps beginners understand network communication, packet structures, and commonly used networking protocols.

## 🎯 Objectives

* Capture live network traffic using Python.
* Analyze captured network packets.
* Identify different network protocols.
* Extract source and destination IP addresses.
* Display TCP and UDP port numbers.
* Analyze ICMP and ARP packet information.
* Examine packet payloads in hexadecimal and ASCII formats.
* Understand how data flows through a network.

## ✨ Features

* **Live Packet Capturing:** Captures network packets in real time using Scapy.
* **Protocol Identification:** Identifies TCP, UDP, ICMP, ARP, IPv4, and IPv6 packets.
* **IP Address Extraction:** Displays source and destination IP addresses.
* **Port Information:** Extracts source and destination port numbers for TCP and UDP.
* **TCP Flag Detection:** Displays TCP flags.
* **ICMP Analysis:** Displays ICMP type and code.
* **ARP Analysis:** Displays ARP operation details.
* **Payload Analysis:** Displays packet payload length and optional HEX and ASCII previews.
* **Packet Filtering:** Supports BPF filters to capture specific types of network traffic.
* **Packet Count Control:** Allows users to specify the number of packets to capture.
* **Cross-Platform Support:** Uses Scapy for packet capturing on Linux, Windows, and macOS, with the required platform-specific capture dependencies.

## 🛠️ Technologies Used

| Technology  | Purpose                               |
| ----------- | ------------------------------------- |
| Python      | Programming language                  |
| Scapy       | Network packet capturing and analysis |
| Argparse    | Command-line argument handling        |
| BPF Filters | Filtering network traffic             |

## 📂 Project Structure

```text
Python-Network-Sniffer/
│
├── net2_sniffer.py
│
├── README.md
│
└── requirements.txt
```

## ⚙️ Installation and Setup

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd Python-Network-Sniffer
```

### Step 3: Install Scapy

Install the required Python library:

```bash
pip install scapy
```

Alternatively, create a `requirements.txt` file containing:

```text
scapy
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Install Packet Capture Dependencies

Depending on your operating system:

* **Windows:** Install Npcap to enable packet capturing.
* **Linux:** Ensure the required packet-capture permissions are available.
* **macOS:** Ensure the required BPF packet-capture permissions are available.

## 🚀 How to Run the Program

Run the following command:

```bash
python net2_sniffer.py
```

The program starts capturing network packets using the default network interface.

**Note:** Run the terminal with administrator/root privileges if required.

## 💻 Command-Line Options

The program supports several command-line arguments.

| Argument              | Description                                     |
| --------------------- | ----------------------------------------------- |
| `-i` or `--interface` | Specify the network interface                   |
| `-c` or `--count`     | Specify the number of packets to capture        |
| `-f` or `--filter`    | Apply a BPF packet filter                       |
| `--show-payload`      | Display packet payload in HEX and ASCII formats |

### Examples

**1. Capture packets using the default interface**

```bash
python net2_sniffer.py
```

**2. Capture only 10 packets**

```bash
python net2_sniffer.py -c 10
```

**3. Capture only TCP packets**

```bash
python net2_sniffer.py -f "tcp"
```

**4. Capture only UDP packets**

```bash
python net2_sniffer.py -f "udp"
```

**5. Capture only ICMP packets**

```bash
python net2_sniffer.py -f "icmp"
```

**6. Display packet payload**

```bash
python net2_sniffer.py --show-payload
```

**7. Capture 20 TCP packets and display their payload**

```bash
python net2_sniffer.py -c 20 -f "tcp" --show-payload
```

**8. Specify a network interface**

```bash
python net2_sniffer.py -i "eth0"
```

Replace `eth0` with the appropriate interface name on your system.

## 📊 Sample Output

```text
===================================
       PYTHON NETWORK SNIFFER
===================================

Interface : Default
Packet Limit: 10
Filter    : tcp

Starting packet capture...


=======================================================
NETWORK PACKET DETECTED
=======================================================

Source IP      : 192.168.1.5
Destination IP : 142.250.183.14
Protocol       : TCP
Packet Size    : 74 bytes
Source Port    : 54321
Destination Port: 443
TCP Flags      : S

Payload: No application data available.

=======================================================

Packet capture completed.
```

*Note: The sample IP addresses and packet details are illustrative. Actual output depends on your network traffic.*

## 🔍 Supported Network Protocols

| Protocol | Description                                                   |
| -------- | ------------------------------------------------------------- |
| TCP      | Provides reliable, connection-oriented communication.         |
| UDP      | Provides fast, connectionless communication.                  |
| ICMP     | Used for network diagnostics and error reporting.             |
| ARP      | Resolves IPv4 addresses into MAC addresses on local networks. |
| IPv4     | Internet Protocol version 4.                                  |
| IPv6     | Internet Protocol version 6.                                  |

## 🧠 How the Program Works

The network sniffer follows these steps:

1. **Packet Capturing:** Scapy listens to the selected network interface and captures packets.
2. **Protocol Identification:** The program identifies the protocol associated with each packet.
3. **Address Extraction:** It extracts source and destination IP addresses.
4. **Packet Analysis:** It analyzes TCP, UDP, ICMP, and ARP-specific information.
5. **Payload Extraction:** It extracts available packet payload data.
6. **Payload Display:** When enabled, it displays payload data in hexadecimal and ASCII formats.
7. **Output:** The captured packet information is displayed in the terminal.

## 🔐 Security and Ethical Considerations

* Use this tool only on networks you own or have explicit permission to monitor.
* Do not capture or inspect other people's private network communications without authorization.
* Avoid exposing sensitive information contained in packet payloads.
* HTTPS traffic is encrypted, so the actual application data generally cannot be read directly.
* Packet capturing may require administrator or root privileges.

## ⚠️ Limitations

* The program captures only traffic visible to the selected network interface.
* Encrypted traffic cannot generally be decoded into its original application content.
* Packet capture permissions depend on the operating system.
* Payload analysis is limited to a preview of the first 256 bytes.
* Some protocols may not contain application payload data.
* BPF filter availability depends on the packet-capture backend.

## 🎓 Learning Outcomes

By completing this project, you will gain practical knowledge of:

* Network packet capturing.
* Network protocols and their functions.
* TCP/IP communication.
* IP addressing and port numbers.
* Packet headers and payloads.
* Network traffic monitoring.
* Python network programming.
* Basic cybersecurity and network analysis concepts.

## 🔮 Future Enhancements

The project can be extended with the following features:

* Graphical User Interface (GUI).
* Packet capture statistics and graphs.
* Export captured packets into PCAP files.
* Advanced protocol detection.
* Packet filtering by IP address and port number.
* Real-time network traffic visualization.
* Packet analysis reports.

## 👨‍💻 Author

**Name:** Your Name

**Project:** Basic Network Sniffer

**Domain:** Python Programming / Cybersecurity

## 📜 License

This project is developed for educational and learning purposes. You may modify and improve it for authorized network monitoring and analysis.
