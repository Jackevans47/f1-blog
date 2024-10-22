# Deployment

- The app was deployed to [Heroku](https://dashboard.heroku.com).
- The database was deployed to [PostgreSQL](https://dbs.ci-dbs.net/).

- The app can be reached by the [link](https://f1-blog-project-4-e7ef4f08fdeb.herokuapp.com/).

---

## Local deployment

*Note:*
  - This project requires to install all the requirements:
  - Open the terminal window and type:
  - `pip3 install -r requirements.txt`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/Jackevans47/f1-blog).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/Jackevans47/f1-blog.git`
 
  ---

  1. Install the dependencies:

    - Open the terminal window and type:
    - `pip3 install -r requirements.txt`


1. Create a `.gitignore` file in the root directory of the project where you should add env.py and __pycache__ files to prevent the privacy of your secret data.

1. Create a `.env` file. This will contain the following environment variables:

    ```python
    import os

      os.environ['SECRET_KEY'] = 'Add a secret key'
      os.environ['DATABASE_URL'] = 'will be used to connect to the database'
      os.environ['DEBUG'] = 'True'
    ```

    *During the development stage DEBUG is set to True, but it is vital to change it to False.*

1. Run the following commands in a terminal to make migrations: 
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
1. Create a superuser to get access to the admin environment.
    - `python3 manage.py createsuperuser`
    - Enter the required information (your username, email and password).
1. Run the app with the following command in the terminal:
    - `python3 manage.py runserver`
1. Open the link provided in a browser to see the app.

1. If you need to access the admin page:
    - Add /admin/ to the link provided.
    - Enter your username and password (for the superuser that you have created before).
    - You will be redirected to the admin page.

---

## Heroku Deployment

* Set up a local workspace on your computer for Heroku:
    - Create a list of requirements that the project needs to run:
      - type this in the terminal: `pip3 freeze > requirements.txt`
    - Commit and push the changes to GitHub
    
* Go to [www.heroku.com](www.heroku.com) 
* Log in or create a Heroku account.
* Create a new app with any unique name <name app>.

  <img width="1301" alt="create app" src="https://github.com/user-attachments/assets/e397f3f9-9e55-4d9d-9fff-bb1b56a57617">

  * Create a Procfile in your local workplace:

  ![Heroku. Procfile](https://github.com/user-attachments/assets/164a9de2-303b-4207-8df1-61495a2e88a8)

    
    This file will will contain the following:
    ```python
        web: gunicorn <name app>.wsgi:application
    ```
    - Commit and push the changes to GitHub.
 
      * Go to the settings app in Heroku and go to Config Vars.

<img width="689" alt="settings" src="https://github.com/user-attachments/assets/a6015086-0454-4184-8e33-dc63af1410d1">

Click on Reveal Config Vars and add the following config variables:

| Key      | Value          |
|-------------|-------------|
| DATABASE_URL | ... | 
| DISABLE_COLLECTSTATIC | 1 |
| CLOUDINARY_URL | ... |
| SECRET_KEY | ... |

* Copy the value of DATABASE_URL and CLOUDINARY_URL then input it into the .env file and generate a secret key (you may use [Djecrety](https://djecrety.ir/) for secret key generation).
* Migrate changes.
* Set debug to False in settings.py
* Commit and push the changes to GitHub.
* Connect your repository to Heroku.

<img width="1413" alt="deploy page" src="https://github.com/user-attachments/assets/2d934f3c-0c35-4c02-9b63-73a6422867b9">


* Deploy the app to Heroku by clicking "Deploy Branch" button. If you want to enable auto-deployment, click "Enable Automatic Deployment".

  <img width="194" alt="enable automatic deploy" src="https://github.com/user-attachments/assets/49522b6e-2cb9-4c9e-90eb-d3f5962322f5">

<img width="628" alt="deploy branch" src="https://github.com/user-attachments/assets/ff5e0a24-b8be-4d6e-8064-f8bd91b5b36c">

The deployment process will start.

<img width="789" alt="deloyment proccess" src="https://github.com/user-attachments/assets/271c9a91-2f84-42a7-a07c-171073e6b347">


Click "View build logs" to see the progress of the deployment.

 <img width="1250" alt="view logs" src="https://github.com/user-attachments/assets/db42c3bc-10fb-4b3c-933e-8bb1cb3a78c6">

*Due to security updates, Heroku dashboard will not allow you to deploy your app from GitHub. Thus, you need to run the following commands in your terminal:*

| action | terminal command | comment |
| ------ | ---------------- | ------- |
| login to your heroku account | `heroku login -i` | |
| create a new app on heroku | `heroku create NAME-OF-YOUR-APP` | if you haven't created the app before, and then, you can access the app via the Heroku dashboard and set up your config vars.|
| add remote to your local repository | `heroku git:remote -a NAME-OF-YOUR-APP` | if you have already created app on Heroku (before the security updates) and connected it using Heroku dashboard |
| deploy new version of the app | `git push heroku main` | |
| rename app | `git remote rename NAME-OF-YOUR-APP NAME-OF-YOUR-APP-2` | |

**Final Deployment**

* Set debug to False locally + delete DISABLE_COLLECTSTATIC from config vars in Heroku dashboard.
* Commit and push the changes to GitHub.
