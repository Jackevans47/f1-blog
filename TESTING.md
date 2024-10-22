# Testing

## Manual Testing

Testing was done throughout site development.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.

|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Home        |                        |                  |      |             |
| 1           | Click on the "Home" button | To be directed to the home page | Y | Available to everyone |
| 2           | Click on "About" button | Directed to the about page | Y | Available to everyone |
| 3           | Click on "Register" button | Directed to the register page| Y | Available to everyone|
| 4           | Click on "Login" button | Directed to the login page| Y | Available to everyone |
| 5           | Click on "Blog posts" | Directed to the blog post | Y | Available to everyone|
| 6           | Click on "Next" button | User is taken to the next page of blog posts | Y |  Available to everyone |
| 7           | Click on "Previous" button | User is directed to the previous page | Y | Available to everyone |
| About        |                        |                  |      |             |
| 1           | Click on the "Home" button | To be directed to the home page | Y | Available to everyone |
| 2           | Click on "About" button | Directed to the about page | Y | Available to everyone |
| 3           | Click on "Register" button | Directed to the register page| Y | Available to everyone|
| 4           | Click on "Login" button | Directed to the login page| Y | Available to everyone |
| Register        |                        |                  |      |             |
| 1           | Click on the "Home" button | To be directed to the home page | Y | Available to everyone |
| 2           | Click on "About" button | Directed to the about page | Y | Available to everyone |
| 3           | Click on "Register" button | Directed to the register page| Y | Available to everyone|
| 4           | Click on "Login" button | Directed to the login page| Y | Available to everyone |
| 5           | Click on "Sign up"  | Directed to the home page if user has filled in the form to create profile. Else "please fill in this field" pops up| Y | Available to everyone |
| 4           | Click on "Login" button | Directed to the login page| Y | Available to everyone |
| 5           | Enter valid email | Field will only accept email address format | Y |          |
| 6           | Enter valid username | Allows users to choose their username| Y |          |
| 7          | Enter valid password | Field will only accept secure passwords | Y |          |
| 8          | Enter valid password confirmation | Field will only accept the same password from the previous field | Y |          |
| Log In      |                        |                  |      |             |
| 1           | Click on Sign in button | Redirection to home page if user has filled in the sign in form, else 'please fill in this field' message appears | Y |          |
| 2           | Enter valid username | Allows users type their username to sign in| Y |          |
| 3          | Enter valid password | Field will only accept users secure passwords | Y |          |
| Edit Profile     |                        |                  |      |             |
| 1           | Click on "username" | Allows users to change their username| Y |          |
| 2           | Click on "email address" | Allows users to change their email address| Y |          |
| 3           | Click on "first name" | Allows users to change their first name| Y |          |
| 4           | Click on "last name" | Allows users to change their last name| Y |          |
| 5           | Click on "password" | Users are directed to the change password page| Y |          |
| 6           | Click on "update" | new infomation added will be updated and directed to the home page | Y |          |
| Change password     |                        |                  |      |             |
| 1           | Click on "old password" | Allows users to type their old password| Y |          |
| 2           | Click on "new password1" | Field will only accept secure passwords| Y |          |
| 3          | Click on "new password2" | Field will only accept the same password from the previous field | Y |          |
| Log out    |                        |                  |      |             |
| 1           | Click on "sign out" | User  is logged out and redirected to the home screen | Y |          |
| Blog Post    |                        |                  |      |             |
|    1        | click on "Submit" button  | Logged in user can submit a comment, comment can only be submitted if text box has text inside, otherwise "please fill in this field" message appears | Y |    Only logged in userscan submit comments      |
| 2           | Click on "delete" button | User can delete their comment | Y |     only signed in user and owner of the comment may delete their comment     |
| 3           | Click on "edit" button | User can edit their comment | Y |     only signed in user and owner of the comment may edit their comment     |
| 4           | Click on "like" button | User can like other users comments comment | Y |     The like functionality is only avaliable to users who are logged in. The users can only like other users comment and not their own    |



## Testing User Story

| First Time Visitor Goals | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a First Time Visitor, I want to be able to register my account, so that I can learn the benefits of the app as a user.| Welcome text on the top of the homepage explaining the main purpose of the website and describing the the services offered | <img width="1423" alt="register page" src="https://github.com/user-attachments/assets/eac51132-c22b-4dd4-8a3f-30d575e239ac"> |
| As a First Time Visitor, I want to be able to easily navigate through the app, so that I can find the content. | The website has a navbar helping users easily naviagte their way through the site to areas thet want to be able top access. | <img width="1427" alt="navbar" src="https://github.com/user-attachments/assets/b58b651f-7314-4331-be9c-4bc29b285631">|
| As a First Time Visitor, I want to be able to find the app useful, so that it encourages me to return to the app.| The website cover benefits of becoming a member  | go to features section in the [README.md](README.md)|


| Frequent Visitor Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a Frequent User, I want to be able to log in to my account, so that I can have a personal account. | Log in from the Login page | <img width="1424" alt="log in page" src="https://github.com/user-attachments/assets/494087de-59b7-481d-95d4-04310c3d40ce">|
| As a Frequent User, I want to be able to easily log in and log out, so that I can access my personal account with ease.| Log out from the Logout page|<img width="1432" alt="logout page" src="https://github.com/user-attachments/assets/19706946-7fc5-4cdb-8f39-5ddc28d2238b">|
| As a Frequent User, I can be able to change my password, so that I can keep my account safe in case my password becomes public.| link on edit profile page to change password page | <img width="1426" alt="change password page" src="https://github.com/user-attachments/assets/43527887-8f1b-4b66-8805-22ae64dfd0c3">|
| As a frequent user, i want to be able to edit my profile.| Avaliable on edit profile page|![edit profile page](https://github.com/user-attachments/assets/04524e46-48a7-44d7-9382-77f0301a494f)|
| As a frequent user, i want to be able to comment on blog posts.| After creating a profile, comments can be made on blog posts.|<img width="441" alt="leave a comment" src="https://github.com/user-attachments/assets/ba675e9f-75b4-4a12-b88f-d0abbe0ca1d1">|
|As a frequent user, i want to be able to view comments made on a blog post.| All comments avaliable to view on any blog post|<img width="920" alt="comments logged out" src="https://github.com/user-attachments/assets/85c267e1-f1df-4e90-9b7d-7fb287e948af">|
| As a frequent user, i want to be able to modify or delete my comments.| Next to the comment there is an edit or delete button|<img width="897" alt="comments logged in" src="https://github.com/user-attachments/assets/8420dc1d-5de9-4a65-9955-c3c7c421055d">|
| As a frequent user, i want to be able to like comments on blog posts.| next to comments there is a like button|<img width="345" alt="like comment" src="https://github.com/user-attachments/assets/d7011334-75f8-4977-84de-bad529f35755">|


## Bugs

- During development, a bug was found when refreshing the page after posting a comment would cause the comment to duplicate. This was caused when the page was refreshed a POST request was being made rather than a GET request. This bug has now been resolved 
<img width="495" alt="duplication bug" src="https://github.com/user-attachments/assets/c77cf7d1-be23-4add-abb8-5afd72413861">
<img width="452" alt="refresh  bug" src="https://github.com/user-attachments/assets/6ebb02d8-c94b-4adf-a1ec-0425904fe25a">

- During development, i was having issues with formatting on vs code which was causing errors. This was resolved by saving without formatting


![before format](https://github.com/user-attachments/assets/8365e036-6f30-4fe7-99f7-9758ef72c8ba)
![formating error](https://github.com/user-attachments/assets/c515fa2f-2c57-4123-a7fe-eb9d670c6d14)


### Unit Tests

The application includes a suite of unit tests to ensure the functionality of its components.  Test file can be found in the app folders.
![blog test folders](https://github.com/user-attachments/assets/096aa998-ae4d-46c8-84be-38ccff15b67e)

![about test folders](https://github.com/user-attachments/assets/ccfb266d-d56d-46de-8673-b271d8f50e75)

To run the unit tests locally, use the following command: `python3 manage.py test`


- While running tests, no errors were found.
  ![7 tests ](https://github.com/user-attachments/assets/57f81a17-7983-45ae-84c5-77f82521c742)



- The code used to carry out the tests are as follows:
- ![blog test_views](https://github.com/user-attachments/assets/9d8d895c-9eb1-43af-a28c-0597515b6ce3)
- ![test_views](https://github.com/user-attachments/assets/b1a89f1e-6c03-4f57-9d15-c804c29cc1b3)
- ![test_forms](https://github.com/user-attachments/assets/6b97b7f2-1998-4622-b57c-7fa496741d50)

