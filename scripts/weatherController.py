#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

def getJson():
	url = "http://www.hko.gov.hk/wxinfo/json/one_json.xml"
	jsonDic = json.loads(urlopen(url).read().decode('utf-8'))
	return jsonDic

def getTemperature(jsonArray):
	temperature = jsonArray["hko"]["Temperature"]
	return temperature
	
def getHumidity(jsonArray):
	humidity = jsonArray["hko"]["RH"]
	return humidity
	
def getCurrentUV(jsonArray):
	currentUV = jsonArray["RHRREAD"]["UVIndex"]
	return currentUV

def getForecastUV(jsonArray):
	forecastUV = jsonArray["FUV"]["ForecastTimeInfoMaxUV"]
	return forecastUV

def getWeatherData():
	jsonArray = getJson()
	
	data = {}
	data['temperature'] = getTemperature(jsonArray)
	data['humidity'] = getHumidity(jsonArray)
	data['uv'] = getCurrentUV(jsonArray)
	data['fuv'] = getForecastUV(jsonArray)
	return data
	
def testModule():
	data = getWeatherData()
	print(data['temperature'] + " " + data['humidity'] + " " + data['uv'] + " " + data['fuv'])