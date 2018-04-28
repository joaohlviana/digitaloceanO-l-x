#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=/root/olxc/APIProject-07e3d3740737.json
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
cd /root/olxc
scrapy crawl olxinfo &> /root/olxc/logs/olxinfo_$(date +"%Y%m%d%H%M")
