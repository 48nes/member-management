# Member Management
 A simple team member management app to allow users to view, edit, add, and delete team members.

## Steps to Run the Project

1. After downloading the repo, run `./manage.py runserver` in the same directory
2. The site should be available on the development server, typically at http://127.0.0.1:8000/

## Steps to Run Tests

Tests were written using Django's test library. All tests can be run using `./manage.py test`.

### To-Do

- A login feature would be the next step
- Implementing an authentication layer to disallow non-admins to edit member pages
- Migration to either MySQL or PostgreSQL to support larger databases
- Cleanup 404 error page
