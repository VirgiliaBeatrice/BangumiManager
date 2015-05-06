#!/usr/bin/python  
#-*-coding:utf-8-*-
'''
Created on 2015年5月6日

@author: VirgiliaBeatrice
'''

import sqlite3
from macpath import curdir

conn = sqlite3.connect(u'test.db')

with conn:
    cursor = conn.cursor()
    cursor.execute(u"CREATE TABLE Users(Id INT, Name TEXT)")
    cursor.execute(u"INSERT INTO Users VALUES(1, 'Michelle')")
    cursor.execute(u"INSERT INTO Users VALUES(2, 'Sonya')")


if __name__ == '__main__':
    pass