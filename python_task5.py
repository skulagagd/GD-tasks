import argparse
import platform
import psutil
import cpuinfo
import sys
import os
import socket
 
parser = argparse.ArgumentParser(description="Display information about system",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--distro", action="store_true", help="Show informations about systems distribution")
parser.add_argument("-m", "--memory", action="store_true", help="Show informations about systems memory")
parser.add_argument("-c", "--cpu", action="store_true", help="Show informations about CPU")
parser.add_argument("-u", "--user", action="store_true", help="Show informations about user")
parser.add_argument("-l", "--load", action="store_true", help="Show informations about avg load")
parser.add_argument("-i", "--ipaddr", action="store_true", help="Show informations about IP address")
args = parser.parse_args()
config = vars(args)

if not len(sys.argv) > 1:
    print("No arguments provided, check --help")

if args.distro:
    print(f'System: {platform.uname()[0]} | Node: {platform.uname()[1]} | Release: {platform.uname()[2]} | Version: {platform.uname()[3]} | Machine: {platform.uname()[4]} |')

if args.memory:
    print(f'Total memory(GB): {psutil.virtual_memory()[0]/100000000} | Used memory(GB): {psutil.virtual_memory()[3]/100000000} | Free memory(GB): {psutil.virtual_memory()[4]/100000000}')

if args.cpu:
    print(f'CPU: {platform.processor()} {cpuinfo.get_cpu_info()["brand_raw"]}| Core number(phys): {psutil.cpu_count()} | Speed: {psutil.cpu_freq()}')

if args.user:
    print(f'User: {os.path.expanduser("~").split("/")[-1]}')

if args.load:
    print(f'Load avg(%): {os.getloadavg()}')

if args.ipaddr:
    print(f'IP address: {socket.gethostbyname(socket.gethostname())}')