#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib.request import urlopen

def getSoupAQHI():
	html = urlopen("http://www.aqhi.gov.hk/en/aqhi/past-24-hours-aqhi45fd.html?stationid=80")
	soup = BeautifulSoup(html)
	return soup

def getLatestAQHI(dataTable):
	aqhiTable = dataTable.findAll('tr')[1].findAll('td')
	aqhi = {}
	aqhi['dateTime'] = aqhiTable[0].text
	aqhi['index'] = aqhiTable[1].text
	
	return aqhi

def getSoupAQICN():
	html = urlopen("http://aqicn.org/city/hongkong/central/western/m/")
	soup = BeautifulSoup(html)
	return soup

def getLatestAQICN(dataTable):
	aqi = dataTable.find('div', {'class' : 'aqi'}).text
	
	aqits = dataTable.find('div', {'class' : 'headline item'}).findAll('div')[2].text
	aqits = aqits.split(" on ")[1].strip()
	
	aqhiData = {}
	aqhiData['dateTime'] = aqits
	aqhiData['index'] = aqi
	
	return aqhiData 
	
def getPollutionData():
	soupAQHI = getSoupAQHI()
	dataTableAQHI = soupAQHI.find('table', {'id' : 'dd_stnh24_table'})
	aqhi = getLatestAQHI(dataTableAQHI)
	
	soupAQICN = getSoupAQICN()
	dataTableAQICN = soupAQICN.find('div', {'id' : 'header'})
	aqicn = getLatestAQICN(dataTableAQICN)
	
	data = {}
	data['AQHI'] = aqhi
	data['AQICN'] = aqicn
	return data
	
data = getPollutionData()