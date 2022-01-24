# Spaceport
Spaceport is a full stack website which allows users to access satellite imagery of the Earth.  Users can create a tasking pipeline which will deliver images of the specified area when they are available.  The Skywatch API is used to access information about satellites, and set up the pipelines. The website was developed for Milestone 4 as part of the Code Institute Diploma in Software Developement. 

# Table of contents
- [Spaceport]
- [Definitions]
- [Project Overview]
- [UX]
    * Strategy
        + Site user
        + Admin
    * Structure
        + Pages
        + Database
    * Scope
- [Features]
    * Homepage
    * Discover
    * My Pipelines
    * Create Pipeline
    * Detail view
    * Edit
    * Delete
    * Account authentication
- [Technologies used]
- [Testing]
- [APIs]
    * Skywatch
    * Mapbox
- [Deployment]
- [Media]
- [Credits]
- [Acknowledgements]

# Project Overview
- This website was developed for submission as the Milestone 4 project of the Code Institute Diploma in Software Developement.
- The website is deployed using the Heroku pages at the following url:
- The repository on Github that contains the website source code and assets is available at the following url:
- The website was built with a responsive look and feel, designed to be enjoyable to use on all screen sizes.

# Definitions
This website is based on a technical concept of accessessing satellite imagery, therefore see below some useful definitions which may be used in this document.
These definitions can also be found on the Discover website page.
- Pipeline: a pipeline refers to the timeline, or projected plan or schedule, of receiving satellite images. Each object in the 'List' model represents a pipeline.  Pipelines are active if they have not completed all intervals, and complete if all intervals have been completed
- Interval:
- 


# UX
## Strategy
### Site User
The primary goals of the website user are as follows:
- To create an account on the website, which will allow them to create pipelines
- To create, update, edit and delete pipelines 
- To view the details of a pipeline they have created
- To view the schedule of receiving images
- To see a list of all their pipelines, ordered by status
- To understand the applications and purposes of satellite imagery

### Admin User


## Structure
### Pages
The website has five main pages, with user authentication on three:
- Homepage: to introduce users to the website and detail the purpose
- Discover: to allow users to explore the uses of satellite imagery
- My Pipelines: to list all pipelines created by the user
- View of pipeline: to display all details of the pipeline instance
- Create pipeline: to display an interactive form for creating a pipeline

The additional pages are as follows:
- Edit pipeline
- Delete pipeline
- Confirmation of deleted pipeline
- User authentication pages

The website was designed to be simple, clear and non-cluttered, basic in structure, with attractive images of satellites and images captured by satellites.
Bootstrap was used to aid responsiveness, as well as media queries in CSS.

### Database

- Spaceport App
- templates
- static
- README
- manage.py
- Procfile
- Requirements.txt

#### Database Model
Insert schema here.

#### Models
There are three models in this project.  As the project uses an API for a lot of the information stored in the databases, see the associated tables to understand how the data is created (whether by the User, the Spaceport app, or from the API)

##### User
- The User model contains information about the user, as part of the Django allauth library
- No additional features are added to this model, as a basic username and password satisfy the requirements of the project
- The model fields are: 

##### List
- The List model contains information about the pipeline the user set up
- The model fields are: pipeline_name, pipeline_description, start_date, end_date, interval, output_image, aoi, cloud_cover, num_intervals, date_created, aoi_area, created_by, status, api_id, num_results, num_images, results_updated, featured_image, time_edited

| Field | Description | Created from | Field type|
|-------|-------------|--------------|-----------|
|id|the primary key for this model, used to cross reference Result objects|Django|Primary Key|
|pipeline_name|the name the user gives to the pipeline|User| Charfield|
|pipeline_des|the description the user inputs to identify the pipeline|User| Charfield|
|start_date|what date the pipeline will start looking for images|User| Date|
|end_date|what date the pipeline will stop looking for images|User| Date|
|interval|the interval period set by the user (daily, biweekly, weekly, bimonthly, monthly)|User| Charfield|
|aoi|the coordinates for the Area of Interest chosen by the user|User| JSON|
|output_image|the type of images the pipeline should return|User|Charfield (choice of 6)|
|cloud_cover|the maximum allowable cloud cover in returned images|User|Charfield|
|num_intervals|the number of intervals between the start and end date|API|Charfield|
|date_created|the date the pipeline was created|Spaceport|Date|
|aoi_area|the area in km2 of the AOI|API|Charfield|
|created_by|the user the pipeline was created by|Spaceport|Charfield|
|status|whether the pipeline is active, complete, or pending|Spaceport|Charfield|
|api_id|the unique id given to the pipeline by the API|API|Charfield|
|num_results||||
|num_images|the number of images successfully received by the pipeline|Spaceport|Charfield|
|results_updated|when the pipeline was last refreshed from the API|API|Datetime|
|featured_image|a url to display an image on My Pipelines page|API|Charfield|
|time_edited|when the pipeline was last edited|Spaceport|Datetime|


##### Result
- The Result model contains information about results relating to the pipeline.  The number of results for a pipeline is directly linked to the number of intervals a pipeline has. Example: if a pipeline is 5 days in length, with an interval of 1 day, there will be 5 intervals (1 for each day), and thus 5 results.
- It contains the List as the foreign key.
- The model fields are: 

## Scope

### Site user stories (new and existing)

User story 1: As a **Site User** I can **navigate the site easily**
- 1.1: As a **New/returning Site User** I see **the navigation bar displayed on all pages** so that **I can see all accessible pages wherever I am**
- 1.2: As a **Returning Site User** I am **redicted to My Pipelines page when I log in** so that **the information relating to my account is immediately displayed**
- 1.3: As a **New/returning Site User** I see **the active page** so that **I know which page I am currently on**
- 1.4: As a **New/returning Site User** I am **presented with relevant link buttons** so that **I can navigate the pages in a logical manner**

User story 2: As a **Site User** I can **create an account** so that **I can start creating my own pipelines**

User story 3: As a **Site User** I can **access information on satellite imagery**
- 3.1: As a **New/returning Site User** I can **see at all times the Discover page link** so that **I can always refer to this page for more information**
- 3.2: As a **New Site User** I am **firstly directed to the homepage** so that **the purpose of the site is immediately clear to me**
- 3.3: As a **New/returning Site User** I can **explore technical terms associated with satellite imagery and pipelines** so that **I can check any definitions I am unsure of**
- 3.4: As a **New/returning Site User** I am **given explanations of technical terms in the form** so that **I understand what the parameters I am setting means**
- 3.5: As a **Site User** I am **provided with links to all image metadata** so that **I can use the images in post production**
- 3.6: As a **New/returning Site User** I can **read examples of pipelines created by current/previous clients** so that **I have a context as to what I can use satellite imagery for**
- 3.7: As a **New/returning Site User** I can **read topical events involving satellite imagery** so that **I am aware of the importance of being able to access satellite imagery**

User story 4: As a **Site User** I can **view a list of all my pipelines**
- 4.1: As a **Returning Site User** I can **see the My Pipelines link on the navbar when I am logged in** so that **I can easily refer back to this at all times**
- 4.2: As a **Returning Site User** I can **see all my pipelines ordered by active status** so that **I am aware which pipelines are still active**
- 4.3: As a **Returning Site User** I can **see all my pipelines ordered by completed status** so that **I am aware which pipelines have completed all intervals**
- 4.4: As a **Returning Site User** I can **see all my pipelines ordered by pending status** so that **I am aware which pipelines I should update**
- 4.5: As a **Returning Site User** I can **see a status link section at the top of My Pipelines** so that **I can see how many pipelines are in each category, and navigate to each list separately**
- 4.6: As a **Returning Site User** I can see **a card displaying important information about each pipeline** so that **I can identify which pipeline it refers to**
- 4.7: As a **Returning Site User** I can see **a featured image on the pipeline card** so that **I know if that pipeline has found any images**
- 4.8: As a **Returning Site User** I can see **an interactive style change when I hover over a pipeline** so that **I know I can click on the pipeline card and view pipeline details**
- 4.9: As a **New Site User** I am **shown a message at the top of My Pipelines, directing me to create a pipeline** so that **when first signing up, I am linked to the next logical step**

User story 5: As a **Site User** I can **view all details of a specific pipeline**
- 5.1: As a **Site User** I can **see that the detail view is separated into sections** so that **I can scroll to the section I am interested in**
- 5.2: As a **Site User** I can **see all important and general information at the top of the detail view** so that **I can identify which pipeline it refers to**
- 5.3: As a **Site User** I can **see a zoomable map of the AOI in the detail view** so that **I can see the area on the Earth this pipeline refers to**
- 5.5: As a **Site User** I can **see a timeline chart of my pipeline** so that **I can visualise the pipeline period, completed intervals, incomplete intervals, today's date and if/when images were found**
- 5.6: As a **Site User** I can **see a table of all interval dates** so that **I can see the status of each interval**
- 5.7: As a **Site User** I can **see a table of results** so that **I can easily see if images have been delivered**
- 5.8: As a **Site User** I am **directed to a separate tab when I click on a found image** so that **I can view it in detail and download it**
- 5.9: As a **Site User** I am **directed to a separate tab when I click on image metadata** so that **I can read it or use it in post production of the image**
- 5.10: As a **Site User** I can **view the parameters I selected when creating the pipeline** so that **I am reminded of the parameters I set**
- 5.11: As a **Site User** I can **see a timestamp on 'last edited** so that **I know if/when I edited the pipeline**
- 5.12: As a **Site User** I can **see buttons to edit/delete my pipeline** so that **I know how to access these functions**

User story 3: As a **Site User** I can ****
User story 3: As a **Site User** I can ****

### Admin

