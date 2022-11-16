#!/bin/bash

echo "Current date and time: `date`"
echo "Current user: `whoami`"
echo "Hostname: `hostname`"
echo "Internal IP Address: `ifconfig | grep -Eo '(addr:)?([0-9]*\.){3}[0-9]*' | tr '\n' ' ' | cut -d " " -f 2`"  
echo "External IP Address: `dig +short myip.opendns.com @resolver1.opendns.com`"  
echo "Name and version of Linux Dist: `uname -rs`"
echo "System uptime: `uptime`"
echo "Information about used/free space(GB)"
sudo df -H | head -n 2
echo "Information about total/free RAM: `top -l 1 | grep PhysMem`"
echo `system_profiler SPHardwareDataType | grep "Processor Speed" && echo "Cores: " && sysctl -n hw.ncpu`