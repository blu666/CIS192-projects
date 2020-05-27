### CIS192 Homework 6
### Quikker: An idea space for Quakers

Group:
1. Yijie Lu (Pennkey: luyijie)
2. Yuzhou Lin (Pennkey: yzlin)

Description: Welcome to Quikker--the Quakers' version of Twitter! Quikker includes lots of functionalities from Twitter: log in, sign up, log out, hashtag, like, unlike, delete, access profile, see those who have liked you... Enjoy your quaking time!!!


## Instruction on how to run Quikker in the terminal:

cd twitter
pip3 install django
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver


The (local) url to the Quikker webpage: http://127.0.0.1:8000/

## Routes
The first webpage is the splash page. Click the "Click here to Log In Or Sign Up", and you will enter the accounts page. 

Sign up: sign up by typing your own username, email address, and password

Log In: log in with your registered username and password; if your password/username is wrong or not registered, you will be redirected to the accounts page to enter your information again

Qukkier (http://127.0.0.1:8000/): return to the homepage of your account

Log Out (http://127.0.0.1:8000/logout): log out your account and return to the accounts page

Quake (square button): Post your quake written on the left side of the "Quake"" button ("Write your thoughts down")

Delete (http://127.0.0.1:8000/delete?id=): delete the quake if you are the quake's author

@ Somebody (http://127.0.0.1:8000/profile?user=): access the profile page of the user/quake's author, and you can see all the quakes written by this user/author

Like, Unlike(http://127.0.0.1:8000/like?id=, http://127.0.0.1:8000/unlike?id=): click "Like" for the quake and its number of Likes will increase by 1; click "Unlike" for the quake and its number of Likes will decrease by 1

Hashtags(http://127.0.0.1:8000/hashtag?name=): show only the quakes with the given hashtag message


## Extra Credit Functionality:
"See Who Liked This Quake" (http://127.0.0.1:8000/view_like?id=):

If you are a quake's author, you can check who have liked the quake by clicking "See Who Liked This Quake". Clicking the button will take your to a new webpage that displays the original quake and a list of users who have liked that quake.





