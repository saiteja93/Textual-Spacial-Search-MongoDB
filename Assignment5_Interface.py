#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Assignment3 Interface
# Name: Saiteja Sirikonda



from pymongo import MongoClient
import os
import sys
import json
import math

def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
	#try:
		#print 2000
		data = collection.find()
		#print len(data)
		with open(saveLocation1,"wb") as f1:
			#print 0
			for row in data:
				#print 1
				current_city = row['city']
				#print current_city
				if cityToSearch == current_city: #not checking for the lower/upper case regex equation
					Name = row['name']
					FullAddress = row['full_address'].replace("\n",",")
					State = row['state']
					output_entry = Name+"$"+FullAddress+"$"+current_city+"$"+State
					#print output_entry
					f1.write(output_entry.encode('utf-8')+"\n")
	
	#except EXCEPTION as detail:
		#print detail

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
	#try:
		data = collection.find()
		print data.count()

		f2= open(saveLocation2,"w")

		#count = 0
		b = categoriesToSearch
		for row in data:
			#for category in row['categories']:
			a = row['categories']
			if set(a).intersection(b): #checks if the two lists have any intersection and returns true if it does
					lat1 = row["latitude"]
					lon1 = row["longitude"]
					lat2 = myLocation[0]
					lon2 = myLocation[1]
					dis = Distance(float(lat1),float(lon1),float(lat2),float(lon2))
					#print dis, row['categories']
					if dis <= maxDistance:
						Name = row['name']
						#print "Its entering"
						#count = count + 1
						f2.write(Name.encode("utf-8") + "\n")
					

		f2.close()
	
	#except EXCEPTION as detail:
		#print detail


#https://gist.github.com/rochacbruno/2883505 
#the following code was taken from the above link to suite the requirements of the assignment
def Distance(lat2, lon2, lat1, lon1):
    R = 3959
    latitude1 = math.radians(lat1)
    latitude2 = math.radians(lat2)
    #longitude2 = math.radians(lon2)
    #longitude1 = math.radians(lon1)
    diff_lat = math.radians(lat2-lat1)
    diff_long = math.radians(lon2-lon1)
    
    a = math.sin(diff_lat/2) * math.sin(diff_lat/2) + math.cos(latitude1) * math.cos(latitude2) * math.sin(diff_long/2) * math.sin(diff_long/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d
