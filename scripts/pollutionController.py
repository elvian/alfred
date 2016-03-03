#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

def getSoupAQHI():
	html = urlopen("http://www.aqhi.gov.hk/en/aqhi/past-24-hours-aqhi45fd.html?stationid=80")
	soup = BeautifulSoup(html, "lxml")
	return soup

def getLatestAQHI(dataTable):
	aqhiTable = dataTable.findAll('tr')[1].findAll('td')
	aqhi = {}
	aqhi['dateTime'] = aqhiTable[0].text
	aqhi['index'] = aqhiTable[1].text
	return aqhi

def getRawAQICN():
	source = urlopen("http://aqicn.org/?city=HongKong/Central/Western&widgetscript&lang=en&size=xsmall&id=56d839cf2ad376.29520771")
	source = source.read().decode('utf-8')
	return source

def getLatestAQICN(source):
	aqi = source.split("Air Pollution.")[1]
	aqi = aqi.split("title")[1]
	aqi = aqi.split("</div>")[0]
	aqi = aqi.split(">")[1]
	
	aqits = source.split("Updated on ")[1].strip()
	aqits = aqits.split("<")[0]

	aqhiData = {}
	aqhiData['index'] = aqi
	aqhiData['dateTime'] = aqits
	
	return aqhiData 
	
def getPollutionData():
	soupAQHI = getSoupAQHI()
	dataTableAQHI = soupAQHI.find('table', {'id' : 'dd_stnh24_table'})
	aqhi = getLatestAQHI(dataTableAQHI)
	
	rawAQICN = getRawAQICN()
	aqicn = getLatestAQICN(rawAQICN)
	
	data = {}
	data['AQHI'] = aqhi['index']
	data['AQHITS'] = aqhi['dateTime']
	data['AQICN'] = aqicn['index']
	data['AQICNTS'] = aqicn['dateTime']
	return data

def testModule():
	data = getPollutionData()
	print(data['AQHI']  + " " + data['AQHITS'] + " " + data['AQICN'] + " " + data['AQICNTS'])