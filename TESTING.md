# Testing


# User Story 1
As a **Site User** I can **navigate the site easily**

## User Story 1.1
- As a **New/returning Site User** I can **see the navigation bar displayed on all pages** so that **I can see all accessible pages wherever I am**

Steps:
1. Open Spaceport at the following link:
2. Open the Discover page
3. Open the Create page
4. Open the My Pipelines page
5. Resize the browser to see the navigation bar adjust to the screen width
6. Scroll down through longer pages

|Step|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|1|The homepage is displayed, with the nav bar fixed at the top|[Desktop](readme_img/US1.1_1_lg.JPG)|[Tablet](readme_img/US1.1_1_lg.JPG)|[Mobile](readme_img/US1.1_1_sm.JPG)|Passed|
|2|The Discover page is displayed, with the nav bar fixed at the top|[Desktop](readme_img/US1.1_2_lg.JPG)|[Tablet](readme_img/US1.1_2_md.JPG)|[Mobile](readme_img/US1.1_2_sm.JPG)|FAIL|
|3|The My Pipelines page is displayed, with the nav bar fixed at the top|[Desktop](readme_img/US1.1_3_lg.JPG)|[Tablet](readme_img/US1.1_3_md.JPG)|[Mobile](readme_img/US1.1_3_sm.JPG)|Pass|
|4|The Create pipeline form is displayed, with the nav bar fixed at the top|[Desktop](readme_img/US1.1_4_lg.JPG)|[Tablet](readme_img/US1.1_4_md.JPG)|[Mobile](readme_img/US1.1_4_sm.JPG)|Pass|
|5|When scrolling through all pages, the nav bar remains fixed at the top|[Desktop](readme_img/US1.1_5_lg.JPG)|[Tablet](readme_img/US1.1_5_md.JPG)|[Mobile](readme_img/US1.1_5_sm.JPG)|Pass|

## User Story 1.2
- As a **Returning Site User** I am **redicted to My Pipelines page when I log in** so that **the information relating to my account is immediately displayed**

Steps:
1. Click Login/Sign Up link on the nav bar to be redirected to the login/signup page
2. Enter Log in details; username and password, and click Sign In

|Step|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|1|The Login/Sign Up page is displayed|||||
|2|The My Pipelines page opens, displaying previously created pipelines||||

## User Story 1.3
As a **New/returning Site User** I can **see the active page** so that **I know which page I am currently on**

Steps:
1. 
2. 


## User Story 1.4
As a **New/returning Site User** I am **presented with relevant link buttons** so that **I can navigate the pages in a logical manner**

Steps:
1. Navigate to the homepage and scroll to the bottom to see prompts to explore the Discover page, or Sign Up
2. 

## User Story 1.5
As a **New/returning Site User** I can **see my login status in the nav bar** so that **I am aware if I am logged in**

|Step|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|-|In all pages, the user can see if they are logged in at the right of the navbar.|[Desktop](readme_img/US1.5 lg.JPG)|[Tablet](readme_img/US1.5_md.JPG)|[Mobile](readme_img/US1.5_sm.JPG)|





# User Story 1
As a **Site User** I can **create a pipeline**

- 1.1: As a **New/returning Site User** I can **see an introduction page to creating a pipeline** so that **I understand the restrictions**
- 1.2: As a **New/returning Site User** I can **see an advice on how to maximise my chance of my pipeline returning images** so that **I can choose my parameters accordingly**
- 1.3: As a **New Site User** I am **provided with a list of examples** so that **I have a starting point for my first pipeline**
- 1.4: As a **New/returning Site User** I am **made aware that submitting a pipeline does not guarantee results** so that **I am not disappointed if my pipeline does not receive images**
- 1.5: As a **New/returning Site User** I can **see a progress indicator on the form** so that **I know what my progress in the form is, and which sections I have completed**
- 1.6: As a **New/returning Site User** I can **see inline feedback on my form** so that **I know if the parameter I entered was incorrect**
- 1.7: As a **New/returning Site User** I can **see visual representations of relevant parameters** so that **I have a more accessible understanding of what I am selecting**
- 1.8: As a **New/returning Site User** I can **see descriptions/placeholders of parameters** so that **I know what this parameter means for my pipeline**
- 1.9: As a **New/returning Site User** I can **navigate forwards and backwards in the form** so that **I can change details before I submit**
- 1.10: As a **New/returning Site User** I can **review the details of the pipeline I have created** so that **I can review the details before I submit**
- 1.11: As a **New/returning Site User** I can **see which parameters can be changed after submission** so that **I am aware what can be edited**
- 1.12: As a **New/returning Site User** I have **feedback on submission** so that **I have confirmation that the pipeline was submitted**
- 1.13: As a **New/returning Site User** I am **redirected to the detail view of the pipeline after submission** so that **I can view the details of the pipeline I submitted**
- 1.14: As a **New/returning Site User** I am **encouraged to allow for the website to process the pipeline when first redirected** so that **I understand why the pipeline detail is initially sparse**

## Acceptance Criteria
- User can navigate form without concern
- User is aware when parameters they select are outwith acceptable range
- User is aware of the progress of the form, how much they have completed and when it is submitted
- User can review form before submitting
- Users are redirected to the detail view of this pipeline

## Testing
|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|1.1|Upon opening "Create" page, an introduction to creating a pipeline is displayed|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625901/Spaceport/Desktop/1.1_aw58u0.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644247/Spaceport/Mobile/1.1_sdwyje.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643503/Spaceport/Tablet/1.1_ru8qq0.jpg)|Pass|
|1.2|The form introduction gives advice on how to maximise chances of images|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625901/Spaceport/Desktop/1.2_rdxz5q.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644247/Spaceport/Mobile/1.4_f6nwdq.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643400/Spaceport/Tablet/1.4_zidylg.jpg)|Pass|
|1.3|For new/unfamiliar users, the form introduction suggests 3 starting points|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625900/Spaceport/Desktop/1.3_rkqnvr.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644247/Spaceport/Mobile/1.3_i7xxih.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643402/Spaceport/Tablet/1.3_esftdg.jpg)|Pass|
|1.4|The user can see that there is no guarantee for results in the satellite aquisition section|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643634436/Spaceport/Desktop/1.4_lrtmdn.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644247/Spaceport/Mobile/1.2_bi1o4u.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643400/Spaceport/Tablet/1.4_zidylg.jpg)|Pass|
|1.5|On all form pages, a process indicator shows number of steps, completed steps in darker turquoise, current step in dark grey, incomplete/future steps in light grey|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625900/Spaceport/Desktop/1.5_fd0uwc.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644248/Spaceport/Mobile/1.5_n0p1vo.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643400/Spaceport/Tablet/1.5_j4wggp.jpg)|Pass|
|1.6|Pages with invalid data display a message to inform the user, and do not allow form progression|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625901/Spaceport/Desktop/1.6_uka4iv.jpg) [Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643626582/Spaceport/Desktop/1.6_2_ag8uz9.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644249/Spaceport/Mobile/1.6_bavo1n.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643400/Spaceport/Tablet/1.6_n670cu.jpg)|Pass|
|1.7|Where relevant, pictures are shown to represent the form field value|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625902/Spaceport/Desktop/1.7_gkdnmg.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644250/Spaceport/Mobile/1.7_brxajo.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643400/Spaceport/Tablet/1.7_nfd7zo.jpg)|Pass|
|1.8|Form fields have placeholders, or default values|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625903/Spaceport/Desktop/1.8_grhwg6.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644249/Spaceport/Mobile/1.8_yndgiy.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643400/Spaceport/Tablet/1.8_yttfz1.jpg)|Pass|
|1.9|The form displays a progress indicator showing current page, and Previous and Next buttons to allow for easy form navigation|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625902/Spaceport/Desktop/1.9_vfabel.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644249/Spaceport/Mobile/1.9_ggqxpm.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643400/Spaceport/Tablet/1.9_xtqg7a.jpg)|Pass|
|1.10|The last form tab displays all user's form field values for the user to review|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625902/Spaceport/Desktop/1.10_wbjaas.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644249/Spaceport/Mobile/1.9_ggqxpm.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643401/Spaceport/Tablet/1.10_p06e4v.jpg)|Pass|
|1.11|The form review tab displays that the pipeline name and description can be changed after submission|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625902/Spaceport/Desktop/1.11_a0xwe7.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644250/Spaceport/Mobile/1.11_w1vmir.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643401/Spaceport/Tablet/1.11_g6pbh5.jpg)|Pass|
|1.12|The form displays a 'loading' screen to inform the user the pipeline is being set up. There are no CTAs available on this screen to prevent the user to click |[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643640246/Spaceport/Desktop/1.12_s4yg5q.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643640279/Spaceport/Tablet/1.12_wiubsh.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643640290/Spaceport/Mobile/1.12_cprncw.jpg)|Pass|
|1.13|After a few seconds on the loading screen, the user is redirected to the detail view of the pipeline|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643638899/Spaceport/Desktop/1.13_zh7gye.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643401/Spaceport/Tablet/1.13_oi1mpu.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643401/Spaceport/Tablet/1.13_oi1mpu.jpg)|Pass|
|1.14|The user is informed that pipelines can take a few minutes to set up, and they can update them when required to view full details|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643638899/Spaceport/Desktop/1.14_2_kmt7nv.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643644247/Spaceport/Mobile/1.14_x7utkk.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643402/Spaceport/Tablet/1.14_2_bum8ec.jpg)|Pass|


# User Story 2
As a **Site User** I can **view a list of all my pipelines**

- 2.1: As a **Returning Site User** I can **see the My Pipelines link on the navbar when I am logged in** so that **I can easily refer back to this at all times**
- 2.2: As a **Returning Site User** I can **see all my pipelines ordered by active status** so that **I am aware which pipelines are still active**
- 2.3: As a **Returning Site User** I can **see all my pipelines ordered by completed status** so that **I am aware which pipelines have completed all intervals**
- 2.4: As a **Returning Site User** I can **see all my pipelines ordered by pending status** so that **I am aware which pipelines I should update**
- 2.5: As a **Returning Site User** I can **see a status link section at the top of My Pipelines** so that **I can see how many pipelines are in each category, and navigate to each list separately**
- 2.6: As a **Returning Site User** I can see **a card displaying important information about each pipeline** so that **I can identify which pipeline it refers to**
- 2.7: As a **Returning Site User** I can see **a featured image on the pipeline card** so that **I know if that pipeline has found any images**
- 2.8: As a **Returning Site User** I can see **an interactive style change when I hover over a pipeline** so that **I know I can click on the pipeline card and view pipeline details**
- 2.9: As a **New Site User** I am **shown a message at the top of My Pipelines, directing me to create a pipeline** so that **when first signing up, I am linked to the next logical step**

## Acceptance Criteria
- All user pipelines are listed
- Pipelines are organized by status, and it is obvious how many pipelines are in each status category
- Only user pipelines are listed (cannot see any other user's, testing, or admin pipelines)
- Pipelines are clearly identified with name, description, date created


## Testing

|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|2.1|The 'Pipelines' page is displayed at all times in the navigation bar, underlined when it is the current page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648306/Spaceport/Desktop/2.1_doymna.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654314/Spaceport/Tablet/2.1_likui9.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653986/Spaceport/Mobile/2.1_vinsmc.jpg)|Pass|
|2.2|Active pipelines are in the Active section on My Pipelines page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648307/Spaceport/Desktop/2.2_sayoxy.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654315/Spaceport/Tablet/2.2_jcvgfh.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653986/Spaceport/Mobile/2.2_dtiwyz.jpg)|Pass|
|2.3|Complete pipelines are in the Complete section on My Pipelines page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648306/Spaceport/Desktop/2.3_p9vrb8.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654315/Spaceport/Tablet/2.3_sascef.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653986/Spaceport/Mobile/2.3_y303f3.jpg)|Pass|
|2.4|Pending pipelines are in the Pending section on My Pipelines page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648306/Spaceport/Desktop/2.4_f4vam0.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654316/Spaceport/Tablet/2.4_jhjczu.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653987/Spaceport/Mobile/2.4_qfztnn.jpg)|Pass|
|2.5|The sub navigation panel at the top displays number of pipelines in each status category, and provides a link to jump to the relevant status section|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648306/Spaceport/Desktop/2.1_doymna.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654316/Spaceport/Tablet/2.5_vkgqo8.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653986/Spaceport/Mobile/2.5_bqut87.jpg)|Pass|
|2.6|General pipeline information is displayed to identify the pipeline object|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648307/Spaceport/Desktop/2.6_w1j2px.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654315/Spaceport/Tablet/2.6_t88rly.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653987/Spaceport/Mobile/2.6_x4ghza.jpg)|Pass|
|2.7|If there is an image found, it is used as the featured image for that pipeline.  If there is no image, or the pipeline is 'pending', a placeholder image is used|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648307/Spaceport/Desktop/2.6_w1j2px.jpg) [Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648608/Spaceport/Desktop/2.7_2_oeok42.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654315/Spaceport/Tablet/2.6_t88rly.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653987/Spaceport/Mobile/2.6_x4ghza.jpg)|Pass|
|2.8|The image opacity is changed when the user hovers over the pipeline card|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648308/Spaceport/Desktop/2.8_inmtwv.png)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654316/Spaceport/Tablet/2.8_pynk3r.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653987/Spaceport/Mobile/2.8_wtlj8b.jpg)|Pass|
|2.9|Users with no pipelines are shown a message prompting them to create a pipeline|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643648308/Spaceport/Desktop/2.9_ak1wzx.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643654316/Spaceport/Tablet/2.9_krhhch.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643653987/Spaceport/Mobile/2.9_sk6kmq.jpg)|Pass|

## Acceptance Criteria Status
- [x] All user pipelines are listed
- [x] Pipelines are organized by status, and it is obvious how many pipelines are in each status category
- [x] Only user pipelines are listed (cannot see any other user's, testing, or admin pipelines)
- [x] Pipelines are clearly identified with name, description, date created

# User Story 3
As a **Site User** I can **view all details of a specific pipeline**

- 3.1: As a **Returning Site User** I can **see that the detail view is separated into sections** so that **I can scroll to the section I am interested in**
- 3.2: As a **Returning Site User** I can **see all important and general information at the top of the detail view** so that **I can identify which pipeline it refers to**
- 3.3: As a **Returning Site User** I can **click an Update button** so that **I can refresh the details of the pipeline**
- 3.4: As a **Returning Site User** I can **see a zoomable map of the AOI in the detail view** so that **I can see the area on the Earth this pipeline refers to**
- 3.5: As a **Returning Site User** I can **see a timeline chart of my pipeline** so that **I can visualise the pipeline period, completed intervals, incomplete intervals, today's date and if/when images were found**
- 3.6: As a **Returning Site User** I can **see a table of all interval dates** so that **I can see the status of each interval**
- 3.7: As a **Returning Site User** I can **see a table of results** so that **I can easily see if images have been delivered**
- 3.8: As a **Returning Site User** I am **directed to a separate tab when I click on a found image** so that **I can view it in detail and download it**
- 3.9: As a **Returning Site User** I am **directed to a separate tab when I click on image metadata** so that **I can read it or use it in post production of the image**
- 3.10: As a **Returning Site User** I can **view the parameters I selected when creating the pipeline** so that **I am reminded of the parameters I set**
- 3.11: As a **Returning Site User** I can **see a timestamp on 'last edited'** so that **I know if/when I edited the pipeline**
- 3.12: As a **Returning Site User** I can **see buttons to edit/delete my pipeline** so that **I know how to access these functions**
- 3.13: As a **Returning Site User** I am **told if I cannot edit/delete my pipeline** so that **I am aware why these functions are/are not available**

## Acceptance Criteria
- User is clearly aware which pipeline details they are looking at
- User is aware of the status and progress so far of the pipeline
- User can access how to update, edit or delete this pipeline
- User can see all relating results/images gathered by pipeline

## Testing

|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|3.1|When scrolling throught the detail view of the pipeline, the user can see the page divided into 5 sections|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658623/Spaceport/Tablet/3.1_kzrxk5.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658622/Spaceport/Tablet/3.1_2_xzjuhi.jpg) [Desktop 3](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658623/Spaceport/Tablet/3.1_3_vrzevw.jpg) [Desktop 4](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658623/Spaceport/Tablet/3.1_4_zy66vn.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658805/Spaceport/Tablet/3.1_s0raxv.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658803/Spaceport/Tablet/3.1_2_s8sehh.jpg) [Tablet 3](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658804/Spaceport/Tablet/3.1_3_gaeeu4.jpg) [Tablet 4](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658805/Spaceport/Tablet/3.1_4_ifi1cy.jpg) [Tablet 5](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658804/Spaceport/Tablet/3.1_5_fsnqks.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658677/Spaceport/Mobile/3.1_nqn7j7.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658676/Spaceport/Mobile/3.1_2_gxvm7h.jpg) [Mobile 3](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658676/Spaceport/Mobile/3.1_3_pzynzb.jpg) [Mobile 4](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658676/Spaceport/Mobile/3.1_4_xo2gzk.jpg) [Mobile 5](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658677/Spaceport/Mobile/3.1_5_vawynl.jpg) [Mobile 6](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643658678/Spaceport/Mobile/3.1_6_kfnzyb.jpg)|Pass|
|3.2|The information immediately visible is the pipeline's identifying information (name, description, status, date created, num images)|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660488/Spaceport/Desktop/3.2_qapebn.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659504/Spaceport/Tablet/3.2_xnm3ck.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660424/Spaceport/Mobile/3.2_my5qck.jpg)||
|3.3|For 'pending' and 'active' pipelines, the update button is at the top of the page to refresh the pipeline.  The 'complete' pipelines the button is disabled.|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659504/Spaceport/Tablet/3.3_d0fumr.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659504/Spaceport/Tablet/3.3_d0fumr.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660424/Spaceport/Mobile/3.3_ldtqoy.jpg)|Pass|
|3.4|The AOI chosen by the user is rendered on a zoomable map at the top of the page.  The user can zoom out for better placement of the AOI|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659503/Spaceport/Tablet/3.4_ppkv8g.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659503/Spaceport/Tablet/3.4_2_ieo1oh.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659503/Spaceport/Tablet/3.4_ppkv8g.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659503/Spaceport/Tablet/3.4_2_ieo1oh.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660424/Spaceport/Mobile/3.4_sml4ix.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660424/Spaceport/Mobile/3.4_2_nnpl1j.jpg)|Pass|
|3.5|For active pipelines, a timeline chart displays all intervals, current interval, today represented by a satellite icon, and dates images were taken with a picture icon|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660724/Spaceport/Desktop/3.5_u3tckj.jpg)|N/A for tablet|N/A for mobile|Pass|
|3.6|The interval table displays the number of intervals, current/complete/future intervals|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703225/Spaceport/Desktop/3.6_tn9oyo.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703224/Spaceport/Desktop/3.6_2_u8p8qz.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703271/Spaceport/Tablet/3.6_qn5afy.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703270/Spaceport/Tablet/3.6_2_xa06qj.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703309/Spaceport/Mobile/3.6_uj3ok0.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703309/Spaceport/Mobile/3.6_2_bnnmml.jpg)|Pass|
|3.7|The Results table displays information about any results collected, if there are any.  The table can be expanded to display further technical information about the images.|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643704022/Spaceport/Desktop/3.7_i16xro.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643704022/Spaceport/Desktop/3.7_2_fpscni.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703997/Spaceport/Tablet/3.7_iejwq2.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703997/Spaceport/Tablet/3.7_2_oydjni.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703971/Spaceport/Mobile/3.7_ixl3ej.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703971/Spaceport/Mobile/3.7_2_z7pc92.jpg)|Pass|
|3.8|In the Results table, when the image preview is clicked, the image opens in a new tab|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705666/Spaceport/Desktop/3.8_ojepyv.jpg)|""|""|Pass|
|3.9|In the Results table, when the image metadata link is clicked, the data file opens in a new tab|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705677/Spaceport/Desktop/3.9_xyavzs.jpg)|""|""||
|3.10|The user can see the AOI data, coverge, cloud coverage and output image which relates to this pipeline|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705918/Spaceport/Desktop/3.10_qa5hyg.jpg)|[Tablet]()|[Mobile]()|Pass|
|3.11|The user can see if/when the pipeline was last edited|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705920/Spaceport/Desktop/3.12_jikxfm.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718161/Spaceport/Tablet/3.10_w5nqtp.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718336/Spaceport/Mobile/3.11_nyht92.jpg)|Pass|
|3.12|The Edit Pipeline & Delete Pipeline buttons are available to see at the bottom of the detail view of the pipeline|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705920/Spaceport/Desktop/3.12_jikxfm.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718161/Spaceport/Tablet/3.11_jftfk3.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718336/Spaceport/Mobile/3.11_nyht92.jpg)|Pass|
|3.13|The user cannot edit the pipeline if the status is complete.  The user cannot edit or delete the pipeline if it is pending.|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705920/Spaceport/Desktop/3.11_jllchn.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643706124/Spaceport/Desktop/3.13_toljjs.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718161/Spaceport/Tablet/3.13_b0boiw.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718236/Spaceport/Tablet/3.13_2_qv4luz.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718335/Spaceport/Mobile/3.13_o46sy6.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718335/Spaceport/Mobile/3.13_2_sdxljs.jpg)|Pass|

## Acceptance Criteria Status
- [x] User is clearly aware which pipeline details they are looking at
- [x] User is aware of the status and progress so far of the pipeline
- [x] User can access how to update, edit or delete this pipeline
- [x] User can see all relating results/images gathered by pipeline

# User Story 5
As a **Site User** I can **access information on satellite imagery**

- 5.1: As a **New/returning Site User** I can **see at all times the Discover page link** so that **I can always refer to this page for more information**
- 5.2: As a **New Site User** I am **firstly directed to the homepage** so that **the purpose of the site is immediately clear to me**
- 5.3: As a **New/returning Site User** I can **explore technical terms associated with satellite imagery and pipelines** so that **I can check any definitions I am unsure of**
- 5.4: As a **New/returning Site User** I am **given explanations of technical terms in the form** so that **I understand what the parameters I am setting means**
- 5.5: As a **Site User** I am **provided with links to all image metadata** so that **I can use the images in post production**
- 5.6: As a **New/returning Site User** I can **read examples of pipelines created by current/previous clients** so that **I have a context as to what I can use satellite imagery for**
- 5.7: As a **New/returning Site User** I can **read topical events involving satellite imagery** so that **I am aware of the importance of being able to access satellite imagery**
- 5.8: As a **New/returning Site User** I can **click on links for futher information on how satellite imagery works** so that **I can further my understanding**

## Acceptance Criteria
- Users are clearly and immediately aware of the purpose of the site
- Users can explore further on 'discover' page to see applications of satellite imagery
- Users can explore testimonials/examples to aid with their own pipeline creation

## Testing

|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|5.1||[Desktop]|[Tablet]|[Mobile]||
|5.2||[Desktop]|[Tablet]|[Mobile]||
|5.3||[Desktop]|[Tablet]|[Mobile]||
|5.4||[Desktop]|[Tablet]|[Mobile]||
|5.5||[Desktop]|[Tablet]|[Mobile]||
|5.6||[Desktop]|[Tablet]|[Mobile]||
|5.7||[Desktop]|[Tablet]|[Mobile]||
|5.8||[Desktop]|[Tablet]|[Mobile]||