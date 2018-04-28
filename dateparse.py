#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb

import re
import datetime

def dateparse(strdate):
    dt_regex = re.search('([0-9]{2})\s([a-zA-Z]+)\s([0-9]{2})\:([0-9]{2})', row[1], re.IGNORECASE)
    if dt_regex:
        myDict = {
            "janeiro": "01",
            "fevereiro": "02",
            "março": "03",
            "abril": "04",
            "maio": "05",
            "junho": "06",
            "julho": "07",
            "agosto": "08",
            "setembro": "09",
            "outubro": "10",
            "novembro": "11",
            "dezembro": "12",
            "Janeiro": "01",
            "Fevereiro": "02",
            "Março": "03",
            "Abril": "04",
            "Maio": "05",
            "Junho": "06",
            "Julho": "07",
            "Agosto": "08",
            "Setembro": "09",
            "Outubro": "10",
            "Novembro": "11",
            "Dezembro": "12"
        }
        mysqldate = '{}-{}-{} {}:{}:00'.format(
            datetime.datetime.now().year,
            myDict[dt_regex.group(2)],
            dt_regex.group(1),
            dt_regex.group(3),
            dt_regex.group(4)
        )
        return mysqldate
    else:
        return "0000-00-00 00:00:00"

con = MySQLdb.connect(host='216.172.172.55', user='toyop187', passwd='1mq90nC3jO', db='toyop187_olxc')
c = con.cursor()

c.execute('SELECT id, dt_insert FROM olxinfo WHERE dt_parse is null ORDER BY id DESC')
rows = c.fetchall()
for row in rows:
    c.execute("UPDATE olxinfo SET dt_parse = '%s' WHERE id = %s" % (dateparse(row[1]), row[0]))
    print(str(row[0])+"\t"+str(row[1])+"\t"+str(dateparse(row[1])))
    
con.commit()