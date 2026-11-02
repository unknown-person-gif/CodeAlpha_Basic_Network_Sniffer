from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import ARP
from scapy.packet import Raw
import argparse


# Identify the packet protocol
def identify_protocol(packet):

    if packet.haslayer(TCP):
        return "TCP"

    elif packet.haslayer(UDP):
        return "UDP"

    elif packet.haslayer(ICMP):
        return "ICMP"

    elif packet.haslayer(ARP):
        return "ARP"

    elif packet.haslayer(IP):
        return "IP"

    elif packet.haslayer(IPv6):
        return "IPv6"

    return "OTHER"


# Extract source and destination IP addresses
def get_addresses(packet):

    if packet.haslayer(IP):
        return (
            packet[IP].src,
            packet[IP].dst
        )

    elif packet.haslayer(IPv6):
        return (
            packet[IPv6].src,
            packet[IPv6].dst
        )

    elif packet.haslayer(ARP):
        return (
            packet[ARP].psrc,
            packet[ARP].pdst
        )

    return ("Unknown", "Unknown")


# Display packet payload safely

def display_payload(packet, show_payload=False):

    # Extract the payload after the IP layer
    if packet.haslayer(IP):
        payload = bytes(packet[IP].payload.payload)

    elif packet.haslayer(IPv6):
        payload = bytes(packet[IPv6].payload.payload)

    elif packet.haslayer(ARP):
        payload = bytes(packet[ARP].payload)

    else:
        payload = bytes(packet.payload)

    if not payload:
        print("Payload: No application data available.")
        return

    print("\n========== PAYLOAD ANALYSIS ==========")

    print("Payload Length:", len(payload), "bytes")

    if show_payload:

        print("\nPayload (HEX):")
        print(payload[:256].hex(" "))

        print("\nPayload (ASCII):")

        ascii_data = ''.join(
            chr(byte) if 32 <= byte <= 126 else '.'
            for byte in payload[:256]
        )

        print(ascii_data)

        if len(payload) > 256:
            print("Payload truncated...")

    else:
        print("Payload preview disabled.")
        print("Use --show-payload to display payload.")

    print("======================================")



# Analyze each captured packet
def analyze_packet(packet, show_payload=False):

    protocol = identify_protocol(packet)

    src, dst = get_addresses(packet)

    print("\n" + "=" * 55)

    print("NETWORK PACKET DETECTED")

    print("=" * 55)

    print("Source IP      :", src)
    print("Destination IP :", dst)
    print("Protocol       :", protocol)
    print("Packet Size    :", len(packet), "bytes")

    # TCP details
    if packet.haslayer(TCP):

        print("Source Port    :", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)
        print("TCP Flags      :", packet[TCP].flags)

    # UDP details
    elif packet.haslayer(UDP):

        print("Source Port    :", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)

    # ICMP details
    elif packet.haslayer(ICMP):

        print("ICMP Type      :", packet[ICMP].type)
        print("ICMP Code      :", packet[ICMP].code)

    # ARP details
    elif packet.haslayer(ARP):

        print("ARP Operation  :", packet[ARP].op)

    # Payload analysis
    display_payload(packet, show_payload)

    print("=" * 55)


# Start packet capturing
def start_sniffer(interface, count, packet_filter, show_payload):

    print("\n===================================")
    print("       PYTHON NETWORK SNIFFER")
    print("===================================")

    print("Interface :", interface or "Default")
    print("Packet Limit:", count or "Unlimited")
    print("Filter    :", packet_filter or "All supported traffic")
    print("\nStarting packet capture...\n")

    try:

        sniff(
            iface=interface,
            filter=packet_filter,
            prn=lambda packet: analyze_packet(
                packet, show_payload
            ),
            count=count,
            store=False,
            promisc=False
        )

    except PermissionError:

        print("Error: Administrator privileges required.")

    except Exception as error:

        print("Capture Error:", error)

    print("\nPacket capture completed.")


# Main program
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Python Network Packet Sniffer"
    )

    parser.add_argument(
        "-i", "--interface",
        help="Network interface to capture"
    )

    parser.add_argument(
        "-c", "--count",
        type=int,
        default=0,
        help="Number of packets to capture (0 = unlimited)"
    )

    parser.add_argument(
        "-f", "--filter",
        default="",
        help="BPF filter, e.g. tcp or udp"
    )

    parser.add_argument(
        "--show-payload",
        action="store_true",
        help="Display a limited payload preview"
    )

    args = parser.parse_args()

    start_sniffer(
        args.interface,
        args.count,
        args.filter,
        args.show_payload
    )
