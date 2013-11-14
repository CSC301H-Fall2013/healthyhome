## AHH-38 - AHH-120
#### Test change colour of markers on the map based on the number of complaints in building

* **Marker Color Meaning**
	1. a building with 1 issue complaint, marker color will set to green
	2. a building with 2 to 3 issues complaint, marker color will set to yellow
	3. a building with 4 or more issues complaint, marker color set to red

* **Success criteria**
	1. The map appears with different colour

* **Setup**
	1. Go to the home page at acornhh.herokuapp.com

* **Test process**
	1. Create a building with one issue complaint
		1. Make sure the marker color is green
	2. Create another complaint with three issues for that building
		2. make sure the marker color is yellow
	3. Create another complaint with one issues for that building
		3. make sure the marker color is yellow
	4. Create another complaint with three issues for that building
		4. make sure the marker color is red