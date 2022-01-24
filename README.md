# Spaceport
Spaceport is a full stack website which allows users to access satellite imagery of the Earth.  Users can create a tasking pipeline which will deliver images of the specified area when they are available.  The website was developed for Milestone 4 as part of the Code Institute Diploma in Software Developement. 

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
This website is based on a technical concept of access satellite imagery, therefore see below some useful definitions which may be used in this document.
These definitions can also be found on the Discover website page.
- Pipeline: a pipeline refers to the timeline, or projected plan, of receiving satellite images. Each object in the 'List' model represents a pipeline.  Pipelines are active if they have not completed all intervals, and complete if all intervals have been completed
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

##### User
- The User model contains information about the user, as part of the Django allauth library
- No additional features are added to this model, as a basic username and password satisfy the requirements of the project
- The model fields are: 

##### List
- The List model contains information about the pipeline the user set up
- The model fields are: pipeline_name, pipeline_description, start_date, end_date, interval, output_image, aoi, cloud_cover, num_intervals, date_created, aoi_area, created_by, status, api_id, num_results, num_images, results_updated, featured_image, time_edited


##### Result
- The Result model contains information about results relating to the pipeline.  The number of results for a pipeline is directly linked to the number of intervals a pipeline has. Example: if a pipeline is 5 days in length, with an interval of 1 day, there will be 5 intervals (1 for each day), and thus 5 results.
- It contains the List as the foreign key.
- The model fields are: 

