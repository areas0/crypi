## Server

### 1. Admin creation
You need an administrator, this will be the account that can start and end the vote. The administrator cannot vote however.

run `python manage.py createuser` and enter your credentials in the successive prompts.

## 2. Server

`python manage.py runserver` to run the server.
Once the server is launched, a website is accessible on `localhost:8000` on which you can register new users, then log in as using the admin account you created.
Go the `start` page and start the vote.
The users can then connect and vote.
When you want to stop the count and compute the results, go to the `result` page as admin and click the button to get the results