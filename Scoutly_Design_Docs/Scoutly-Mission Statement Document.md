## Why am I building Scoutly?
    To improve a business function in need of efficiency gains. Also to learn about basic web development. 

## Who is the Project for?
    Sales teams and their potential clients.

## What is gonna make it valuable?
    To help sales teams find higher quality leads by matching individuals with prospects based off business, local, and personal commonalities. The same can be said for potential clients on the platform who need specific services with specific personailties involved. The overall time, effort, and effectiveness of matching services with clients will be improved. Increase the ease leaning on KLT (Know, Like, and Trust) factor. 


## Functional and Non-Functional Sales user Needs
    - Input lead files and return a snapshot of best matches on a dashboard
        - Should be able to filter best matches based on personal, business, and/or local needs
        - Should be able to adjust display of matches as list ranking
        - Dashboard should display most common traits between leads and Sales user
            - Should also display most common traits of leads not found with Sales user
    - When lead files are input from another Sales user
        - If commonalities metric is over a certain threshold, all resepctive Sales users shall be notified via email or text.
            - This can be adjusted to only the best fit( orrange of Sales users) Sales user is notified
        - 
    - Sales user should be able to access a newly created lead profile and identify best matched traits
        - Should also be given a rating for liklehood a Sales user's services are needed
    - Leads given from an enterprise should be able stored along with their embeddings as well as updated if they're are requested so again.
    - The data of leads should be updated in a specified time range.
    - Secure Login and Logout functionality


## Data 
    - Sales
        - Name
        - Picture
        - Age
        - Work Location
        - Business
        - Role
        - Industry
        - Product
        - Years Experience
        - Hobbies
        - Teams
        - Other Facts

    - Client Rep
        - Name
        - Picture(s)
        - Age
        - Work Location
        - Business
        - Role
        - Industry
        - Product
        - Years Experience
        - Hobbies
        - Teams
        - Other Facts
        - Last_Update_Info
        - Lead_Status
        - Last_Reach_Out
        - Likelyhood_for_business_rating (High Level TBD)
            - 1 to 5 rating that rep who last contacted lead gives
            - may also account for any information posted/related to the lead online regarding need for business
        - Similarity_Score (High Level TBD)
        - Key_Similarities_List (High Level TBD)
            - Similarities need to be ranked based off how important they are to lead
        - Profile_Update_Interval
## Data Relation Ship Map 
    - TBD
## MVP
    - Input lead files and return a snapshot of best matches on a dashboard
        - Should be able to filter best matches based on personal, business, and/or local needs
        - Should be able to adjust display of matches as list ranking
    - Sales user should be able to access a newly created lead profile and identify best matched traits
        - Should also be given a rating for liklehood a Sales user's services are needed
    - Leads given from an enterprise should be able stored along with their embeddings
## The Future of the Project
    - I plan to add more sales features for the project
        - Notifications of lead matches and/or likelness for business scores
        - Statistics based data presentation 
        - Lead Map
        - Settings for Scoutly User profiles
        - More Roboust UI to allow for widgets and customization of Overview Screen
    - Scoutly will take months to complete an MVP 1
## Project Presentation
    - WebApp
    - User will simply utilize the application through the web
        - A desktop app maybe provided sometime in the future
## 8 Tech Stack
    -- Storing Data - TBD
    -- Backend - Python Flask
    -- Front-End - React.js  (need to look into dashboard and charts library)



1) start form your goal:
	1) Why am i making this project ?
	2) Who this project is for ?
	3) What is going to make it valuable ?
	- Write them down and think on them not just surface level problems
2) Write down what the users must be able to do with the  project 
	1) features
	2) guardrails
	3) don't overthink with tech stack etc only what features that is needed 
	4) user centric approach
3) Define the data models
	1) don't think about the databases
	2) think about the data what you need and how you want to handle it
	3) draw the relationships
4) Nail an MVP
	1) Look back on all the features above and strip it to the barebones and what is needed to make it function : absolute minimum version
5) Wireframe the project for the most basic user 
	1) think more about UX than UI
	2) paper is cheap but code is expensive
6) Understand the future of the project:
	1) Do you plan to add more features in the future
	2) Do you plan to work on this for months or just a few days ?
		1) don't over or under engineer
7) How is you project going to be presented 
	1) is it a script or a mobile app or a website or a extension
	2) understand how the users will be interacting and base your architecture on that
8) Tech Stack :
	1) Use the points above to choose the tech stack
	2) don't let the tech stack define the project 
	3) best tool for the project not the other way round
	4) Can you deploy this ?
		1) is the tech stack you are choosing viable for deployment and easy to do so so that you don't spend your time more deploying that building
9) The development process
	1) Bare bones
		1) Folder structure
		2) naming conventions
		3) dev environments
		4) version control
	2) setting up the database and creating the data models
	3) backend routes :
		1) API endpoints
		2) test them
	4) Frontend
	5) Project integration and version
	6) CI/CD
	7) test at all steps










