#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alicia Wang
Outputs HTML file
"""

import glob
import os
import json
import csv

#os.remove("new.html")
#print("Old file removed.")

f = open('new.html','w')
print("New file created. Inputting information...")

import csv
file = open('opencoding.csv')
reader = csv.reader(file)
data = list(reader)

numrows = 108
numcolumns = 54

f.write('<div id="options">\n')
c = 3
topics = 0
div = ''
while (c < numcolumns):
    if data[0][c] != '':
        topics+=1
        if topics != 1:
            div += '</div>\n'
        div += '<div class="option-set" data-group="' + data[0][c] + '">\n'
        div += '<input type="checkbox" value="" id="' + data[0][c] + '-all" class="all" checked /><label for="' + data[0][c] + '-all">all ' + data[0][c] + '</label>\n'
        div += '<input type="checkbox" value=".' + data[2][c] + '" id="' + data[2][c] + '" /><label for="' + data[2][c] + '">' + data[2][c] + '</label>\n'
    else:
        div += '<input type="checkbox" value=".' + data[2][c] + '" id="' + data[2][c] + '" /><label for="' + data[2][c] + '">' + data[2][c] + '</label>\n'
    c+=1

div += '</div>\n </div>\n'
f.write(div)

f.write('<p id="filter-display"></p> <div id="container">\n')


for r in range(3,numrows):
    addons = ''
    for c in range(0,numcolumns):
        if data[r][c] == "x" or data[r][c] == "xxx":
            addons += ' ' + data[2][c]
    item = '<div class="iso-box item' + addons + ' col-md-4 col-sm-6"> \n<div class="portfolio-thumb">\n'
    item += ' <img src="imagesdeardata/' + data[r][2] + '_DearData_'
    if len(data[r][1]) <= 1:
        item += '0' + data[r][1]
    else:
        item += data[r][1]
    if data[r][2] == "Stefanie":
        item += '+'
    else:
        item += '_'
    item += 'Front.jpg" class="img-responsive" alt="Portfolio">\n'
    item += '<div class="portfolio-overlay"> <div class="portfolio-item">\n'
    item += '<h2>Week of ' + data[r][0] + '</h2>\n'
    item += '<h2>Week ' + data[r][1] + '</h2>\n'
    item += '<h2>' + data[r][2] + '</h2>\n' + '</div> </div> </div> </div>\n'
    f.write(item)
f.write('</div>')

#+ data[r][0] + data[r][1] + data[r][2] + 