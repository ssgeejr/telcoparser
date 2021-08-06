#!/usr/bin/env python3

import csv, time, sys, getopt, glob, os, datetime
import mysql.connector
from mysql.connector import connect, Error
from pathlib import Path




def loadRawData():

   with open('/opt/apps/telcodata/calllogs.csv', mode ='r')as file:
       csvFile = csv.reader(file)
       try:
           cnx = mysql.connector.connect(user='telco',
           password='telco',
           host='127.0.0.1',
           database='telco')
           print(cnx)
           mycursor = cnx.cursor()
           xref = "insert ignore into export (dateorig,timeorig,origipaddr,callingparty) values(%s,%s,%s,%s)"

           csvFile = csv.reader(file)
           count = 0

           for lines in csvFile:
              if count > 0:
                 # print('DateOrig: ' + lines[5])
                 # print('TimeOrig: ' + lines[6])
                 # print('OrigiIpAddr: ' + lines[9])
                 # print('CallingParty: ' + lines[10])
                  xrecord = (lines[5],lines[6],lines[9],lines[10]) 
                 # print(xref, xrecord)
                  mycursor.execute(xref, xrecord)
                  if (count % 1000) == 0:
                      cnx.commit()
                      print("commiting another 1000 records: " , count)
              count+=1
           cnx.commit()
           print("Total records loaded: " , count)
       except Error as e:
           print('Error at line: ', count)
           print('******** INPUT LINE **********')
           print(lines)
           print('******************************')


def main(argv):
   loadRawData()

if __name__ == "__main__":
    main(sys.argv[1:])
