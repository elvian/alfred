#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib.request import urlopen

def getSoup():
	html = urlopen("http://m.weather.gov.hk/report.htm")
	soup = BeautifulSoup(html)
	return soup

def getTemperature(summaryBlock):
	temperature = summaryBlock.split("Temp")[1].split("°")[0].strip()
	return temperature
	
def getHumidity(summaryBlock):
	humidity = summaryBlock.split("RH")[1].split("%")[0].strip()
	return humidity
	
def getUV(summaryBlock):
	uv = summaryBlock.split("UV Index")[1].split(" ")[1].strip()
	return uv

def getWeatherData():
	soup = getSoup()
	summaryBlock = soup.findAll('td', {'class' : 'list'})[0].text
	data = {}
	data['temperature'] = getTemperature(summaryBlock)
	data['humidity'] = getHumidity(summaryBlock)
	data['uv'] = getUV(summaryBlock)
	return data
	
data = getWeatherData()
print(data['temperature'] + " " + data['humidity'] + " " + data['uv'])