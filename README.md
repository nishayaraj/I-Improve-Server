# I-Improve: Server
### i-improve in action: https://www.loom.com/share/3cd63fe91e7f40919020f7cee7de19f3

I-Improve is a web application designed to provide users with a personalized and accountable approach to goal tracking. In a market flooded with generic goal-tracking apps, I-Improve aims to offer a unique experience that encourages users to take ownership of their goals.

The app uses modern web development technologies such as HTML, CSS, JavaScript and React on the front-end, while the back-end is powered by Python, Django and SQLite. The user interface is designed to be intuitive and user-friendly, making it easy for users to navigate and use the app.

## Project Overview
Using I-Improve, users can create, update, and delete their goals, along with adding key metrics to break down their targets. Once the due date arrives, the app prompts users to do a retrospective analysis. This analysis helps users identify what went right, what went wrong, and create an action plan based on the findings.

### Features
- Users can sign in to the app with Google
- Landing/Welcome Page/ My Goals:
   - This page displays all user-created goal cards, with due date, tags and completion rate
   - "Add new goal button" takes the user to the goal form to create a new goal.
   - If due date is passed, "Edit goal" button disabled and "Start retro" button highlighted
   - "View goal" button opens individual goal data, with tags, due date and associated key metrics
   - You can add new key metrics to a goal by clicking the "Add new key-metrics button"
   - Goal can be updated using "Edit goal" button and deleted using "delete goal" button.
- Manage Tags Page:
   - Displays all the tags created by the user.
   - The user can add new tags by clicking the "Add new tag" button.
   - Tags can be deleted by clicking the "delete" button on the tag cards.
- Retro Button on Goal Card:
   - On click directs user to Retro form with guided questions on what went well, what to improve and one action item to succeed in future.
   -  The button is highlighted once user passes due date.
   - The button is always active.
- Action Items Page:
   - Displays all the action items created by the user in the Retro Process.

## Try out i-improve/ Run Locally
This is the server side repo of i-improve.
To try the client side repo, [click here](https://github.com/nishayaraj/I-Improve-Client). Read the repository's ReadMe for instructions on how to get the frontend on your local machine

1. Clone i-improve server to your machine
```bash
git clone git@github.com:nishayaraj/I-Improve-Server.git
```
2. Navigate into the directory
```bash
cd I-Improve-Server
```
3. Install packages
 ```bash
 pipenv install
 ```
4. Set up virtual environment
 ```bash
 pipenv shell
 ```
5. Make migrations
```bash
python manage.py makemigrations iimproveapi
```
```bash
python manage.py migrate
```
6. Seeding the database
- **Option 1**
  - Create a file called seed.sh at the root level of the Project
  - Add the following commands in the file

     - rm -rf iimproveapi/migrations
     - rm db.sqlite3
     - python manage.py migrate
     - python manage.py makemigrations iimproveapi
     - python manage.py migrate iimproveapi
     - python manage.py loaddata users
     - python manage.py loaddata tags
     - python manage.py loaddata retros
     - python manage.py loaddata key_metrics
     - python manage.py loaddata goals
     - python manage.py loaddata goal_tags

- Then Run these commands one by one to finish seeding the database.
```bash
chmod +x seed.sh
```
```bash
./seed.sh
```

- **Option 2**
 - Another option is to run the following commands **one by one** in the terminal
 ```bash
     python manage.py loaddata users
     python manage.py loaddata tags
     python manage.py loaddata goals
     python manage.py loaddata key_metrics
     python manage.py loaddata retros
     python manage.py loaddata goal_tags
```

7. Starting the API server
```bash
python manage.py runserver
```
## Planning
- [ERD](https://dbdiagram.io/d/63dad405296d97641d7dca1e).
- [App Wireframes](https://whimsical.com/i-improve-8B3aqYMnxcQXSpwPP5DvZc).

## Tech Stack
### Frontend
<div align="center">
<a href="https://reactjs.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/react-original-wordmark.svg" alt="React" height="50" /></a>
<a href="https://getbootstrap.com/docs/3.4/javascript/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/bootstrap-plain.svg" alt="Bootstrap" height="50" /></a>
<a href="https://en.wikipedia.org/wiki/HTML5" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/html5-original-wordmark.svg" alt="HTML5" height="50" /></a>
<a href="https://www.javascript.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/javascript-original.svg" alt="JavaScript" height="50" /></a>
<a href="https://firebase.google.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/firebase.png" alt="Firebase" height="50" /></a>
</div>

</td><td valign="top" width="33%">

### Backend
<div align="center">
<a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50" /></a>
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/django-original.svg" alt="Django" height="50" /></a>
<a href="hhttps://www.sqlite.org/index.html" target="_blank"><img style="margin: 10px" src="https://user-images.githubusercontent.com/33158051/103467186-7b6a8900-4d1a-11eb-9907-491064bc8458.png" alt="SQLite" height="50" /></a>
</div>

</td><td valign="top" width="33%">
