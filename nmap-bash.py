import os
from pathlib import Path
import pandas as pd
import argparse

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description='CSV to NMAP BASH')

parser.add_argument('-i', '--input', help='Input file', required=True)
parser.add_argument('-a', '--assesment', help='Name of the Assesment to name the ouput bash files', required=True)

tcp = "nmap -sSCV -vvv -Pn --top-ports=2000 "
udp = "nmap -sUCV -vvv -Pn --top-ports=20 "

scope_file = FILE_PATH + "/" + parser.parse_args().input
assesment =  parser.parse_args().assesment
output_folder = FILE_PATH


def scan_tcp(target):
    output_file = assesment + "_TCP.sh"
    with open(output_file, "w") as bash:
        for line in targets:
            target = line.rstrip()
            output_tcp = target + "_tcp"
            command_tcp = tcp + target + " -oA " + output_tcp
            command = command_tcp
            bash.write(command)
            bash.write("\n")


def scan_udp(target):
    output_file = assesment + "_UDP.sh"
    with open(output_file, "w") as bash:
        for line in targets:
            target = line.rstrip()
            output_udp = target + "_udp"
            command_udp = udp + target + " -oA " + output_udp
            command = command_udp
            bash.write(command)
            bash.write("\n")



df = pd.read_csv(scope_file)



with open(scope_file, "r") as targets:
    for line in targets:
        line = line.strip()
        line = line.split(",")
        target = line[0]
        scan_tcp(target)

with open(scope_file, "r") as targets:
    for line in targets:
        line = line.strip()
        line = line.split(",")
        target = line[0]
        scan_udp(target)