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
import re

os.remove("new.html")
print("Old file removed.")
import csv
file = open('opencoding.csv')
reader = csv.reader(file)
data = list(reader)

#creating html for filter
f = open('new.html','w')
print("New file created. Inputting information...")

#107, 54
numrows = 107
numcolumns = 54

print('CREATING CHECKBOXES.')
#CREATING CHECKBOXES

c = 3
topics = 0
div = ''

additions = '''
<div class="col-md-3"> 
    <div class="card mb-4"> 
        <div class="card-header"><a role="button" data-toggle="collapse" href="#who" aria-expanded="false" aria-controls="Who">Who</a></div> 
          <div id="who" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="who">
                <ul class="list-group list-group-flush">
                      <li class="list-group-item"> 
                    <div class="option-set" data-group="Giorgia"><input type="checkbox" value=".Giorgia" id="Giorgia" /> 
                    <label for="Giorgia">Giorgia</label></div> 
                    </li>
                    <li class="list-group-item"> 
                    <div class="option-set" data-group="Stefanie"><input type="checkbox" value=".Stefanie" id="Stefanie" /> 
                    <label for="Stefanie">Stefanie</label></div> 
                    </li>
              </ul> 
          </div>
    </div> 
    </div>
'''

while (c < numcolumns):
    if data[0][c] != '':
        if topics != 0:
            div += '</ul> </div> </div> </div>'
        topics+=1
        div += '<div class="col-md-3">  <div class="card mb-4">  <div class="card-header">'
        div += '<a role="button" data-toggle="collapse" href="#' + ''.join(e for e in data[0][c] if e.isalnum()) + '" aria-expanded="false" aria-controls="' + ''.join(e for e in data[0][c] if e.isalnum()) + '">'
        div += data[0][c] + ' </a> </div>'
        div += '<div id="' + ''.join(e for e in data[0][c] if e.isalnum()) + '" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="' + ''.join(e for e in data[0][c] if e.isalnum()) + '">'
        div += '<ul class="list-group list-group-flush">'
    div += '<li class="list-group-item">  <div class="option-set" data-group="' + ''.join(e for e in data[2][c] if e.isalnum()) + '">'
    div += '<input type="checkbox" value=".' + ''.join(e for e in data[2][c] if e.isalnum()) + '" id="' + ''.join(e for e in data[2][c] if e.isalnum()) + '" />  <label for="' + ''.join(e for e in data[2][c] if e.isalnum()) + '">' + data[2][c] + ' <span class="filter-count"></span></label>'
    div += '</div>  </li>'
    c+=1

div += '</ul> </div> </div> </div> </div>'

print topics

f.write(additions)
f.write(div)
f.write('<h3>Filter selections: </h3><p class="large" id="filter-display"></p> <p id="filter-count"></p> <p id="gpercentages"></p> <p id="spercentages"></p>  </div>  </div>  <div class="container">  <div class="row" id="container"> ')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print('CREATING PICTURES.')
#CREATING PICTURES AND MODALS
section=''
for r in range(3,numrows):
    addons = ''
    properties = ''
    item = ''
    name = data[r][2]
    topic = data[r][0]
    number = data[r][1]
    title = 'Week ' + number + ': ' + topic + '; ' + name
    for c in range(2,numcolumns):
        if data[0][c] != '':
            properties += ' <strong>' + data[0][c] + '</strong>: '
        if data[r][c] == "x" or data[r][c] == "xxx" or data[r][c] == "new":
            addons += ' ' + ''.join(e for e in data[2][c] if e.isalnum())
            properties += data[2][c]
            if c < numcolumns or data[0][c+1] == '':
                properties += ', '
        if data[r][c] == "Giorgia" or data[r][c] == "Stefanie":
            addons += ' ' + ''.join(e for e in data[r][c] if e.isalnum())
    item += '<div class="col-md-3 item' + addons + ' ">'
    imgsrc = '/' + name + '_DearData_'
    if len(data[r][1]) <= 1:
        imgsrc += '0' + number
    else:
        imgsrc += data[r][1]
    if data[r][2] == "Stefanie":
        imgsrc += '+'
    else:
        imgsrc += '_'
    item += '<div class="card mb-4">  <a href="imagesdeardata' + imgsrc + 'Front.jpg" target="_blank"><img class="card-img-top" src="thumbimages' + imgsrc + 'Front.jpg"></a>'
    item += '<div class="card-body">  <h5 class="card-title">' + title + '</h5>'
    item += '<div class="d-flex justify-content-between align-items-center">  <div class="btn-group">'
    item += '<button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#' + name + number + '">See legend</button>'
    item += '</div>  </div>  </div>  </div>  </div>'
    f.write(item)

    section += '<div class="modal fade" id="' + name + number + '" tabindex="-1" role="dialog" aria-labelledby="' + name + number + '" aria-hidden="true">'
    section += '<div class="modal-dialog modal-lg" role="document">  <div class="modal-content">  <div class="modal-header">  <h5 class="modal-title" id="' + name + number + '">'
    section += title + '</h5>'
    section += '<button type="button" class="close" data-dismiss="modal" aria-label="Close">  <span aria-hidden="true">&times;</span>  </button>  </div>  <div class="modal-body">'
    section += '<a href="imagesdeardata' + imgsrc + 'Front.jpg" target="_blank"><img class="large" src="thumbimages' + imgsrc + 'Front.jpg"></a>'
    section += '<a href="imagesdeardata' + imgsrc + 'Back.jpg" target="_blank"><img class="large" src="thumbimages' + imgsrc + 'Back.jpg"></a>'
    section += '<p>' + properties + '</p>'
    section += ' </div>  </div>  </div>  </div>'

f.write('</div></div>')
f.write(section)
f.close

print('thank you come again')
'''



<div class="container">
          <!--Starts the filtering table with checkboxes-->

      <h2>Filtering the visualizations</h2>

      <div class="row">      

        <!--filters-->

        </div>
      </div>

      
      <div class="container" id="container">
        <div class="row">
            <p id="filter-display">  </p>
        
          <!--card and modal-->


          </div>
        </div>



<!--Filter Group-->
        <div class="col-md-3">
            <div class="card mb-4">
                <div class="card-header">
                  Data Group
                </div>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">  <div class="option-set" data-group="ExternalPeople">
                      <input type="checkbox" value=".ExternalPeople" id="ExternalPeople" />  <label for="ExternalPeople">External: People</label>
                      </div>  </li>
                  <li class="list-group-item">  <div class="option-set" data-group="InternalSelfReflection">
                      <input type="checkbox" value=".InternalSelfReflection" id="InternalSelfReflection" />  <label for="InternalSelfReflection">Internal: Self-Reflection</label>
                      </div>  </li>
                  <li class="list-group-item">  <div class="option-set" data-group="ExternalPeople">
                      <input type="checkbox" value=".ExternalPeople" id="ExternalPeople" />  <label for="ExternalPeople">External: People</label>
                      </div>  </li>
                </ul>
              </div>
          </div>
          <!--Filter Group End-->

<!-- Card -->
          <div class="col-md-3 item ExternalPhysicalObjectsEnvironments Nominal Temporal When Why How Highlighting Attribute Grid Stacked Shape Position Dot Glyph">
              <div class="card mb-4">
                <img class="card-img-top" src="imagesdeardata/Giorgia_DearData_01_Front.jpg">
                <div class="card-body">
                    <h5 class="card-title">Week 1: Clocks; Giorgia</h5>
                  <div class="d-flex justify-content-between align-items-center">
                    <div class="btn-group">
                      <button type="button" class="btn btn-sm btn-outline-secondary" data-toggle="modal" data-target="#week1Giorgia">See legend</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Modal -->
          <div class="modal fade" id="week1Giorgia" tabindex="-1" role="dialog" aria-labelledby="week1GiorgiaLabel" aria-hidden="true">
              <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title">Week 1: Clocks; Giorgia</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                          <img class="large" src="imagesdeardata/Stefanie_DearData_01+Front.jpg"/>
                          <img class="large" src="imagesdeardata/Stefanie_DearData_01+Back.jpg"/>
                          <p>  </br>  <strong>Theme</strong>: External: Physical Objects/Environments, Nominal, </br>  <strong>Data</strong>: Temporal, </br>  <strong>Sematic</strong>: </br>  <strong>Context</strong>: When, How, </br>  <strong>Visual Annotation</strong>: </br>  <strong>Visual Layout</strong>: Radial, Shape, </br>  <strong>Visual Encoding Channels</strong>: Position, Orientation, </br>  <strong>Visual Marks</strong>: Glyph, </p>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                      </div>
                </div>
              </div>
            </div>






      <div class="row">
        <div class="col-md-12" id="options">
          <table class="table table-striped">
            <thead>
              <tr>
                <th>Data Group</th>
                <th>Data Group</th>
                <th>Data Group</th>
                <th>Data Group</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>  <div class="option-set" data-group="InternalSelfReflection">
                    <input type="checkbox" value=".InternalSelfReflection" id="InternalSelfReflection" />  <label for="InternalSelfReflection">Internal: Self-Reflection</label>
                    </div>  </td>
                <td>  <div class="option-set" data-group="ExternalPeople">
                    <input type="checkbox" value=".ExternalPeople" id="ExternalPeople" />  <label for="ExternalPeople">External: People</label>
                    </div>  </td>
                <td>  <div class="option-set" data-group="ExternalPhysicalObjectsEnvironments">
                    <input type="checkbox" value=".ExternalPhysicalObjectsEnvironments" id="ExternalPhysicalObjectsEnvironments" />  <label for="ExternalPhysicalObjectsEnvironments">External: Physical Objects/Environments</label>
                    </div>  </td>
                <td>  <div class="option-set" data-group="Nominal">
                    <input type="checkbox" value=".Nominal" id="Nominal" />  <label for="Nominal">Nominal</label>
                    </div>  </td>
              </tr>
              <tr>
                  <td>  <div class="option-set" data-group="InternalSelfReflection">
                      <input type="checkbox" value=".InternalSelfReflection" id="InternalSelfReflection" />  <label for="InternalSelfReflection">Internal: Self-Reflection</label>
                      </div>  </td>
                  <td>  <div class="option-set" data-group="ExternalPeople">
                      <input type="checkbox" value=".ExternalPeople" id="ExternalPeople" />  <label for="ExternalPeople">External: People</label>
                      </div>  </td>
                  <td>  <div class="option-set" data-group="ExternalPhysicalObjectsEnvironments">
                      <input type="checkbox" value=".ExternalPhysicalObjectsEnvironments" id="ExternalPhysicalObjectsEnvironments" />  <label for="ExternalPhysicalObjectsEnvironments">External: Physical Objects/Environments</label>
                      </div>  </td>
                  <td>  <div class="option-set" data-group="Nominal">
                      <input type="checkbox" value=".Nominal" id="Nominal" />  <label for="Nominal">Nominal</label>
                      </div>  </td>
                </tr>
                <tr>
                    <td>  <div class="option-set" data-group="InternalSelfReflection">
                        <input type="checkbox" value=".InternalSelfReflection" id="InternalSelfReflection" />  <label for="InternalSelfReflection">Internal: Self-Reflection</label>
                        </div>  </td>
                    <td>  <div class="option-set" data-group="ExternalPeople">
                        <input type="checkbox" value=".ExternalPeople" id="ExternalPeople" />  <label for="ExternalPeople">External: People</label>
                        </div>  </td>
                    <td>  <div class="option-set" data-group="ExternalPhysicalObjectsEnvironments">
                        <input type="checkbox" value=".ExternalPhysicalObjectsEnvironments" id="ExternalPhysicalObjectsEnvironments" />  <label for="ExternalPhysicalObjectsEnvironments">External: Physical Objects/Environments</label>
                        </div>  </td>
                    <td>  <div class="option-set" data-group="Nominal">
                        <input type="checkbox" value=".Nominal" id="Nominal" />  <label for="Nominal">Nominal</label>
                        </div>  </td>
                  </tr>
            </tbody>
          </table>
        </div>
      </div>

      <p id="filter-display">  </p>
      <div class="container" id="container">

          <!-- Card -->
          <div class="card item ExternalPhysicalObjectsEnvironments Nominal Temporal When Why How Highlighting Attribute Grid Stacked Shape Position Dot Glyph col-md-4 col-sm-6" style="width: 18rem;">
              <img class="card-img-top small" src="imagesdeardata/Giorgia_DearData_01_Front.jpg">
              <div class="card-body">
                <h5 class="card-title">Week 1: Clocks; Giorgia</h5>
                <p class="card-text">Hmmmm</p>
                <a href="#" class="btn btn-primary" data-toggle="modal" data-target="#week1Giorgia">See Legend</a>
              </div>
            </div>

            <!-- Modal -->
          <div class="modal fade" id="week1Giorgia" tabindex="-1" role="dialog" aria-labelledby="week1GiorgiaLabel" aria-hidden="true">
              <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="week1GiorgiaLabel">Week 1: Clocks; Giorgia</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                      <img class="large" src="imagesdeardata/Stefanie_DearData_01+Front.jpg"/>
                      <img class="large" src="imagesdeardata/Stefanie_DearData_01+Back.jpg"/>
                      <p>  </br>  <strong>Theme</strong>: External: Physical Objects/Environments, Nominal, </br>  <strong>Data</strong>: Temporal, </br>  <strong>Sematic</strong>: </br>  <strong>Context</strong>: When, How, </br>  <strong>Visual Annotation</strong>: </br>  <strong>Visual Layout</strong>: Radial, Shape, </br>  <strong>Visual Encoding Channels</strong>: Position, Orientation, </br>  <strong>Visual Marks</strong>: Glyph, </p>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                  </div>
                </div>
              </div>
            </div>


'''

'''
print('CREATING MODALS.')
#CREATING MODALS

for r in range(3,numrows):
    section = ''
    properties = ''
    for c in range(0,numcolumns):
        if data[0][c] != '':
            properties += '</br>  <strong>' + data[0][c] + '</strong>: '
        if data[r][c] == "x" or data[r][c] == "xxx":
            properties += data[2][c]
            if c < numcolumns and data[0][c+1] != '':
                properties += ', '
    name = data[r][2]
    topic = data[r][0]
    number = data[r][1]
    section += '<section data-modal="' + name + number + '" class="modal-wrapper">'
    section += '<article class="modal-body">'
    section += '<header>  <h2>WEEK ' + number + ': ' + topic + '; ' + name + '</h2>  <a class="close">close</a>  </header>'
    section += '<div class="modal-main">'
    section += '<img src="imagesdeardata/' + name + '_DearData_'
    #create img src
    imgsrc = 'imagesdeardata/' + name + '_DearData_'
    if len(data[r][1]) <= 1:
        imgsrc += '0' + number
    else:
        imgsrc += data[r][1]
    if data[r][2] == "Stefanie":
        imgsrc += '+'
    else:
        imgsrc += '_'
    section += '<img src="' + imgsrc + 'Front.jpg"/>'
    section += '<img src="' + imgsrc + 'Back.jpg"/>'
    section += '<p>' + properties + '</p>'
    section += '</div>  <footer>  </footer>  </article>  </section>'
    f.write(section)
f.close
'''

'''
<section data-modal="form" class="modal-wrapper">
          <article class="modal-body">
            <header>
              <h2>WEEK 3: PUBLIC TRANSPORTATION; Giorgia</h2>
              <a class="close">close</a>
            </header>
            <div class="modal-main">
            <img src="imagesdeardata/Giorgia_DearData_01_Front.jpg">
            <img src="imagesdeardata/Giorgia_DearData_01_Back.jpg">
            <p>Visual Annotation: something something something</p>
            <p>Visual Content: something something something</p>
            </div>
            <footer>  </footer>
          </article>
        </section>
'''

'''
        if topics != 1:
            div += '</div>'
        div += '<div class="option-set" data-group="' + ''.join(e for e in data[0][c] if e.isalnum()) + '">  '
        div += '<input type="checkbox" value="" id="' + ''.join(e for e in data[0][c] if e.isalnum()) + '-all" class="all" checked />  <label for="' + ''.join(e for e in data[0][c] if e.isalnum()) + '-all">all ' + data[0][c] + '</label>'
        div += '<input type="checkbox" value=".' + ''.join(e for e in data[2][c] if e.isalnum()) + '" id="' + ''.join(e for e in data[2][c] if e.isalnum()) + '" />  <label for="' + ''.join(e for e in data[2][c] if e.isalnum()) + '">' + data[2][c] + '</label>'
    else:
        div += '<input type="checkbox" value=".' + ''.join(e for e in data[2][c] if e.isalnum()) + '" id="' + ''.join(e for e in data[2][c] if e.isalnum()) + '" />  <label for="' + ''.join(e for e in data[2][c] if e.isalnum()) + '">' + data[2][c] + '</label>'
    c+=1
'''