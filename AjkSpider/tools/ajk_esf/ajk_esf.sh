#! /bin/bash
export PATH=$PATH:/usr/local/bin
source /usr/local/crawler/dxc/venv/bin/activate
cd /usr/local/crawler/dxc/AnjukeSpider/AjkSpider

nohup scrapy crawl ajk_get_esf1 > /dev/null 2>&1 &
sleep 3m
a1 = ps x | grep ajk_get_esf1 | grep -v grep | awk '{print $1}'
kill -s 9 $a1

nohup scrapy crawl ajk_get_esf2 > /dev/null 2>&1 &
sleep 3m
a2 = ps x | grep ajk_get_esf2 | grep -v grep | awk '{print $1}'
kill -s 9 $a2

nohup scrapy crawl ajk_get_esf3 > /dev/null 2>&1 &
sleep 3m
a3 = ps x | grep ajk_get_esf3 | grep -v grep | awk '{print $1}'
kill -s 9 $a3

nohup scrapy crawl ajk_get_esf4 > /dev/null 2>&1 &
sleep 3m
a4 = ps x | grep ajk_get_esf4 | grep -v grep | awk '{print $1}'
kill -s 9 $a4

nohup scrapy crawl ajk_get_esf5 > /dev/null 2>&1 &
sleep 3m
a5 = ps x | grep ajk_get_esf5 | grep -v grep | awk '{print $1}'
kill -s 9 $a5

nohup scrapy crawl ajk_get_esf6 > /dev/null 2>&1 &
sleep 3m
a6 = ps x | grep ajk_get_esf6 | grep -v grep | awk '{print $1}'
kill -s 9 $a6

nohup scrapy crawl ajk_get_esf7 > /dev/null 2>&1 &
sleep 3m
a7 = ps x | grep ajk_get_esf7 | grep -v grep | awk '{print $1}'
kill -s 9 $a7

nohup scrapy crawl ajk_get_esf8 > /dev/null 2>&1 &
sleep 3m
a8 = ps x | grep ajk_get_esf8 | grep -v grep | awk '{print $1}'
kill -s 9 $a8

nohup scrapy crawl ajk_get_esf9 > /dev/null 2>&1 &
sleep 3m
a9 = ps x | grep ajk_get_esf9 | grep -v grep | awk '{print $1}'
kill -s 9 $a9

nohup scrapy crawl ajk_get_esf > /dev/null 2>&1 &

deactivate
