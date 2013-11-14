## AHH-36 - AHH-105
#### Test the map for the existence of the category filter

* **Success criteria**
	1. The map shows checkboxes for each complaint category
* **Setup**
	1. Empty the buildings database

* **Test process**
	1. Create a new complaint for a building with any address L with complaint category X
	2. Go to the home page
		* Make sure the categories container has exactly one category X with a checkbox next to it
	3. Create a new complaint for a building with address L with complaint category Y
		* Make sure the categories container lists exactly two categories: X and Y
	4. Repeat step 3
		* Make sure the categories container lists exactly two categories: X and Y
	5. Create a new complaint for a building with address M with complaint category Y
		* Make sure the categories container lists exactly two categories: X and Y
	6. Create a new complaint for a building with address L with complaint category Z
		* Make sure the categories container lists exactly three categories: Y, Z and Z
		

* **Note**
	* Categories Y,Z and Z are any distinct categories listed on the complaint submission website
	* Addresses L and M are valid street addresses
