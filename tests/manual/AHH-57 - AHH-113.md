## AHH-57 - AHH-113
#### Test the template for the building page

* **Success criteria**
    1. The building page displays the building title, address, map and complaint category counts.

* **Setup**
    1. Create a new building with with address X and choose 2 complaint categories

* **Test process**
    1. Go to the home page, find the building at address X on the map and click on the marker
    2. Make sure the building page shows up (ie no 404)
    3. Make sure the address for the building is X
    4. Make sure the complaint table contains two categories with the value 1 in each.
    5. Submit a complaint for address X again, and choose one of the previously selected complaint categories
    6. Go back to the building page, and make sure the complaint category now has the value 2
