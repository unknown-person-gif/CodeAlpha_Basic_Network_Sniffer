# 🛡️ CodeAlpha – Basic Network Sniffer

## 📌 Project Overview

The **Basic Network Sniffer** is a Python-based network monitoring tool developed using the Scapy library. It captures live network packets and analyzes their structure to understand how data travels across a network.

The program identifies different network protocols, extracts source and destination IP addresses, displays port information, and analyzes packet payloads.

This project is developed as part of the CodeAlpha Python Programming Internship to gain practical knowledge of computer networking and packet analysis.

## 🎯 Objectives

* Capture live network traffic using Python.
* Analyze captured network packets.
* Identify different network protocols.
* Extract source and destination IP addresses.
* Display TCP and UDP port numbers.
* Analyze ICMP and ARP packet information.
* Display packet payloads in hexadecimal and ASCII formats.
* Understand how data flows through a network.

## ✨ Features

* **Live Packet Capturing:** Captures network packets in real time using Scapy.
* **Protocol Identification:** Identifies TCP, UDP, ICMP, ARP, IPv4, and IPv6 traffic.
* **IP Address Extraction:** Displays source and destination IP addresses.
* **Port Information:** Extracts source and destination ports for TCP and UDP packets.
* **TCP Flag Detection:** Displays TCP flags.
* **ICMP Analysis:** Displays ICMP type and code.
* **ARP Analysis:** Displays ARP operation details.
* **Payload Analysis:** Displays payload length and optional HEX and ASCII previews.
* **Packet Filtering:** Supports BPF filters to capture specific network traffic.
* **Packet Count Control:** Allows users to specify the number of packets to capture.
* **Command-Line Interface:** Provides flexible options using Python's argparse module.

## 🛠️ Technologies Used

| Technology | Purpose                        |
| ---------- | ------------------------------ |
| Python     | Programming language           |
| Scapy      | Packet capturing and analysis  |
| Argparse   | Command-line argument handling |
| BPF        | Network packet filtering       |

## 📂 Project Structure

```text
CodeAlpha_Basic_Network_Sniffer/
│
├── .github/
│   └── workflows/
│
├── README.md
│
├── Screenshot.png
│
└── net2_sniffer.py
```

*Note: Screenshot.png represents your project screenshot. Use the actual screenshot filename in your repository.*

## ⚙️ Installation and Setup

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd CodeAlpha_Basic_Network_Sniffer
```

### 3. Install Scapy

```bash
pip install scapy
```

### 4. Install Packet Capture Dependencies

Depending on your operating system:

* **Windows:** Install Npcap.
* **Linux:** Use the appropriate packet-capture permissions. Scapy can use AF_PACKET.
* **macOS:** Ensure the required BPF packet-capture permissions are available.

## 🚀 How to Run

Run the following command from the project directory:

```bash
python net2_sniffer.py
```

The program starts capturing packets using the default network interface.

**Note:** Administrator or root privileges may be required for packet capturing.

## 💻 Command-Line Options

| Argument            | Description                              |
| ------------------- | ---------------------------------------- |
| `-i`, `--interface` | Specify the network interface            |
| `-c`, `--count`     | Specify the number of packets to capture |
| `-f`, `--filter`    | Apply a BPF packet filter                |
| `--show-payload`    | Display payload in HEX and ASCII formats |

### Examples

**1. Capture packets using the default interface**

```bash
python net2_sniffer.py
```

**2. Capture only 10 packets**

```bash
python net2_sniffer.py -c 10
```

**3. Capture TCP packets**

```bash
python net2_sniffer.py -f "tcp"
```

**4. Capture UDP packets**

```bash
python net2_sniffer.py -f "udp"
```

**5. Capture ICMP packets**

```bash
python net2_sniffer.py -f "icmp"
```

**6. Display packet payload**

```bash
python net2_sniffer.py --show-payload
```

**7. Capture 20 TCP packets and display payload**

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

*The above output is illustrative. Actual results depend on captured network traffic.*

## 🔍 Supported Protocols

| Protocol | Description                                 |
| -------- | ------------------------------------------- |
| TCP      | Reliable, connection-oriented communication |
| UDP      | Fast, connectionless communication          |
| ICMP     | Network diagnostics and error reporting     |
| ARP      | Resolves IPv4 addresses into MAC addresses  |
| IPv4     | Internet Protocol version 4                 |
| IPv6     | Internet Protocol version 6                 |

## ⚙️ Working Process

1. **Packet Capturing:** Scapy listens to the selected network interface and captures packets.
2. **Protocol Identification:** Identifies the protocol used by each packet.
3. **Address Extraction:** Extracts source and destination IP addresses.
4. **Packet Analysis:** Examines TCP, UDP, ICMP, and ARP information.
5. **Payload Extraction:** Extracts available packet payload data.
6. **Payload Display:** Displays payload information in HEX and ASCII formats when enabled.
7. **Output:** Prints the analyzed packet information in the terminal.

## 🔐 Security and Ethical Considerations

* Use this tool only on networks you own or have permission to monitor.
* Do not capture private network communications without authorization.
* Avoid exposing sensitive information contained in packet payloads.
* HTTPS traffic is encrypted, so its application data generally cannot be read directly.
* Packet capturing may require administrator or root privileges.

## ⚠️ Limitations

* Captures only traffic visible to the selected network interface.
* Encrypted application data cannot generally be decoded directly.
* Payload preview is limited to the first 256 bytes.
* Packet capture permissions depend on the operating system.
* Some packets may not contain application payload data.

## 🎓 Learning Outcomes

Through this project, I gained practical knowledge of:

* Network packet capturing.
* TCP/IP communication.
* Network protocols and their functions.
* IP addressing and port numbers.
* Packet headers and payloads.
* Network traffic monitoring.
* Python network programming.
* Basic cybersecurity concepts.

## 🔮 Future Enhancements

* Develop a graphical user interface (GUI).
* Add real-time network traffic statistics.
* Export captured packets into PCAP files.
* Implement advanced packet filtering.
* Add network traffic visualization.
* Generate packet analysis reports.

## 👨‍💻 Author

**Name:** G.BHARATH KUMAR

**Internship:** CodeAlpha Python Programming Internship

**Project:** Basic Network Sniffer

**Technology:** Python and Scapy

## 📜 License

This project is developed for educational purposes as part of the CodeAlpha internship.
