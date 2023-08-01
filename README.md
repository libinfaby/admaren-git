# admaren-git
### A text saving and retrieval web app using Django, Django REST Framework and Simple JWT.
---
## Running the project
(database is not deleted and .gitignore is not included for easier testing purposes)
- Clone the repository.
- Install `pipenv`. Alternatively, `pyenv`, `venv` etc. can also be used.
- Run `pipenv shell` inside the directory. This will create a virtual environment named `admaren-git`.
- Install packages mentioned inside the `Pipfile`.
- Test django by running `python manage.py runserver` from the root directory.
- Test the urls and views. Some views require authentication. The `.../api/token/` view will create a new access token, if given the username and password, which can be used to authenticate the user.
- For testing purposes, there is a python client in `py_client/snippet_overview.py`, which can be used to test the `SnippetOverviewAPIView`. A username and password is required to generate the token. The database already has a user with `username: admin, password: admin` or you can create a new user through the admin panel or another admin user by running `python manage.py createsuperuser` and giving the necessary credentials.
- Most of the views require token authentication. Tools like cURL or Postman can be used to resolve the URL's for protected views. Example:
`curl \
  -H "Authorization: Bearer {access-token}" \
  http://localhost:8000/api/{some-protected-view}/`.
