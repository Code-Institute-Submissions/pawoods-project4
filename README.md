# Pencil + Paper
Pencil + Paper is an online retail store, selling a range of art and stationery supplies to consumers. The site allows the consumers the ability to see a range of products from different categories and brands, place orders, register and maintain a profile with the site and see updates posted by the store.
➕➕➕➕➕
Am I responsive Image
Link to live site
➕➕➕➕➕
## Table of Contents
-   [UX](#ux)
    -   [User Stories](#user-stories)
    -   [Design](#design)
        -   [Wireframes](#wireframes)
        -   [Data Design](#data-design)
        -   [Visual Design](#visual-design)
            -   [Colours](#colours)
            -   [Fonts](#fonts)
            -   [Icons](#icons)
-   [Features](#features)
    -   [Current Features](#current-features)
        -   [Page Features Matrix](#page-features-matrix)
        -   [User Feature Permissions](#user-features-permissions)
    -   [Future Features](#future-features)
-   [Languages and Technologies](#languages-and-technologies)
-   [Testing](#testing)
    -   [Bugs](#bugs)
        -   [Fixed Bugs](#fixed-bugs)
        -   [Unfixed Bugs](#unfixed-bugs)
-   [Deployment](#deployment)
    -   [Live Deployment](#live-deployment)
    -   [Local Deployment](#local-deployment)
    -   [Requirements and settings](#requirements-and-settings)
    -   [Database](#database)
    -   [Heroku](#heroku)
-   [Credits](#credits)
    -   [Code Credits](#code-credits)
    -   [Support Credits](#support-credits)
## UX
### User Stories
The first part of the planning process was to develop the suer stories that would guide the development and design, these are broken down into the three teirs of users below: 
1. First time (unregistered) user - I should...
    - See a consistent and easily accessible navigation menu with access to all applicable parts of the site.
    - Be able to view products, filtered and sorted to my needs, including further details of each product.
    - See updates from the site, including offers, new products and other news.
    - Be prompted to register to the site, finding an accessbile registration page.
    - Be able to add products to a basket, update or remove if needed and checkout quickly and simply as a guest user.
2. Registered user - I should...
    - Be able to find a sign in page that makes returning to the site quick and simple.
    - See my details on a profile page, including personal, saved shipping information and previous orders.
    - Be able to update my details from the profile page.
    - Be able to add products to a basket, update or remove if needed and checkout, either adding or retrieving saved details from my profile.
3. Site admin - I should...
    - Find options to edit site contents in the menu/profile.
    - Be able to update products, brands, categories and updates from the site interface.
### Design
#### Wireframes
➕➕➕➕➕
For all wireframes, including mobile, tablet and desktop views, please see [WIREFRAMES.md](WIREFRAMES.md) file.
➕➕➕➕➕
#### Data Design
Using a relational database for this project, it was important to design the data from the outset to ensure every element interacted correctly with those it needed to as well as giving the users the best experience of the site.
I drew up the data structure early on in the project to keep in mind when developing so as to avoid having to go back and make changes once everything was up and running. I used the base Boutique Ado walkthrough project as a starting point and then build custom models on top of this to enhance the site.

➕➕➕➕➕
Lucid chart screenshot
➕➕➕➕➕

#### Visual Design
##### Colours
I used [coolors](https://coolors.co/) to design my colour palette, I wanted to keep the majority of the site light in colour to give a clean and simple look while using some darker accent colours for the text, footer, menu and buttons. This was the palette I settled on as it gave a good contrast between the light and dark colours while not being visually overwhelming for the user.

➕➕➕➕➕Coolors image➕➕➕➕➕
##### Fonts
I used [Google Fonts](https://fonts.google.com/) for the fonts on the site, choosing to user one font for the logo and page/section headers and another for the majority of the text on the site. Using sample text for the site, I settled on ➕➕➕➕➕
##### Icons
I used [Font Awesome](https://fontawesome.com/) for all the icons on the site, using them to draw the attention of the user either to a navigation or CTA element or to important areas of information, brand labels, payment information etc.

➕➕➕➕➕Icon Images➕➕➕➕➕
## Features
### Current Features
#### Page Feature Matrix
#### User Feature Permissions
### Future Features
## Languages and Technologies

## Testing

➕➕➕➕➕

For all manual user testing, lighthouse performance testing and code validation, please see [TESTING.md](TESTING.md) file.

➕➕➕➕➕

### Bugs

#### Fixed Bugs
1. Bug found when adding updates to the carousel, active attribute was being set to all slides in the loop - Fixed by adding if statement to check forloop.counter == 1 to only set active to the first update slide in the loop.

2. Bug found where update link was not submitting the form on basket page - this was caused by empty href tags left on the links element, removing them fixed the issue.

3. Bug found where remove link on basket page threw an error for missing or incorrect csrf token - moving this function from the script.js file directly into the postload block on the basket.html page fixed the issue.

#### Unfixed Bugs
## Deployment
### Live Deployment
### Local Deployment

local environment

pip3 install -r requirements.txt
add host to allowed hosts
python3 manage.py migrate
python3 manage.py createsuperuser
- Enter username
- Enter email address
- Enter Password
- Confirm Password
Superuser is created

### Requirements and Settings
### database
### Heroku

## Credits

### Code Credits

Back to Top button - [CodePen](https://codepen.io/Shiko/pen/NxpZae) - Roman

List specific field of query set - [Reddit](https://www.reddit.com/r/django/comments/x4vgcs/how_to_get_all_the_ids_into_a_list/) - User Deleted

### Support Credits