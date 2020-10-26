#!/usr/bin/python
import sys
import argparse
import datetime

TODAY = datetime.date.today().strftime("%Y%m%d")

FARGS = argparse.ArgumentParser(description='Generate Plow Count Queries')
FARGS.add_argument('--date', help='The date of the inserteddate= partition for tables (yyyymmdd)', default=TODAY)
FARGS.add_argument('--table', help='The Plow table to get counts of', default='plow_testmedia_monitor')
FARGS.add_argument('--out', help='Output SQL queries to output file', default='./output.hql')
def print_sql(dt,tbl,out):
    qtemp = "select '%%DATE%%', '%%TIME1%%', '%%TIME2%%', count(*) from %%TABLE%% where inserteddate = '%%DATE%%' and time >= '%%TIME1%%' and time <= '%%TIME2%%' group by 1,2,3,4;"
    qtemp = qtemp.replace('%%TABLE%%',tbl)
    querylst = []
    for hr in range(24):
        strhr = str(hr)
        strhr = strhr.rjust(2,'0')
        time1 = strhr + ':00:00'
        time2 = strhr + ':30:00'
        time3 = time2
        nxthr = hr + 1
        strnxthr = str(nxthr)
        strnxthr = strnxthr.rjust(2,'0')
        time4 = strnxthr + ':00:00'
        timesql1 = qtemp.replace('%%TIME1%%', time1)
        timesql1 = timesql1.replace('%%TIME2%%', time2)
        timesql1 = timesql1.replace('%%DATE%%',dt)
        timesql2 = qtemp.replace('%%TIME1%%', time3)
        timesql2 = timesql2.replace('%%TIME2%%', time4)
        timesql2 = timesql2.replace('%%DATE%%',dt)
        querylst.append(timesql1)
        querylst.append(timesql2)
    with open(out, "wt") as fh:
        for query in querylst:
            fh.write(query + "\n")

def main(argv):
    global ARGS
    ARGS = FARGS.parse_args(argv[1:])
    #dt = '20201024'
    #tbl = 'plow_testmedia_monitor' 
    #tbl = 'plow_mediahuis_nieuwsblad_canary'
    # usage: "print_plow_table_counts.py" [date] [plow table] [output file]  
    print_sql(ARGS.date, ARGS.table, ARGS.out)


if __name__ == '__main__':
    main(sys.argv)
