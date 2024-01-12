import time
from pathlib import Path
from scapy.all import PcapReader, IP, Raw

pcap_path = Path("./fangede_pakker.pcap")

t0 = time.time()
flag = ""
with PcapReader(str(pcap_path)) as reader:
    for i, packet in enumerate(reader):
        if IP not in packet:
            print(f"No IP in packet {i}")
            packet.show()
            continue

        src = packet[IP].src
        dst = packet[IP].dst

        # https://en.wikipedia.org/wiki/Evil_bit
        evil = packet[IP]
        if "evil" in evil.flags:
            raw = Raw(packet[IP].payload)
            data = raw.load.decode()
            c = chr(int(data, 2))
            flag += c

t1 = time.time()
print(f"Timing: parse={t1 - t0:.2f}s")

print("Flag:", flag)

