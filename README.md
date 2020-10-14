# Body Coach 

[Body Coach](https://foodfactoryrecipes.herokuapp.com/) has been updated for 2020, the new plans give you the tools to transform your body and get you fitter, stronger, healthier and happy. 15 new and exclusive real-time workouts, online support from our team of support coaches, and access to our official Facebook community group.
## UX

### Project Goal

[FILL IN]:
- Browse recipes
- 

#### User goals
- Sign up to a fitness/nutrition plan that will improve my health and wellbeing.
- Browse and potentially purchase products from the site.

#### Business goals
- Maximise uptake of the fitness and nutition plans.
- Drive a new income stream from the new kitchenware range.

#### User Stories

As a user visiting the site, I would like:
- Select a fitness plan that is right for my needs.



### Wireframes

[Figma](https://www.figma.com/) was used to produce the wireframes for the desktop and mobile layouts of the site.

- [Desktop]()
- [Mobile]()

## Existing Features
### Elements on All Pages 

**Navbar**
- Logo - conventionally positioned top left and reloads the page
- Home - takes the user back to the home page from anywhere on the site.
- Kitchenware - dropdown menu that allows users to view products by category or "All".
- Search - Users can enter a search term to filter the products listed on the site.
- ```if user.is_authenticated``` 
- The nav has class ```navbar-expand-lg``` applied so the full navbar is available for larger screen sizes.
- The has also been set to ```sticky-top``` so it is always available to the user for easy navigation whatever the scroll position of the window.

**Footer**

- Features social media icons. 
- The links have the ```target=_blank``` property to open these platforms in a new window. 
- The links point to the homepage of each platform at this time.

### Home Page

**Hero Image**
- 

**Get Started Button**
- 
### Products Page



- 

### Product Detail Page
- 

<div align="center">
<img src="" alt="Form Validation" >
</div>


### Bag
- 

### Checkout Page
- 

### Checkout Success Page


## Features Left to Implement
**Pagination** 
- 
**Plans App** 
- 








## Technologies Used


- This project was built with HTML, CSS, JavaScript & Python programming languages.
- [jQuery](https://jquery.com/)
    - Used for responsive navbar and DOM manipulation
- [Popper.js](https://popper.js.org/)
    - Also used for the responsive, collapsible navbar.
- [Gitpod](https://www.gitpod.io/)
    - The developer chose this IDE to compile all code for this project.
- [GitHub](https://github.com/)
    - Used for version control.
- [Bootstrap](https://getbootstrap.com/)
    - This was used to provide a structured layout and ease of making the site responsive.
- [Google Fonts](https://fonts.google.com)
    - Text elements were styled using **Google fonts**.
- [Fontawesome](https://fontawesome.com/)
    - The source for all iconography.
- [Jinja](http://jinja.pocoo.org/docs/2.10/) templating logic to construct html.


# Testing 

### Code Validation

Validation tools were used to check that the website code was valid:

- [W3C Mark Up Validation](https://validator.w3.org) for HTML.
    - Passed test with no warnings.
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) for CSS.
    - Passed all tests with no issues.
- [JSHint](https://jshint.com/) for JavaScript.
    - One warning regarding an unused variable ```validation```. My feeling is that this is an empty array until the form **submit** button is clicked and the script then checks for forms with the ```needs-validation``` class.
- [PEP8](http://pep8online.com/) for Python
    - 3 ```line too long``` issues and 1 ```trailing whitespace```. 

### User Stories Testing

**To be inspired to cook by the range of recipes**


### Manual Functionality Testing

**Browsers**

The site was tested on the following browsers: Chrome, Firefox, Safari, Internet Explorer & Edge on desktop and laptop devices.

**Mobile Devices**

- The devices used for testing were:
    - iPhone 6s, XR
    - iPad Air 
    - Samsung S10

**Navigation**

- On desktop, go to the landing page.
- Reduce the browser size down to verify that the navbar is responsive and switches from the expanded, inline menu to burger menu at the medium screen size.
- Check that the burger button expands and collapses the menu to give access to the nav items.
- Click on the **Body Coach** logo in the top left of the navbar and the **home** link in turn and confirm that both link to the home page. 
- Click on the kitchenware dropdown and select each dropdown category in turn and verify it takes the user to the relevant product page.
- 
- Check that the navbar becomes sticky when the window is scrolled down.
- All above functionality and checks carried out on tablet and mobile.

**Hero Image and Get started button**

- Check all screen sizes and confirm that the background image looks good.
- 













# Deployment

## How to run this project locally

Here are instructions to run this project within your chosen IDE:

Pre-requisites:
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). 
    - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

### Instructions

1. Follow this link to the [Body Coach repository](https://github.com/jpg6453/body-coach/). 
2.	Click the green **Code** button.
3.	A Clone with HTTPs modal appears on screen, copy the clone URL for the repository.
4.	Within your chosen IDE launch a terminal session
5.	Ensure the current working directory is the location where you want the cloned directory to be made. Change this if necessary.
6.	Type ```git clone```, and then paste the URL copied in Step 3.
```
git clone https://github.com/jpg6453/body-coach
```

7.	Press **Enter** and a clone will be created locally. This could take a few minutes.

8. In terminal, install all required modules with the command 
```
pip -r requirements.txt
```
9. Create an environment variable and set this to the value of your MONGO_URI. How to do this will vary by IDE and individual set-up.
10. You can now run the application with the command
```
python3 manage.py runserver
```

9. You can visit the website at `http://127.0.0.1:5000`

## Heroku Deployment

To deploy the project to heroku:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add`, `git commit` the requirements and Procfile and then `git push` the changes to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
AWS_ACCESS_KEY_ID | < ENTER VALUE >
AWS_SECRET_ACCESS_KEY | < ENTER VALUE >
DATABASE_URL | < postgres://.....>
SECRET_KEY | < ENTER VALUE >
STRIPE_PUBLIC_KEY | < ENTER VALUE >
STRIPE_SECRET_KEY | < ENTER VALUE >
USE_AWS | TRUE




8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

## Credits


**Images**

- Hero Image [Pixabay](https://pixabay.com/)

- Product Images [The Body Coach](https://www.thebodycoach.com/)

**Code**

- Code Institute Course Material
- [Corey Schafer Python Tutorial](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

## Acknowledgements

A big thank you to my Code Institute Mentor, Maranatha Ilesanmi, for demonstrating concepts and providing focus when time was tight! 

## Disclaimer

- This project was developed for educational purposes and all images are licence free.

