
# **PODDLY**
## The Community Podcast Directory

This website is designed and created for the Data Centric Development Milestone Project, for Code Institute's Diploma in Web Application Development.

Poddly - The Community Podcast Directory is a free to use online podcast sharing platform, where podcast lovers from around the world can share their favourites, and expand their own library of podcasts with new discoveries shared by the Poddly Community Directory.

The platform will allow users to browse a complete directory of shared podcasts, search by Category, Channels or Name, leave comments, and even give podcasts a thumbs up.

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



## **UX** 
## **Strategy**
--- 
The main aim of the website is to provide a free-to-use podcast resource, which allows the **user** to add podcast suggestions to the site so it can be viewed by other **users**, browse and search for new podcasts, amend and delete their own suggestions and comments. Information presented is clear, intuitive, easy to use.

- To allow the growth of a recipe database for the **user** and by the **user**.
- To allow the **site owner** to encourage the **user** to purchase the cookbooks highlighted on the Bookshop page by directing them to the appropriate Amazon site.
#### **Site Owner Goals**
1. To create an easy to use platform that is intuitive in design, responsive and easy to navigate.
2. Implement CRUD (Create, Read, Update, Delete) functionality, allowing users to add, edit and delete their podcast recommendations.
3. Implement defensive programming using data validation and authentication
4. Create a mobile-first design, while ensuring the website is responsive across all device sizes.

#### **External User Goals**
First Time User - As a casual/first time user who has not created an account, I want to be able to:
- Search for specific podcasts or browse categories and channels
- View podacast reviews including comments and ratings
- Be able to contact for more information and queries
- Create an account

#### **Returning User Goals**
Registered User - As a user who has registered and signed in, I want to be able to:
- Do everything a Causal User can
- Add, edit and delete my own podcast suggestions
- Comment and rate other users suggestions
- Edit my account information
- Delete my account

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
| Send Messages to Admin | 5 | 5 | In |
| Full CRUD Functionality | 5 | 5 | In |
| Page for users to Create, Read, Update, Delete Tracks | 5 | 5 | In |
| Search/Filter by Name/Category/Channel | 5 | 4 | In |
| Podcast Recommendations based on the "liked" podcasts | 4 | 3 | Out |
| Save Podcasts onto a personal listened to/want to listen list | 4 | 4 | Out |
| Add/Edit/Delete Comments | 5 | 4 | In |
| Links to Socials | 3 | 5 | In |
| 'Like' Button for Podcasts | 4 | 4 | In |
| Upload and display user profile picture | 3 | 3 | Out |
| Edit Profile Page | 5 | 5 | In |
| Play selected podcast directly from website | 4 | 1 | Out |
| Display users Apple Podcasts/Spotify playlist | 3 | 1 | Out |
| Manage Podcast categories/channels (as Admin) | 5 | 5 | In |
| Contact Page | 4 | 5 | In |
| 404 Page | 5 | 5 | In |
| Fully Responsive Website | 5 | 5 | In |

In order to complete the project in time for the deployment and submission deadline, functions of less importance will not be implemented in the first release of project, below are the main features to be impletmented for the project:

- Home Page displaying all podcasts
- Ability to Register, Login and Logout
- Contact form
- Full CRUD Functionality to Add, Read, Edit and Delete Tracks
- A page for users to add podcasts to the platform
- Display more information and comments about relative podcast
- Functionality for users to leave comments on podcast cards
- Search/Filter functionality
- 'Like' button, with click counter.
- Profile Page for Users
- Functionality for users to edit profile
- Contact Page
- 404 Page
- Admin Priveleges (to manage Genres and Tracks)

Features for future releases:

- Podcast Recommendations based on the "liked" podcasts
- Save Podcasts onto a personal listened to/want to listen list
- Upload and display user profile picture
- Play selected podcast directly from website
- Display users Apple Podcast/Spotify playlists


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

4. Profile Page - Here users can display and edit their own profile for other users to view. 
    - Navigation Bar
    - Profile Image
    - Details - First Name, Last Name, Age, additional 'About Me' information
    - Personal Podcasts, a list of all podcasts added by this user

5. 'Add a Podcast' Page
    - Navigation Bar
    - Form to add details of a Podcast
    - Footer

6. Contact Page
    - Navigation Bar
    - Contact Form
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

## **Technologies Used** 
---
### Languages

*
*
*
*
### Database

* [MongoDB](https://www.mongodb.com/)

### Front-End Libraries

* [MaterializeCSS](https://materializecss.com/)
* [Google Fonts](https://fonts.google.com/)