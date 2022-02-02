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
|3.2|The information immediately visible is the pipeline's identifying information (name, description, status, date created, num images)|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660488/Spaceport/Desktop/3.2_qapebn.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659504/Spaceport/Tablet/3.2_xnm3ck.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660424/Spaceport/Mobile/3.2_my5qck.jpg)|Pass|
|3.3|For 'pending' and 'active' pipelines, the update button is at the top of the page to refresh the pipeline.  The 'complete' pipelines the button is disabled.|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659504/Spaceport/Tablet/3.3_d0fumr.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659504/Spaceport/Tablet/3.3_d0fumr.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660424/Spaceport/Mobile/3.3_ldtqoy.jpg)|Pass|
|3.4|The AOI chosen by the user is rendered on a zoomable map at the top of the page.  The user can zoom out for better placement of the AOI|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659503/Spaceport/Tablet/3.4_ppkv8g.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659503/Spaceport/Tablet/3.4_2_ieo1oh.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659503/Spaceport/Tablet/3.4_ppkv8g.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643659503/Spaceport/Tablet/3.4_2_ieo1oh.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660424/Spaceport/Mobile/3.4_sml4ix.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660424/Spaceport/Mobile/3.4_2_nnpl1j.jpg)|Pass|
|3.5|For active pipelines, a timeline chart displays all intervals, current interval, today represented by a satellite icon, and dates images were taken with a picture icon|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643660724/Spaceport/Desktop/3.5_u3tckj.jpg)|N/A for tablet|N/A for mobile|Pass|
|3.6|The interval table displays the number of intervals, current/complete/future intervals|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703225/Spaceport/Desktop/3.6_tn9oyo.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703224/Spaceport/Desktop/3.6_2_u8p8qz.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703271/Spaceport/Tablet/3.6_qn5afy.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703270/Spaceport/Tablet/3.6_2_xa06qj.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703309/Spaceport/Mobile/3.6_uj3ok0.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703309/Spaceport/Mobile/3.6_2_bnnmml.jpg)|Pass|
|3.7|The Results table displays information about any results collected, if there are any.  The table can be expanded to display further technical information about the images.|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643704022/Spaceport/Desktop/3.7_i16xro.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643704022/Spaceport/Desktop/3.7_2_fpscni.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703997/Spaceport/Tablet/3.7_iejwq2.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703997/Spaceport/Tablet/3.7_2_oydjni.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703971/Spaceport/Mobile/3.7_ixl3ej.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643703971/Spaceport/Mobile/3.7_2_z7pc92.jpg)|Pass|
|3.8|In the Results table, when the image preview is clicked, the image opens in a new tab|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705666/Spaceport/Desktop/3.8_ojepyv.jpg)|""|""|Pass|
|3.9|In the Results table, when the image metadata link is clicked, the data file opens in a new tab|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705677/Spaceport/Desktop/3.9_xyavzs.jpg)|""|""|Pass|
|3.10|The user can see the AOI data, coverge, cloud coverage and output image which relates to this pipeline|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705918/Spaceport/Desktop/3.10_qa5hyg.jpg)|[Tablet]()|[Mobile]()|Pass|
|3.11|The user can see if/when the pipeline was last edited|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705920/Spaceport/Desktop/3.12_jikxfm.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718161/Spaceport/Tablet/3.10_w5nqtp.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718336/Spaceport/Mobile/3.11_nyht92.jpg)|Pass|
|3.12|The Edit Pipeline & Delete Pipeline buttons are available to see at the bottom of the detail view of the pipeline|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705920/Spaceport/Desktop/3.12_jikxfm.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718161/Spaceport/Tablet/3.11_jftfk3.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718336/Spaceport/Mobile/3.11_nyht92.jpg)|Pass|
|3.13|The user cannot edit the pipeline if the status is complete.  The user cannot edit or delete the pipeline if it is pending.|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643705920/Spaceport/Desktop/3.11_jllchn.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643706124/Spaceport/Desktop/3.13_toljjs.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718161/Spaceport/Tablet/3.13_b0boiw.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718236/Spaceport/Tablet/3.13_2_qv4luz.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718335/Spaceport/Mobile/3.13_o46sy6.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643718335/Spaceport/Mobile/3.13_2_sdxljs.jpg)|Pass|

## Acceptance Criteria Status
- [x] User is clearly aware which pipeline details they are looking at
- [x] User is aware of the status and progress so far of the pipeline
- [x] User can access how to update, edit or delete this pipeline
- [x] User can see all relating results/images gathered by pipeline

# User Story 4
As a **Site User** I can **create an account** so that **I can log in to create pipelines, and view my pipelines**

- 4.1: As a **New Site User** I can **sign up to Spaceport** so that **I can create pipelines**
- 4.2: As a **Returning Site User** I can **log in to my account when revisiting the page** so that **I view details of my pipelines**
- 4.3: As a **Site User** I can **see the login/signup/logout link in the nav bar** so that **I am always aware of my log in state**
- 4.4: As a **Site User** I am **redirected to my pipelines when I log in** so that **my account information is immediately visible to me**
- 4.5: As a **Site User** I can **logout from my account on Spaceport** so that **my account information is kept safe and private**

## Acceptance Criteria
- User can Sign Up to the website from the homepage
- Users are aware of their current login/logout status
- Users are redirected to the relevant page when signing up, logged in etc

|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|4.1|The user can click on the navigation bar to see the login page, and create an account with a username and password|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643814151/Spaceport/Desktop/4.1_yfgqm7.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817438/Spaceport/Tablet/4.1_omdbgm.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817245/Spaceport/Mobile/4.1_owben4.jpg)||
|4.2|If the user clicks Login/Signup, they are directed to the login page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643814151/Spaceport/Desktop/4.2_qlzy3g.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817439/Spaceport/Tablet/4.2_fkptee.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817244/Spaceport/Mobile/4.2_srsunr.jpg)||
|4.3|If logged in, the user can see their username in the navigation bar so they are aware of their log in status|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643814151/Spaceport/Desktop/4.3_hsidlg.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817440/Spaceport/Tablet/4.3_c1m4op.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817244/Spaceport/Mobile/4.3_j4palf.jpg)||
|4.4|When the user has logged in, their My Pipelines page is visible|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643814151/Spaceport/Desktop/4.3_hsidlg.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817440/Spaceport/Tablet/4.3_c1m4op.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817349/Spaceport/Mobile/4.4_cezgzh.jpg)||
|4.5|The user can confirm they want to log out|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643814152/Spaceport/Desktop/4.5_gwzjdv.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817439/Spaceport/Tablet/4.5_ldybbf.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643817349/Spaceport/Mobile/4.5_jzgdk0.jpg)||

## Acceptance Criteria Status
- [x] User can Sign Up to the website from the homepage
- [x] Users are aware of their current login/logout status
- [x] Users are redirected to the relevant page when signing up, logged in etc

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
- 5.9 As a **New/returning Site User** I can **read about common applications of satellite imagery** so that **I have more understanding of the real life applications of the website**

## Acceptance Criteria
- Users are clearly and immediately aware of the purpose of the site
- Users can explore further on 'discover' page to see applications of satellite imagery
- Users can explore testimonials/examples to aid with their own pipeline creation

## Testing

|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|5.1|The Discover page is always visible for the user to refer back to for technical information about satellite imagery|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722246/Spaceport/Desktop/5.1_lkdugj.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723668/Spaceport/Tablet/5.1_kug8gj.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723195/Spaceport/Mobile/5.1_zvnj07.jpg)|Pass|
|5.2||[Desktop]|[Tablet]|[Mobile]|Pass|
|5.3|The Glossary section on the Discover page provides definitions of any technical terms the user may encounter while using the site|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722247/Spaceport/Desktop/5.3_yhrr7b.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723637/Spaceport/Tablet/5.3_memzjp.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723196/Spaceport/Mobile/5.3_c7spi4.jpg)|Pass|
|5.4|Definitions of parameters are also explained while the user is creating a pipeline (unless the parameter meaning is obvious, such as 'Name')|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722765/Spaceport/Desktop/5.4_k0fubf.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722766/Spaceport/Desktop/5.4_2_megqg6.jpg) [Desktop 3](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722766/Spaceport/Desktop/5.4_3_ews80t.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723636/Spaceport/Tablet/5.4_wj8lfb.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723636/Spaceport/Tablet/5.4_2_olnctq.jpg) [Tablet 3](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723636/Spaceport/Tablet/5.4_3_bhyfwa.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723196/Spaceport/Mobile/5.4_hm2yz8.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723197/Spaceport/Mobile/5.4_2_ldskdy.jpg) [Mobile 3](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723197/Spaceport/Mobile/5.4_3_mkucyv.jpg)|Pass|
|5.5|For any delivered images, users are provided with a link to the technical data associated with the image|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722630/Spaceport/Desktop/5.5_eh4hvy.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723637/Spaceport/Tablet/5.5_vlil28.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723198/Spaceport/Mobile/5.5_pshowm.jpg)|Pass|
|5.6|Users can read two examples of how the website could be used|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722248/Spaceport/Desktop/5.6_nqkucm.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723639/Spaceport/Tablet/5.6_qtmrej.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723199/Spaceport/Mobile/5.6_gcdjzr.jpg)|Pass|
|5.7|The In the News section on the Discover page describes topical events relating the satellite imagery|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722426/Spaceport/Desktop/5.7_f7ypqt.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723639/Spaceport/Tablet/5.7_qrzicf.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723197/Spaceport/Mobile/5.7_z2abv3.jpg)|Pass|
|5.8|The glossary provides several additional links for the user to explore more|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722427/Spaceport/Desktop/5.8_sdu3iv.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723639/Spaceport/Tablet/5.8_fly6mw.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723198/Spaceport/Mobile/5.8_c4krit.jpg)|Pass|
|5.9|The Discover page outlines several industries which rely on satellite imagery, and explains how|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643722531/Spaceport/Desktop/5.9_y4fach.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723640/Spaceport/Tablet/5.9_qijcdx.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643723198/Spaceport/Mobile/5.9_e0miv5.jpg)|Pass|

## Acceptance Criteria Status
- [x] Users are clearly and immediately aware of the purpose of the site
- [x] Users can explore further on 'discover' page to see applications of satellite imagery
- [x] Users can explore testimonials/examples to aid with their own pipeline creation

# User Story 9
As a **Site User** I can **see a visual graph of the progress of the pipeline** so that **I have a more visually pleasing understanding of the pipeline progress** (active pipelines only)

- 9.1: As a **Site User** I can **see a timeline spanning the full duration of my pipeline** so that **I can see when the pipeline starts and ends**
- 9.2: As a **Site User** I can **see a legend on the timeline** so that **I know what all icons and colours represent**
- 9.3: As a **Site User** I can **see all intervals in my pipeline** so that **I know when the intervals start, end, and the duration**
- 9.4: As a **Site User** I can **see the status of all pipelines colour-coded** so that **I can see which intervals have been completed, and which are still to be completed**
- 9.5: As a **Site User** I can **see today represented on the timeline** so that **I can gauge an understanding of how much of the pipeline has been completed, and how much is left**
- 9.6: As a **Site User** I can **see when images were delivered** so that **I know which intervals were successful**

## Acceptance Criteria
- Users can see a timeline graph of the entire pipeline, displaying start, end dates and all intervals
- Users can see where the pipeline is in the timeline
- Users can see which intervals are complete, incomplete, current
- Users can see which intervals have been successful

## Testing
|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|9|For active pipelines, the user can see interval detail, status, dates, image dates and a respresentation of today on the timeline|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643809183/Spaceport/Desktop/9_ekbquo.jpg)|N/A for tablet|N/A for mobile||

## Acceptance Criteria Status
- [x] Users can see a timeline graph of the entire pipeline, displaying start, end dates and all intervals
- [x] Users can see where the pipeline is in the timeline
- [x] Users can see which intervals are complete, incomplete, current
- [x] Users can see which intervals have been successful

# User Story 10
As a **Site User** I can **select the AOI for my pipeline on a map feature** so that **there is a more accessible way of selection/viewing my chosen AOI**

- 10.1: As a **Site User** I am **instructed to select an area of an interactive map** so that **my pipeline will retrieve satellite images of that area**
- 10.2: As a **Site User** I am **made aware of the restrictions of the map selection** so that **I can draw an area which will meet those restrictions**
- 10.3: As a **Site User** I am **given inline feedback of my map selection size** so that **I can adjust the area I drew if it does not meet the requirements**
- 10.4: As a **Site User** I am **given instructions on how to use the map features** so that **understand how to draw, select, edit and delete the area I drew**
- 10.5: As a **Site User** I can **zoom in and out on the map** so that **I can more easily find the area on Earth I am looking for**
- 10.6: As a **Site User** I am **given a review of the AOI I selected in the form review and my pipeline detail view** so that **I am reminded of the location of the AOI I selected**
- 10.7: As a **Site User** I can **see the geoJSON data/coordinates of the area I selected** so that **I can use this information in post production**

## Acceptance Criteria
- Users can select the Area of Interest (AOI) on a map feature, which inputs the selection into the form
- Users can delete/edit a selection if they change their mind
- Users can see what the area of their selection is, and if it is within an acceptable range

## Testing
|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|10.1|The user can see a definition of what the AOI, and is instructed to select the map|[Desktop]|[Tablet]|[Mobile]||
|10.2|The restriction on the size of AOI is displayed at all times|[Desktop]|[Tablet]|[Mobile]||
|10.3|If the AOI selected falls outwith the restriction, the user is notified and cannot progress the form|[Desktop]|[Tablet]|[Mobile]||
|10.4|At the start of the form, there are 6 steps to teach the user how to use the form|[Desktop]|[Tablet]|[Mobile]||
|10.5|The user can use their mouse scroll to zoom in and out to view the AOI from different zooms|[Desktop]|[Tablet]|[Mobile]||
|10.6|The AOI is rendered |[Desktop]|[Tablet]|[Mobile]||
|10.7||[Desktop]|[Tablet]|[Mobile]||

# User Story 11
As a **Site User** I can **view/download images and metadata of retrieved API results** so that **I can use this information in post production**

- 11.1: As a **Site User** I can **view a preview of a delivered image** so that **I can determine if the image is of good quality**
- 11.2: As a **Site User** I can **download the full-size image** so that **I can use the image for the purpose I need it/view it in higher resolution**
- 11.3: As a **Site User** I can **see the size of the full-size image** so that **I am aware how large in computer memory the image is**
- 11.4: As a **Site User** I can **see technical data associated with any delivered images** so that **I can determine if the image is of use to me/meets the parameters I set**
- 11.5: As a **Site User** I can **open a file containing the metadata associated with delivered images** so that **I can view further technical information about the image/satellite which took the image**

## Acceptance Criteria
- Users can click on resulting images and view/download them
- Users can click on a link to the image metadata and copy it

## Testing
|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|11.1|The user can click on the Image Preview in the Results table, which will open a separate tab with a smaller resolution image preview|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643739946/Spaceport/Desktop/11.1_quhbnl.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643739951/Spaceport/Desktop/11.1_2_hzkcpq.jpg)|""|""||
|11.2|The user can click Download Image in the Results table, which will download the full size image to their computer|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643739946/Spaceport/Desktop/11.2_zyew4j.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643739946/Spaceport/Desktop/11.2_2_n0cty4.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643740552/Spaceport/Tablet/11.2_boivk7.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643740311/Spaceport/Mobile/11.2_d0exg4.jpg)||
|11.3|The user can see the size in megabytes of the full-size image|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643739946/Spaceport/Desktop/11.3_grhxhj.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643740551/Spaceport/Tablet/11.3_yhrcds.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643740310/Spaceport/Mobile/11.3_xzwdhv.jpg)||
|11.4|The user can expand the Results table to review additional information about the image|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643739950/Spaceport/Desktop/11.4_wkuqjd.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643740552/Spaceport/Tablet/11.4_xcxtrt.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643740311/Spaceport/Mobile/11.4_hcgspb.jpg)||
|11.5|The user can click on the Metadata tab in the Results table to open a seperate tab including further technical information about the image|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643739952/Spaceport/Desktop/11.5_ewxawt.jpg)|""|""||

# User Story 12
As a **Site User** I can **edit details of my pipelines**

- 12.1: As a **New/returning Site User** I can **access the edit form on the pipeline detail page** so that **I can edit the pipeline**
- 12.2: As a **New/returning Site User** I can **see which parameters I can change for my pipeline** so that **I am aware of the limitations once my pipeline has been submitted**
- 12.3: As a **New/returning Site User** I can **change the name and description of my pipeline** so that **I can correct if needed, or add details about results in the description**
- 12.4: As a **New/returning Site User** I can **see if my pipeline is able to be edited** so that **I am aware if I can edit the pipeline and, if not, the reason why**
- 12.5: As a **New/returning Site User** I am **redirected back to the detail view of the pipeline** so that **I can see the changes I made reflected**
- 12.6: As a **New/returning Site User** I am **shown a timestamp of when the pipeline was last edited** so that **I am aware if and when I last edited my pipeline**

## Acceptance Criteria
- User can edit specific parameters of their pipeline
- User is aware by feedback that their pipeline has been edited
- User is aware which features they can edit
- User is aware when pipeline was last edited

## Testing
|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|12.1|The Edit Pipeline button sits at the bottom of the pipeline instance page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728203/Spaceport/Desktop/12.1_a9ejp2.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643738531/Spaceport/Tablet/12.1_d7arfk.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728882/Spaceport/Mobile/12.1_ketqxn.jpg)||
|12.2|Parameters available to be edited are displayed in the review tab of the create pipeline form.  They are also the only options present on the edit form|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643625902/Spaceport/Desktop/1.10_wbjaas.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728203/Spaceport/Desktop/12.3_x1eh6u.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643643401/Spaceport/Tablet/1.11_g6pbh5.jpg)|[Mobile]()||
|12.3|Users can input different values for the name and description of the pipeline, and save|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728203/Spaceport/Desktop/12.3_x1eh6u.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728203/Spaceport/Desktop/12.3_2_j7avva.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643729211/Spaceport/Tablet/12.3_z9gla5.jpg)[Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643729213/Spaceport/Tablet/12.392_byr3tr.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728882/Spaceport/Mobile/12.3_2_bhwmpl.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728882/Spaceport/Mobile/12.3_dp2vuo.jpg)||
|12.4|Users can access the Edit Pipeline button if the pipeline can be edited.  If not, the reason is displayed why|[Desktop 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728203/Spaceport/Desktop/12.4_wukt8g.jpg) [Desktop 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728204/Spaceport/Desktop/12.4_2_kng5bg.jpg)|[Tablet 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643729212/Spaceport/Tablet/12.4_2_ieseuo.jpg) [Tablet 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643729212/Spaceport/Tablet/12.4_rpasm7.jpg)|[Mobile 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728883/Spaceport/Mobile/12.4_qvfcpr.jpg) [Mobile 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728883/Spaceport/Mobile/12.4_2_ldyhul.jpg)||
|12.5|The changes the user made in the Edit Pipeline form are reflected when the user is redirected back to the pipeline instance|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728204/Spaceport/Desktop/12.5_lv7par.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643729213/Spaceport/Tablet/12.5_rkpxle.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728883/Spaceport/Mobile/12.5_w3lsew.jpg)||
|12.6|If the pipeline was edited, a timestamp of when is displayed|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728203/Spaceport/Desktop/12.6_cbki2o.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643729213/Spaceport/Tablet/12.6_dyhqfc.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643728883/Spaceport/Mobile/12.6_kr9x7q.jpg)||

## Acceptance Criteria
- [x] User can edit specific parameters of their pipeline
- [x] User is aware by feedback that their pipeline has been edited
- [x] User is aware which features they can edit
- [x] User is aware when pipeline was last edited

# User Story 13
As a **Site User** I can **delete my pipeline** so that **I can remove pipelines I no longer need, or were incorrect**

- 13.1: As a **Site User** I can **see the Delete Pipeline button on my pipeline view** so that **I can access the delete form**
- 13.2: As a **Site User** I am **provided with an intermediate view of deleting the pipeline** so that **I do not delete my pipeline immediately by pressing the Delete Pipeline button**
- 13.3: As a **Site User** I am **aware which pipeline I am about to delete** so that **I am certain which pipeline I am about to delete**
- 13.4: As a **Site User** I can **see a list of results of deleting the pipeline** so that **I am aware of the consequences of deleting a pipeline**
- 13.5: As a **Site User** I can **see an exit button when deleting my pipeline** so that **I can change my mind if I no longer want to delete this pipeline**
- 13.6: As a **Site User** I am **given feedback that the pipeline was deleted** so that **I have confirmation that the pipeline was deleted**

## Acceptance Critera
- User knows how to delete their pipeline
- User is aware of the consequences of deleting their pipeline
- User is clear which pipeline they are deleting
- User is given an opportunity to change their mind about deleting
- User is aware that pipeline has been deleted

## Testing
|User story|Result|Desktop|Tablet|Mobile|Status|
|----|------|-------|------|------|------|
|13.1|The Delete Pipeline button is displayed at the bottom of the pipeline instance detail page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806374/Spaceport/Desktop/13.1_rpvbma.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806445/Spaceport/Tablet/13.1_rlpdik.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806522/Spaceport/Mobile/13.1_wqiw79.jpg)|Pass|
|13.2|Users are given an opportunity to review the details of deleting the pipeline, before officially deleting the pipeline|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806375/Spaceport/Desktop/13.2_x6ezme.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806445/Spaceport/Tablet/13.2_dyvx0q.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806522/Spaceport/Mobile/13.2_nxkmx3.jpg)|Pass|
|13.3|The pipeline name is displayed on the delete form so the user knows for certain which pipeline they are deleting|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806374/Spaceport/Desktop/13.3_xq6u22.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806444/Spaceport/Tablet/13.3_oiquny.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806522/Spaceport/Mobile/13.3_nbydnv.jpg)|Pass|
|13.4|The consequences of deleting the pipeline are displayed in list format|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806375/Spaceport/Desktop/13.4_i09m9u.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806444/Spaceport/Tablet/13.4_wgr4bz.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806523/Spaceport/Mobile/13.4_r5arnf.jpg)|Pass|
|13.5|Users have an opportunity to back out from deleting the pipeline by returning back to the pipeline detail view|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806375/Spaceport/Desktop/13.5_pnz24h.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806445/Spaceport/Tablet/13.5_ozjygo.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806523/Spaceport/Mobile/13.5_c8d5x2.jpg)|Pass|
|13.6|The user can see confirmation that the pipeline was deleted|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806375/Spaceport/Desktop/13.6_fjr0id.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806445/Spaceport/Tablet/13.6_hyo5sz.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643806523/Spaceport/Mobile/13.6_xlkl7l.jpg)|Pass|

## Acceptance Critera Status
- [x] User knows how to delete their pipeline
- [x] User is aware of the consequences of deleting their pipeline
- [x] User is clear which pipeline they are deleting
- [x] User is given an opportunity to change their mind about deleting
- [x] User is aware that pipeline has been deleted