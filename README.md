# What’s Contained in Each Folder/File:  

### models.py:  
Contains a class object for each county, useful for retrieving and searching for information about a certain county.  

### urls.py:  
Contains all the relevant paths used within the Django framework.  

### views.py:  
Contains code to execute within a Django framework.
- The yourlist function displays a personal list of counties.
- The savecounty and unsavecounty functions add or remove county items from the personal list of counties.
- The countyinformation function obtains the county name and executes code to display the appropriate information in countyinformation.html.  

### util.py:
Contains functions to return a list of all county entries in the folder and get a specific county from the folder. Both functions are used in views.py 


## The Static Folder:  
### map.js:  
Contains a javascript function to execute code when areas of the image map in index.html is clicked on. Contains another function to include the current time of Massachusetts under the image map in index.html.  

### styles.css:  
Contains CSS code to format the HTML to appear a certain way.  

## The templates/county Folder:  
### countyinformation.html:  
Animates and displays the converted Markdown2 content of a certain county. Contains an unsaved or saved button depending on whether the user is logged in or not.  

### index.html:  
The main page where an image map of Massachusetts is present and each county in the image is clickable to execute a function and display a modal popup which contains few key points about the county. In the modal, there is a "more info" button which if clicked on, takes you to countyinformation.html and displays even more information of the county.  
The map and the clickable contents are mobile responsive, where any adjustments to the screen width will change the size of the image map and adjust the coordinates of the clickable areas.  
There is a live, current time of Massachussets displayed under the image map.  
All of the content uses different kinds of animations.  

### layout.html:  
Contains the navigation panel code to extend and display in every other HTML file. Also contains links to the map resizer javascript, bootstrap stylesheets, w3 stylesheet (for animations), map.js, font awesome stylesheet (for icons used in the navigation panel).  

### login.html:  
Contains code for enabling users to log in where they can save/unsave counties, and access their personal list of counties after registering.  

### register.html:  
Contains code to create users so that they can log in, save/unsave counties, and access their personal list of counties.  

### yourlist.html:  
Displays a list of county names that have been saved/unsaved. Includes pagination, where a limit of 5 county names can be displayed in a page. Each county name can be clicked on so that the user can access more information about that county. Contains animation.  

## The entries folder:  
Contains a list of county information in the form of .md files. They will be converted from Markdown2 content to HTML and this be used in the countyinformation.html file.    


# Why this Project Satisfies the Distinctiveness and Complexity Requirements:  
The project extensively uses knowledge learned throughout the course. They include:  
- Using Django's models.py, urls.py, views.py (and other Django files).
- Uses extending HTML layouts, and several types of Jinja2 syntax.
- Obtains md files from a common folder and converts markdown2 content.
- Uses JavaScript for displaying the appropriate information.
- Uses image maps, area tags, and coordinates.
- Utilizing mobile-responsive elements.
- Utilizes animations
- Imports and uses functions such as login, register, is_anonymous
- Uses pagination
- Uses stylesheets such as Bootstrap, W3 schools
