
# **PODDLY**
## The Community Podcast Directory

![alt text](/readme_assets/responsive_mockup.png "Responsive Mockup")

**[Live Site](https://poddly.onrender.com)**

This website is designed and created for the Data Centric Development Milestone Project, for Code Institute's Diploma in Web Application Development.

Poddly - The Community Podcast Directory is a free to use online podcast sharing platform, where podcast lovers from around the world can share their favourites, and expand their own library of podcasts with new discoveries shared by the Poddly Community Directory.

The platform will allow users to browse a complete directory of shared podcasts, search, leave comments, and even recommend their own favorite podcasts.

## **Table of Contents**

* [UX](#UX)
    * [Strategy](#strategy)
        * [Site Owner Goals](#site-owner-goals)
        * [External User Goals](#external-user-goals)
        * [Returning User Goals](#returning-user-goals)
    * [Scope](#scope)
    * [Structure](#structure)
        * [Database](#database)
    * [Skeleton](#skeleton)
        * [Wireframes](#wireframes)
    * [Surface](#surface)
        * [Colour Palette](#colour-palette)
        * [Typography](#typography)
        * [Icons](#icons)
        * [Images](#images)
* [Technologies Used](#technologies-used)
* [Bugs & Testing](#bugs-&-testing)



## **UX** 
## **Strategy**
--- 
The main aim of the website is to provide a free-to-use podcast resource, which allows the **user** to add podcast suggestions to the site so it can be viewed by other **users**, browse and search for new podcasts, amend and delete their own suggestions. Information presented is clear, intuitive, easy to use.

- To allow the growth of a podcast database for the **user** and by the **user**.
- To allow the **site owner** to encourage the **user** to engage in recomemnding podcasts and leaving comments and feedback on other users recommended podcasts.
#### **Site Owner Goals**
- To create an easy to use platform that is intuitive in design, responsive and easy to navigate.
- Implement CRUD (Create, Read, Update, Delete) functionality, allowing users to add, edit and delete their podcast recommendations.
- Implement defensive programming using data validation and authentication
- Create a mobile-first design, while ensuring the website is responsive across all device sizes.

#### **External User Goals**
First Time User - As a casual/first time user who has not created an account, I want to be able to:
- Search for specific podcasts or keyword
- View podacast descriptions including other users comments
- Register and create an account

#### **Returning User Goals**
Registered User - As a user who has registered and signed in, I want to be able to:
- Do everything a Causal User can
- Add, edit and delete my own podcast suggestions
- Comment on other users suggestions
- Edit my podcast information
- Delete my podcasts

Admin - As an administrator, I want to be able to:
- Have the ability to maintain the website and the content on it
- Edit and Delete any podcast suggestion
- Edit and Delete any comment and/or rating
- Add, Modify and Delete any catagory and/or channel

## **Scope**
---
### **Feature Ideas Table**
Below is a table to highlight the importance of potential features in the first release, versus the feasibility of implementation.

| Feature/Opportunity | Importance (out of 5) | Feasibility/Viability (out of 5) | In or Out? |
| --- | --- | --- | --- |
| Home Page, displaying all Podcasts | 5 | 5 | In | 
| Register/Login/Logout | 5 | 5 | In |
| Send Messages to Admin | 3 | 5 | Out |
| Full CRUD Functionality | 5 | 5 | In |
| Page for users to Create, Read, Update, Delete Podcasts | 5 | 5 | In |
| Search by keyword | 5 | 4 | In |
| Podcast Recommendations based on the "liked" podcasts | 4 | 3 | Out |
| Save Podcasts onto a personal listened to/want to listen list | 4 | 4 | Out |
| Add Comments | 5 | 4 | In |
| Links to Socials | 3 | 5 | In |
| 'Like' Button for Podcasts | 4 | 3 | Out |
| Upload and display user profile picture | 3 | 3 | Out |
| Edit Profile Page | 4 | 3 | Out |
| Play selected podcast directly from website | 4 | 1 | Out |
| Display users Apple Podcasts/Spotify playlist | 3 | 1 | Out |
| Manage Podcast categories/channels (as Admin) | 5 | 5 | In |
| Contact Page | 4 | 4 | Out |
| 404 Page | 4 | 3 | Out |
| Fully Responsive Website | 5 | 5 | In |

In order to complete the project in time for the deployment and submission deadline, functions of less importance will not be implemented in the first release of project, below are the main features to be impletmented for the project:

- Home Page displaying all podcasts
- Ability to Register, Login and Logout
- Full CRUD Functionality to Add, Read, Edit and Delete Tracks
- A page for users to add podcasts to the platform
- Display more information and comments about relative podcast
- Functionality for users to leave comments on podcast cards
- Search functionality
- Admin Priveleges (to manage Categories and Channels)

Features for future releases:

- Like counter for simple user rating
- Podcast Recommendations based on the "liked" podcasts
- Categorise podcasts further to include most popular, best of the year, most listened to.
- Save Podcasts onto a personal listened to/want to listen list
- Upload and display user profile picture
- Play selected podcast directly from website


[Click here](/readme_assets/flow_%20chart.png) to view the Flow Chart

## **Structure**
---

The structure of each page to be used on the website is listed below.

1. Home Page
    - Navigation Bar/Brand Logo - A navigation bar will be displayed at the top level of the home page and all subsequent pages.
    - Search Form - Searching by name or browse by category or channel dropdown.
    - Cards displaying podcasts - All podcasts added by users will be shown on the page.
    - Modal window - Users can find out more about individual podcasts by clicking on the cards, which will trigger a modal window showing more information about the selected podcast. Users will be able to 'like' and comment on the podcast.
    - Footer - Social Media Links will be displayed at the bottom of the Home Page.

2. Login Page - As well as being able to login directly from the home page, users will also be able to visit a dedicated Login Page.
    - Navigation Bar
    - Login Form
    - Footer

3. Registration Page
    - Navigation Bar
    - Registration Form
    - Footer

4. 'Recommend a Podcast' Page
    - Navigation Bar
    - Form to add details of a Podcast
    - Footer

6. Admin Dashboard
    - Navigation Bar
    - Add, edit and delete functions on site wide content.
    - Footer

### **Database**

The noSQL database MongoDB Atlas will be used to handle all the data in the Poddly website, including user details, podcast information and comments. 

## **Skeleton**
---
### **Wireframes**

[Mobile](/readme_assets/mobile.png)\
[Desktop](/readme_assets/desktop.png)\
[Tablet](/readme_assets/tablet.png)

## **Surface**
---
### **Colour Palette**

![Color Palette](/readme_assets/palette.png)

### **Typography**

The website uses the Google Fonts library to provide the fonts:

* Dosis ExtraBold 800 - Used for the directory logo.

![Logo](/readme_assets/Dosis.png)
* Lato - Used for all other text content.

![Text](/readme_assets/Lato.png)

---

## **Database Design** ##

5 collections were used for the construction of the database in MongoDB.
The collection used the most was **podcasts** as it holds the majority of the information required to display information.
There are associations with the following:

- **categories** to **podcasts**
    - category_name

- **channels** to **podcasts**
    - channel

- **service** to **podcasts**
    - streaming_service

- **users** to **podcasts**
    - username

### Categories ###


| Description | Collection Key | Data Type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Name of category | category_name | string |

### Podcasts ###

| Description | Collection Key | Data Type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Category of podcast | category_name | string |
| Name of podcast | podcast_name | string |
| Description of podcast | podcast_description | string |
| Which user added the recipe | added_by | string |
| Channel produced by | channel | string |
| Streaming service available | streaming_service | string |
| What date was it added | added_on | string |
| Cover art | cover | string |
| User comments | comments | array |


### Channel  ###

| Description | Collection Key | Data Type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Channel produced by | channel | string |

### Service  ###

| Description | Collection Key | Data Type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Streaming service available | streaming_service | string |

### Users ###

| Desription | Collection Key | Data Type |
| --- | --- | --- |
| Unique ID | _id | ObjectId |
| Username | username | string |
| Email of user | user_email | string |
| password | password | string |

## **Technologies Used** 
---
### Languages

The primary languages used throughout the development of this project are:

* [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Python3](https://www.python.org/downloads/)
* [JavaScript](https://www.javascript.com/)

### Database

* [MongoDB](https://www.mongodb.com/)

### Front-End Libraries

* [Bootstrap](https://getbootstrap.com//)
* [Google Fonts](https://fonts.google.com/)
* [FontAwesome](https://fontawesome.com/)

### Back-End Libraries

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - The microservice Flask framework is used to handle routing and serving of HTML pages displaying front-end content.
* [Flask-PyMongo](https://docs.mongodb.com/drivers/pymongo/) - Flask's extension 'Flask-PyMongo' is the language used to interact between Flask and the MongoDB database. It handles the data inputted through the website's forms and sends it to the database, as well as retrieving it from the database to be served onto the client's screen.
* [jQuery](https://jquery.com/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - The WSGI web-application library Werkzeug was used to generate hashed passwords, therefore providing password security for the client.

### Other Technologies

* [Google Chrome Devtools](https://developer.chrome.com/docs/devtools/)
* [Favicon.io](https://favicon.io//)
* [XD](https://www.adobe.com/uk/products/xd.html/) - Wireframes were made using Adobe XD software
* [Random Keygen](https://randomkeygen.com/)

## **Bugs & Testing**
Bugs and Testing information can be found in the seperate [Bugs and Testing](/TESTING.md) file.
## Credits

## Deployment

The site is hosted on [Render](https://poddly.onrender.com).

Deployment of the site has been achieved by the steps following below, outlined in the Code Institue Walkthorugh Project:

- Create a new repository within GitHub.
- Create a requirements.txt file by typing "pip3 freeze --local > requirements.txt" in the terminal which tells Render what dependencies are required.
- Create a Procfile for Render by typing "echo web: python app.py > Procfile" in the terminal.
- Push the requirements.txt and Procfile to GitHub.
- Log in to Render and selected "Create New App".
- Select the input field "App Name" and give app a unique name.
- Select a region.
- Click Create App.
- Select Deploy from Render menu.
- Select "GitHub" in Deployment Method.
- Input GitHub repo name and Search.
- Connect
- Select Settings from the Render menu.
- Select Reveal Config Vars and input relevant key/value information from env.py (IP, PORT, MONGO_URI, MONGO_DBNAME, SECRET_KEY) file making sure no quotation marks are used.
- Select Deploy.
- Select Enable Automatic Deployment.
- Select Master Branch in Branch Selected.
- Deploy Branch
- View to launch the app.

## Acknowledgements

* The Code Institute Slack community, has once again throughout this project, been a valuable resource. 
* Stack Overflow is another constant source of helpful guidance and answers to so many questions. 
* My mentor, Spencer Barriball, has been supportive and encouraging throughout this project. 
* The Tutor Support on Code Institute has also been valuable resourse for this project. 
