# Pencil + Paper
Pencil + Paper is an online retail store, selling a range of art and stationery supplies to consumers. The site allows the consumers the ability to see a range of products from different categories and brands, place orders, register and maintain a profile with the site and see updates posted by the store.

## About Us


![Am I Responsive Screenshot](/media/readme/amiresponsive.webp)

View live site [here!](https://project-4-pawoods-21f8fc070c89.herokuapp.com/)
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
    -   [Future Features](#future-features)
-   [Languages and Technologies](#languages-and-technologies)
-   [Testing](#testing)
    -   [Bugs](#bugs)
        -   [Fixed Bugs](#fixed-bugs)
        -   [Unfixed Bugs](#unfixed-bugs)
-   [Deployment](#deployment)
    -   [Local Deployment](#local-deployment)
    -   [Live Deployment](#live-deployment)
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
    - Be able to add products to a basket, update or remove if needed.
    - Checkout quickly and simply as a guest user.
2. Registered user - I should...
    - Be able to find a sign in page that makes returning to the site quick and simple.
    - Be able to like products with a click and see feedback to denote my liked products on the product page.
    - See my details on a profile page, including personal, saved shipping information, previous orders and wish list items.
    - Be able to update my details from the profile page, including removing liked products from my wishlist.
    - Checkout, either adding or retrieving saved details from my profile.
3. Site admin - I should...
    - Find options to edit site contents in the menu/profile.
    - Be able to update products from the site interface.
    - Be able to update posts from the site interface.
    - Be able to remove produts or posts from the site interface.
    - Have a lin kto access the django admin panel.

### Design
#### Wireframes

For all wireframes, including mobile, tablet and desktop views, please see [WIREFRAMES.md](WIREFRAMES.md) file.

#### Data Design
Using a relational database for this project, it was important to design the data from the outset to ensure every element interacted correctly with those it needed to as well as giving the users the best experience of the site.
I drew up the data structure early on in the project to keep in mind when developing so as to avoid having to go back and make changes once everything was up and running. I used the base Boutique Ado walkthrough project as a starting point and then build custom models on top of this to enhance the site.

![Data Model Design](/media/readme/modeldatabase.webp)

#### Visual Design
##### Colours
I used [coolors](https://coolors.co/) to design my colour palette, I wanted to keep the majority of the site light in colour to give a clean and simple look while using some darker accent colours for the text, footer, menu and buttons. This was the palette I settled on as it gave a good contrast between the light and dark colours while not being visually overwhelming for the user. To add additional colours to the site, I used the alpha values in colours to simply darken or lighten depending on the theme of the element.

![Coolors Image](/media/readme/coolors.webp)

##### Fonts
I used [Google Fonts](https://fonts.google.com/) for the fonts on the site, choosing to user one font for the logo and page/section headers and another for the majority of the text on the site. Using sample text for the site, I settled on Nunito for the main site text and smaller headers and PT Serif for the Site logo and larger headers:

PT Serif

![PT Serif Imge](/media/readme/ptserif.webp)

Nunito

![Nunito Image](/media/readme/nunito.webp)

##### Icons
I used [Font Awesome](https://fontawesome.com/) for all the icons on the site, using them to draw the attention of the user either to a navigation or CTA element or to important areas of information, brand labels, payment information etc.

![Icons Image](/media/readme/icons.webp)


## Features

Before developing the project, i made a list of the features i wanted to include and ordered them from most to least essential for the design brief, below are the features split into current and future sections:

### Current Features

- Home page with information about the site/store
- Nav menu element to compile all relevant links for the user
- Ability to search products by keywords, or filter by brands, categories and sub categories
- Product page with ability to sort and filter products
- Product details page showing more in depth information on the products
- Ability to select quantity pf product and add to basket
- Basket view with option to update quantity and remove products, return to products or go to checkout
- Checkout page with order summary and form to complete shipping and payment details
- Order confirmation page with order details and a link to continue shopping
- Profile page with ability to view and update details, view order history and wish list products
- Update posts which could include new offers, ranges or store information
- Ability to add and remove products to with list for signed in users
- Admin option to add, update and remove products from the store with relevant form page
- Admin option to add, update and remove update posts from the store with relevant form page

### Future Features

- Add UI CRUD functionality for brands, categories and sub categories for admin users to update these classifications from the site rather than the django admin page.
- Add a Contact Form using the email feedback system integrated with the order confirmation.
- Add messages set through the Contact Form to the relevant user profiles and allow admin access to view all messages.

## Languages and Technologies

| Language/Technology | Use/location in Project                                                                                                                                                                                                                |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HTML                | Used to build templates for all pages on site                                                                                                                                                                                          |
| CSS                 | Used to customise materialize styling on all elements                                                                                                                                                                                  |
| JavaScript          | Used to initialize Bootstrap elements, handle qty selection buttons in product detail and basket templates and price selection on product add page                                                                                     |
| Python              | Used for majority of logic on site, processing data between database and front end                                                                                                                                                     |
| CI DB Tool             | Storing data entered by users                                                                                                                                                                                                          |
| Django               | Used to create views, urls, templates and static files housing majority of python logic                                                                                                                                                               |
| Django Templates               | Used to template front end sites, using loops over lists and if statements to check user status                                                                                                                                        |
| Codeanywhere        | Used as the dev environment for the project                                                                                                                                                                      |
| Git        | Used for version control within development environment                                                                                                                                                                      |
| GitHub        | Used to store project repo                                                                                                                                                                      |
| Heroku              | Used to deploy the live site                                                                                                                                                                                                           |
| Bootstrap         | Used for many individual elements; menu, accordion, cards, reveal elements, modals, tooltipped elements and action buttons. Also used for basic styling with helper classes for colour, button size, element positioning and size etc. |
| Google Fonts        | Used for site fonts;                                                                                                                                                                                          |
| Font Awesome        | Used for icons within the menu element                                                                                                                                                                                                 |
| Favicon             | Used for site favicon                                                                                                                                                                                                                  |
|Code Institute Python Linter | Used to test for Pep8 compliance |
|W3 HTML Validator| Used to test all HTML files|
|W3 CSS Validator|Used to test CSS file|
|JsHint|Used to Test JavaScript File|
|Chrome Dev Tools|Used as primary browser during development|
|Lighthouse (Chrome)|Used to check code standards|

## Testing

For all manual user testing, lighthouse performance testing and code validation, please see [TESTING.md](TESTING.md) file.

### Bugs

#### Fixed Bugs

1. Bug found when adding updates to the carousel, active attribute was being set to all slides in the loop - Fixed by adding if statement to check forloop.counter == 1 to only set active to the first update slide in the loop.

2. Bug found where update link was not submitting the form on basket page - this was caused by empty href tags left on the links element, removing them fixed the issue.

3. Bug found where remove link on basket page threw an error for missing or incorrect csrf token - moving this function from the script.js file directly into the postload block on the basket.html page fixed the issue.

4. Bug with codeanywhere using environment variables, worked well for STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY but not for _STRIPE_WH_SECRET - fixed by setting the STRIP_WH_SECRET in an env.py file and adding if statement to import the file to settings.py and similarly to decide whether to use os.environ.get or os.getenv to allow getting the environment variable from Heroku

5. Bug found where stripe payment intent only holds a full name field where I am using first and last name - Fixed by adding the names individually to the payment intent metadata and concatenating both to form the shipping and billing name

#### Unfixed Bugs

Where an item is deleted and is the only item on an order, the order remains in the database but with a value of 0.00. With more time to fix, I would enter conditional statements to either delete or just not display orders with a 0 value

## Deployment

The site was deployed to [Heroku](https://www.heroku.com/platform). View the live site [here!](https://project-4-pawoods-21f8fc070c89.herokuapp.com)

### Local Deployment

To access this [GitHub Repository](https://github.com/pawoods/project4) locally, you can follow the below guides to either clone or fork the repo.

#### Cloning

Cloning this repository will pull down a full copy to a local computer or remote virtual machine within a codespace. You can then `push` or `pull` your own or other users changes to the original repo. To clone this repo, follow the below step by step instructions:

1. Navigate to the [GitHub Repository](https://github.com/pawoods/project4) for this project.
2. Click the `<> Code` button above the list of files.
3. Chose whether to clone using HTTPS, SSH, or GitHub CLI and copy the URL.
4. Open Git Bash or Terminal.
5. Change the current working directory to the location where you want the cloned repo.
6. Use the `git clone` command followed by the copied URL.
   ```
   git clone https://github.com/pawoods/project4.git
   ```
7. Press enter to create your local clone.

#### Forking

Forking this repository will create a parallel version in your own GitHub account, allowing changes to be made with no change to the original repo. To fork this repo, follow the below step by step instructions:

1. Navigate to the [GitHub Repository](https://github.com/pawoods/project4) for this project.
2. Click `Fork` button in top right under main navigation bar.
3. A copy of this repo should now exist in your GitHub account.

#### Requirements and env

After cloning or forking the repo, the dependancies within the requirements.txt need to be installed using the command `pip3 install -r requirements.txt`

Any other packages installed in the project after cloning or forking the repo can be added to the requirements.txt file by using the command `pip3 freeze --local > requirements.txt`

An `env.py` file will also need to be created at root-level to contain environment variables that should not be pushed to GitHub, the `env.py` file is listed in the `.gitignore` file to ensure this.

If you are using an IDE such as GitPod or Code Anywhere, these environment variables call also be saved on the account or exported in the command line as seen below:

```
export VARIABLE_NAME=variable_value
```

### Local Django Setup

To set up Django, once instilled, you will need to allow your local host by adding the host url to the `ALLOWED_HOSTS` Variable in the settings.py file.

You will then need to migrate the models and fixtures to the local db by following the commands below:

```
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
python3 manage.py createsuperuser
Enter username
Enter email address
Enter Password
Confirm Password
```
The data in the fixtures will then need to be loaded with the command `python3 manage.py loaddata --fixture name` taking care to add the Categories and brands first, followed by the subcategories, products and updates/posts.

### Live Deployment

#### Database
To create the live database, I followed the steps below:

1. Follow CodeInstitute internal tool link for creating a database, copy URL from confirmation email to use in Heroku Environment Variables.
2. Update database URL in the settings.py file of the project, add if statement to check if 'DATABASE_URL' in os.environ and if so, use the DATABASE_URL variable from the environiment.
3. Run show migrations command to check the new database has been connected (all migrations should show as needing to be made) and then make the migrations and load data from fixtures, taking case to pay attention to the order; Categories, subcategories, brands, products, updates.
4. Create superuser with the method previously shown, this time for the live environment.


#### Heroku
To deploy your app on [Heroku](https://www.heroku.com/platform), these are the steps to follow: 

1. Sign up for an account with Heroku.
2. Click New button and select Create New App.
3. Choose a name for your app. This must be unique.
4. Select a region and click Create App.
5. Choose your connection method, I used automatic deployment from GitHub repo. 
6. Make sure your GitHub profile is displayed and search for the repository. You may need to connect to your GitHub account if not completed at registration.
7. Once the repo is found, click connect.
8. Navigate to Settings tab and click on Reveal Config Vars
9. Add config vars of Stripe; STRIPE_WH_SECRET, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY and DATABASE_URL for the db created in the last section.
10. From the terminal - Heroku login - confirm in browser
11. `heroku confi:set DISABLE_COLLECTSTATIC = 1 --app herokuappname` to prevent the following commit and push from attempting to pick up static files as we are not yet set up with AWS for storage.
12. Add heroku app name to ALLOWED_HOSTS variable in settings.py
13. Commit and push changes and then push to heroku with `git push heroku main` - initialise the app if created on the website with `heroku git:remote -a herokuappname`
14. Generate a django secret key, save to the config vars in heroku as SECRET_KEY and change the settings.py file to get from the environment and default to empty string
15. Once deployed, you will need to set development to true in the development environemt, either through environment variables or exporting the variable with `export DEVELOPMENT=True`
16. Once all config vars are added, you can now navigate back to the deploy tab and click Enable Automatic Deploys, select the branch to deploy and click Deploy.
17. Once complete, you can click Open App to view the live site.
- NOTE: The live site will now update any time changes are pushed to the connected GitHub repository.


#### Stripe
The following steps are those I used to connect to [Stripe](https://stripe.com/gb) for payments through the site:

1. Sign up for account
2. erify account from account verification email
3. Click developers option and API Keys tab to find stripe public key and secret key
4. These can be saved in environemt variable in a developement environment or in an env.py file within the environment, they can also be exported using the command 
```
export VARIABLE_NAME=variable_value
```
6. Run server in the development environment and copy the URL
7. in the Webhooks tabs in stripe, click add enpoint, paste the environment URL in and select all events. Once created, the signing secret can be revealed and copied into the environment with the export command or directly into environment variable as STRIPE_WH_SECRET


#### AWS
1. Sign up for account on free tier
2. Navigate to the S3 product and create a new bucket, mimicking the name of the project for ease of use.
3. Within this bucket, create a media/ folder to hold the initial media items for the site.
4. Navigate to IAM to create a User Group, a policy relating to the User Group and a User to be put into the group.
5. Once the user is created, you will need to download the CSV file with the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY values in, saving these to your live environment. 
6. The bucket name and AWS region will alos need to be updated in the settings.py file to match the newly created AWS bucket.
7. In your live environment, remove the config var for DISABLE_COLLECTSTATIC. On the next commit and push, AWS will pick up the static files.


#### Email
To connect to real emails, you will need to connect to an email account and create and app password, for this project, I have done this with Gmail as outlined in the steps below:
1. Sign into Gmail or sign up for a free account. 
2. Access the settings menu and set up 2-Step verification
3. Once completed, you can access a setting to create App Passwords
4. Once created, this can be added to the environment variables along with the email account which will then be picked up by the settings in settings.py (Gmail)

## Credits

### Code Credits

Back to Top button - [CodePen](https://codepen.io/Shiko/pen/NxpZae) - Roman

List specific field of query set - [Reddit](https://www.reddit.com/r/django/comments/x4vgcs/how_to_get_all_the_ids_into_a_list/) - User Deleted

Redirect to page that requested a view - [Reddit](https://www.reddit.com/r/django/comments/c54ycv/how_to_conditionally_redirect_a_django_view/) - NotSelfAware

### Support Credits

I would like to thank my cohort, including cohort leads, Amy, Irene and Iris for their support over the entire course and expesically during the challenging times with CodeAnywhere and other issues along this journey. 

My mentor Martina has also been a huge support throughout the course and has kept me on track when issues have arisen within the projects. 