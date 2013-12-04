HealthyHome
===========

The HealthyHome project looks to develop an interactive mapping platform that would display sub-standard housing complaints captured by a number of outreach techniques (door to door, flyers, on line eblasts, and more) that would be sent into the interactive map through text messaging and through a web browser. The information would include minimum criteria to be determined, such as: mold and pest infestation, unit disrepair, heat problems, and security issues. The data will be displayed on a Google Map. The purpose of the interactive map would be to expose the huge amount of housing problems that exist in large Canadian Cities. Toronto will serve as a pilot site with the aim of broadening the project to Ottawa and eventually nation-wide. HealthyHome is a sister website of [Acorn Canada](https://www.acorncanada.org/).

[Live Website](acornhh.herokuapp.com)

### Requirements
- Google Maps API
- Disqus Account 
- Python 2.7
- Django 1.5.4
- dj-database-url 0.2.2
- dj-static 0.0.5
- django-form-utils 1.0.1
- django-toolbelt 0.0.1
- gunicorn 18.0
- psycopg2 2.5.1
- python-dateutil 2.2
- python-mimeparse 0.1.4
- six 1.4.1
- sqlparse 0.1.10
- static 0.4
- wsgiref 0.1.2

### Installation

1. Ensure that python 2.7 is installed on the web server.
    - Skip this step if python is already installed on the web server.
    - See http://www.python.org/getit for installation instructions.

2. Ensure that pip is installed on the web server.
    - Pip is a python package manager that will help install the requirements for healthyhome.
    - See http://www.pip-installer.org for installation instructions.

3. Upload the healthyhome files to the server using one of the following steps:
    1. FTP
        - Download an archive of the application from https://github.com/CSC301H-Fall2013/healthyhome/archive/master.zip.
        - Upload the archive to server and unzip it.
    2. Git
        - Use URL https://github.com/CSC301H-Fall2013/healthyhome.git

4. Install the packages required by healthyhome.
    - SSH into the server.
    - cd into the healthyhome directory.
    - Run `pip install -r requirements.txt` to install the requirements.

5. Follow the [Deploying Django](http://www.djangobook.com/en/2.0/chapter12.html) instructions to setup healthyhome for the current server environment.

### Submitting a Complaint
Replace http://www.example.com with the base URL (the URL healthyhome is accessible from) in the instructions below.

1. Report complaints at http://www.example.com/report.
2. Enter in a valid address, city and province. 
3. Select at least one problem to complain about.
4. Click submit.
5. Confirm the complaint, or go back to edit the address.

### Moderation
Replace http://www.example.com with the base URL (the URL healthyhome is accessible from) in the instructions.

1. Access the admin area of the website at http://www.healthyhome.com/admin
2. Login with default admin account 'healthyhome' and password 'fiber'.
3. Delete a building or complaint.
    - Delete a building by clicking on the 'Building' link, selecting the building, and choosing 'Delete selected buildings' from the Action dropdown.
    - Delete a complaint by clicking on the 'Complaint' link, selecting the complaint, and choosing 'Delete selected complaint' from the Action dropdown.

### Using the application
Replace http://www.example.com with the base URL (the URL healthyhome is accessible from) in the instructions.

Refer to the help page at http://www.example.com/help for instructions on using healthyhome.

### Disqus
Healthyhome uses Disqus for building page comments. By default, healthyhome is setup to work with the 'healthyhome' Disqus account. To change to a new account follow these steps.

1. Setup a Disqus account using http://disqus.com.
2. Edit the template page templates/complaints/building\_page.html, replacing the disqus_shortname variable with shortname associated with the new Disqus account.

To moderate comments, login to the Disqus account from (http://disqus.com).
