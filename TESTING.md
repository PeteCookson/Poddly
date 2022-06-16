<span id="top"></span>

Back to [README](README.md)

## Index

- [Strategy](#strategy)
* [Site Owner Goals](#site-owner-goals)
* [External User Goals](#external-user-goals)
* [Returning User Goals](#returning-user-goals)
- [Bugs & Testing resolved](#bugs-&-testing)
- [Bugs & Testing unresolved](#bugs-&-testing)

---
## **Strategy**
--- 
The main aim of the website is to provide a free-to-use podcast resource, which allows the **user** to add podcast suggestions to the site so it can be viewed by other **users**, browse and search for new podcasts, amend and delete their own suggestions. Information presented is clear, intuitive, easy to use.

- To allow the growth of a podcast database for the **user** and by the **user**.
- To allow the **site owner** to encourage the **user** to engage in recomemnding podcasts and leaving comments and feedback on other users recommended podcasts.


### **Site Owner Goals**
**To create an easy to use platform that is intuitive in design, responsive and easy to navigate.**
- This has been acheived by using a simple design, minimal colors for clarity of purpose, clear buttons and links with a focus on quality content.

**Implement CRUD (Create, Read, Update, Delete) functionality, allowing users to add, edit and delete their podcast recommendations.**
- A user that is logged in has the aility to recommend a Podcast (Create),view (Read) the entire directory, edit (Update) any podcast the user has recommended, and also delete those podcasts from the Poddly Directory.

**Implement defensive programming using data validation and authentication.**
- This is achieved by way of modals to confirm deletion of content, registration and login to restrict access and an Admin Dashboard.
---

### **External User Goals**

**First Time User - As a casual/first time user who has not created an account, I want to be able to:**

**Search for specific podcasts or keyword**
- The search field is available to all users.

**View podacast descriptions including other users comments**
- The directory of podcasts is available to all users, as are the content modals with description, comments and additional information.
**Register and create an account**
- This function is available to all user not registered.
---
**Returning User Goals**

**Registered User - As a user who has registered and signed in, I want to be able to:**

**Do everything a Causal User can**
- This is the basic function that requires no user authentication.

**Add, edit and delete my own podcast suggestions**
- Recommending or "adding" a podcast to the directory is limited to registered users, podcasts that a logged in user recommends are able to be edited or deleted, but only by that specific user.

**Comment on other users recommendations**
- This function is accessed directly through the podcasts modal.

**Edit my podcast information**
- See above

**Delete my podcasts**
- See above

---
**Admin - As an administrator, I want to be able to:**

**Add, Modify and Delete any catagory and/or channel**
- The Admin Dashboard allows the admin user to add/edit/delete categories, channels and streaming services.
---

## Manual testing

The following tests have been carried out without issue:

**Navigation bar**

- The Poddly logo returns the user to the Podcast directory page.
- The correct menu icons options appear depending on the user's session status:
  - **Not logged in**: Home, Log In, Register
  - **Logged in**: Home, Recommend a Podcast, Log Out
  - **Logged in as "admin"**: as above plus Admin Dashboard
- Selecting each link takes the user to the relevant page, or logs the user out.

**Home page**

- Cards function as expected, open modals, and only shows add comment if logged in, or edit if user posted the podcast.
- Links to Log In and Register direct to the correct forms.
- Recommend a Podcast only appears if user is logged in.

**Register page**

- The 'Log In' link takes the user to the Log In page.
- If username and/or password does not match the form validation, a Flash message is printed.
- Submitting a username and/or email that has already been registered prints a Flash message.
- When the 'Register' button is tapped/clicked with valid details, the user is redirected to the Podcast page and a Flash messages indicates they have successfully registered.
- On registering, the new username and password are added to the Users collection on the database.

**Log In page**

- Entering a username or password not matching the form validation highlights the issue to the user.
- Entering either an incorrect username or password displays a Flash indicating "Incorrect Username and/or Password".
- When the 'Log In' button is tapped/clicked with valid details, the user is redirected to the Podcast page and aFlash including their username indicates they have successfully logged in.


**Activities page**

Search functionality:

- After entering a term in the search field and using the search icon or pressing Enter, the correct results are displayed from the indexed fields (podcast_name, category_name, channel).
- If no results are found, a message to the effect appears.

<span id="testing-auto"></span>

## Automated testing

[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

[W3C - HTML](https://validator.w3.org/) 

[W3C - CSS](https://jigsaw.w3.org/css-validator/)

[CSS Lint](http://csslint.net/)

### Browsers

Tested on:

- Chrome
- Firefox
- Safari (iOS)

### Screen sizes

Tested with Chrome DevTools using profiles for:

- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5 SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X
- iPad
- iPad Pro

Physical testing on:

- iPhone XSmax
- Macbook Pro Retina 13'
- Imac 27" 
- Philips 27" desktop monitor


