#!/usr/bin/env python
#tests

import weatherController
import pollutionController

def testWeather():
	data = weatherController.getWeatherData()
	print("Temperature is: " + data['temperature'])
	print("Humidity is: " + data['humidity'])
	print("UV is: " + data['uv'])
	print("Forecast UV is: " + data['fuv'])


def testPollution():
	data = pollutionController.getPollutionData()
	print("AQHI index is: " + data["AQHI"]) 
	print("AQHI timestamp is: " + data["AQHITS"]) 
	print("AQICN index is: " + data["AQICN"]) 
	print("AQICN timestamp is: " + data["AQICNTS"]) 

testWeather()
testPollution()