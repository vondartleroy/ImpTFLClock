# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:32:46 2013
Gets time to next Eastbound trains at West Kensington station
@author: yousaf
"""

import xml.etree.ElementTree as ET
import urllib
import json
import io

tflData= urllib.urlopen('http://cloud.tfl.gov.uk/TrackerNet/PredictionDetailed/D/WKN').read()
root = ET.fromstring(tflData)

TrainData = { 'dataTime': root[4].get('CurTime'), 'trainTimes':[]}

for child in root[4][1]:
    TrainData['trainTimes'].append(child.get('SecondsTo'))

#print(json.dumps(TrainData, indent=4))


with io.open('data.txt', 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(TrainData, ensure_ascii=False)))
