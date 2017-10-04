#This script preproess the data so that it can be read by JavaScript in main html file


import json
json_data = open('courseDataRaw.json').read()
data = json.loads(json_data)
count= 0

# Set course time span
for item in data:
	if item['Day_And_Time']!= " TBA To Be Arranged" and "Cancelled" and "TBA" not in item :
		aa,bb = item['Day_And_Time'].split()
		if  bb !="Cancelled":
			cc,dd = bb.split('-')
			start,ff= cc.split(':')
			end,gg = dd.split(':')
			if "00" not in gg:
				end = int(end)+1
			if "PM" in dd and "12" not in dd:
				end = int(end)+12
			if "PM" in cc and "12" not in cc:
				start = int(start)+12	
			item['starttime'] =int(start)
			item['endtime'] = int(end)
			# print item['starttime']
			count= count+1
	item['Day_And_Time']=item['Day_And_Time'].replace("MWF ","MoWeFr ").replace("MTuWTh ","MoTuWeTh ").replace("MW ","MoWe ").replace("WF ","WeFr ").replace("M ","Mo ").replace("W ","We ").replace("F ","Fr ")


# Set course capacity
for item in data: 	
	a,b = item['Capacity'].split('E')
	item['Capacity']=a
	c,d = item['Capacity'].split('of')
	c = int(c)
	d = int(d)
	if c>d:
		item['Capacity'] = c
	else:
		item['Capacity'] = d
	item['Capacity']=int(item['Capacity'])


# For the locations that are very close to each other, or two names representing the same place, combine them to only one 
duplicate_location= ["TA Studio","TA Lecture","TA Mainstage","TA 2nd Stage","TA Offices","TA Foundry",]
duplicate_location2=["Martial Arts","Fitness/Wellness","East Field","Dance Studio","E Racquet Ct","E Tennis Ct","E Racquet Ct","East Gym","OPERS Conference","50 Mtr Pool",]
for item in data: 
	if 'E Baskin' in item['Class_Location']:
		item['Class_Location']=item['Class_Location'].replace ('E Baskin','J Baskin Engr')
	for ii in duplicate_location:
		if ii in item['Class_Location']:
			item['Class_Location']= item['Class_Location']+'  (Theater Arts)'
	for ee in duplicate_location2:
		if ee in item['Class_Location']:
			item['Class_Location']= item['Class_Location']+'  (East field)'


with open('newCourseData.json', 'w') as outfile:
    json.dump(data, outfile)





