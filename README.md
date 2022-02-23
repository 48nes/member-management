# Member Management
 A simple team member management app to allow users to view, edit, add, and delete team members.

## Steps to Run the Project

1. After downloading the repo, run `./manage.py runserver` in the same directory
2. The site should be available on the development server, typically at http://127.0.0.1:8000/

## Steps to Run Tests

Tests were written using Django's test library. All tests can be run using `./manage.py test`.

I have also tested directly on the test server to ensure that the web app is functional, although I have wiped the databases.

### To-Do

- Cleaning of phone numbers to validate number while still retaining support for international numbers
- A login feature would be the next step
- Implementing an authentication layer to disallow non-admins to edit member pages
- Migration to either MySQL or PostgreSQL to support larger databases
- Cleanup 404 error page

#### Testing

- Tests for deleting a member
- Test to verify edits change the database