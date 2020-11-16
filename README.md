# QA Fundamental Project

**Gig Listings App** _By Isaac Lister_

## Resources

Website: http://35.246.80.16:5000/
Trello: https://trello.com/b/FYH0cnRN/agile-sprint-board
Risk Assessment: https://docs.google.com/spreadsheets/d/15WIGvHh8FQEDUEicGsjjrn0KgMcBp4hbD8GJF3MOx-U/edit?usp=sharing


## Contents

* Brief
    * [Building the Minimum Viable Product](#building-the-minimum-viable-product)
    * [Further Definition](#further-definition)
* [Architecture](#architecture)
    * [Models and Routes](#models-and-routes)
    * [Initial Relationship Schema](#initial-relationship-schema)
    * [Final Relationship Schema](#final-relationship-schema)
* [Risk Assessment](#risk-assessment)
* Design
    * [CI Pipeline](#ci-pipeline)
    * [Back End](#back-end)
    * [Front End](#front-end)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Errata Analysis](#errata-analysis)
* Testing
    * [Unit Testing](#unit-testing)
    * [Integration Testing](#integration-testing)
* [Branching](#branching)
* [Versioning](#versioning)

## Brief
### Building the Minimum Viable Product (MVP)

For this project, the MVP would be defined as a functional CRUD application with two models that have a relationship.

In order to achieve this, we can use a skeletal Entity-Relationship Diagram and declare a basic folder architecture.

![erd1][erd1]

In Fig.1, we evidence two tables, Bands and Venues. They share a many-to-many relationship- meaning, in real world context, that one band can appear at many venues, and one venue can have many bands perform at it.

### Further Definition

Exclusive to the project; where our MVP should be able to adhere to basic CRUD functionality- in this case, the ability to:

* Add a band to the database (satisfies Create)
* Return lists of bands and the venue they're gigging at (satisfies Read)
* Edit entries for gigs and update the database (satisfies Update)
* Delete entries for gigs and update the database (satisfies Delete)

### Architecture

We declare a simple architecture for the project:
![architect][architect]

The architecture permits that the app can be created and run from the top level; initialises database connections and stores its models and routes in the application folder; and holds its HTML templates to be returned within the routes in the templates folder.

A Trello board was configured to manage the project in best fit with an Agile methodology.

![trello][trello]

### Models and Routes

![basemodel][basemodel]

The problem is that v1.0.0 is not technically an MVP because band_name and genre are attributes of the same class. We have not yet created In order to model a functional relationship between two tables, we define the concept of a 'gig', which for this project is defined as:

_'A gig is one band performing at one venue.'_

In order for the project to meet all the Minimum Viable Product requirements, we must model a relationship between two tables. 

### Initial Relationship Schema

Initially, the project was to utilise an intermediate table; bands_venues, between bands and venues. However, to ensure the simple execution of the project and not to confuse myself, I have instead opted for just two tables, bands and venues, sharing a one-to-many relationship in the sense that one band can perform at many venues. For now, this project ignores the real-life situation that many bands could perform at many venues, and focuses on functionality within the constraints of the relationship I have chosen to model.

![erd2][erd2]

Ultimately, it was decided that basic functionality for the app required only a one-to-many relationship between the two tables Bands and Venues, such that one band can perform at many venues. With the venues to be selectable from a drop-down SelectField when creating a gig in the database, it is not necessary to use an intermediate table with back referencing. This led to the final relationship schema for the app, which was built using this SQL schema as its foundation.

### Final Relationship Schema

![erd3][erd3]

### Risk Assessment

A full risk assessment was designed and implemented prior to beginning to build the project.
The full assessment can be found at: https://docs.google.com/spreadsheets/d/15WIGvHh8FQEDUEicGsjjrn0KgMcBp4hbD8GJF3MOx-U/edit?usp=sharing

![risk][risk]

## Design

### CI Pipeline

Here is the CI Pipeline specific to this project.

![myci][myci]

Project tracking through Trello (see Resources) allows for a list of tasks as backlog to refer to.
These tasks are completed and pushed as code to the GitHub repository, managed with Git VCS.
The Git VCS triggers the Jenkins CI Server (this should be subsequently automated in the Execute shell, I have not done this)
Unit testing and integration testing can be performed, also by running Pytest in the shell.
Pytest feeds back coverage reports which can be emailed to developers. One such report is included in the Testing section.
Builds which pass the tests get added to an artifact repository in Jenkins, which can be staged for live.

Using a VCS controlled CI Pipeline makes changes easily trackable, and the feedback loop between clients and developers more transparent.






### Back End

The application back-end is built by Jenkins and run using a Gunicorn WSGI server through Jenkins' execute shell. Here's an example.

![shell][shell]

Here's an example of Gunicorn running the app on Jenkins.

![gunicorn][gunicorn]

### Front End

The front end of the application is a basic HTML frame which will require a more professional looking GUI in a future release.

![frontend1][frontend1]

Following the 'Add Gig' hyperlink takes you to a basic page to add a new gig and select a venue:

![frontend2][frontend2]

This will display the gig on the main page. Unfortunately there is no way to change the gig details such as entry fee or start time, but this should be included in a future version.

![frontend3][frontend3]

Following the Delete link clears the listing you have just entered.
Following the Update link presents with the following screen, where all changeable features of the listing can be modified:

![frontend4][frontend4]

...and the update will be reflected on index.html:

![frontend5][frontend5]

### Known Issues

There is no user login functionality. Whilst this reduces risk, it is also an important piece of functionality. A predetermined list of venues is not really useful for the functionality of the app. Neither is the fact that you cannot set what the gig time or the entry fee is. Otherwise, the application is fully functional, barring syntax errors and id conflicts at the programming stage.

### Future Improvements

A more professional and functional GUI
The ability to input what date the gig is on
The ability to set entry fees and gig times independent of venue selection.
The ability to register and login as a user
The ability to subscribe to favourite bands and venues
The ability to add pictures of the gig to the gig's Archive.

### Errata Analysis

Test-running the app the first time yielded an error in Jinja2, encountering an unknown tag error as band.band_name was declared in incorrect brackets in index.html.

On the second test iteration, I realised I hadn't declared any use of 'genre', where I had made it a field in models.py (class Bands), and as such SQLAlchemy threw an error, as a nullable=False field became null.
To fix this, I ensured that the /add route assigns a genre to the new_band and displays it in the list.

On the third test iteration, the app ran successfully, and the test bands and test genres display in 'id-descending' order.

While Unit Testing, I encountered a syntax error in a test class. There was an absent comma, this was fixed and the test ran successfully.

## Testing

### Unit Testing

![test][test]

Through writing unit tests in test_app.py, I was able to obtain an overall coverage of 82%. Unfortunately, an AssertionError when trying to test the /add route is keeping that percentage low, but I can't seem to solve it. In future, I would ensure that all routes are tested to ensure none of my tests fail.

The scope of the unit tests were to ascertain if all CRUD functionality was working.
Routes for add, update, read and delete were tested.
Testing the add route failed, due to an AssertionError, so i would want to fix this prior to release.

### Integration Testing

Integration testing was achieved with a test_int.py file, connecting to a test database, a chromedriver executable, and running integration tests by xpath for adding and updating a gig in the database. Unfortunately I don't know how to obtain a report for this, but the tests passed when running pytest.

Adding a user to the database by xpath was tested in integration.
To run the integration test, a separate Database URI and Secret Key is required to keep testing separate from production.
As there is an initialisation file and a test_int.py in the tests folder; the integration test can be run by running the command pytest from the terminal.


### Branching

For v1.0.0, once I had working code, a new branch was checked out to in Git called 101branch.
This enables updates to be made to the code without affecting a working version, to be merged later.
Iteratively, I do this for 10nbranch throughout building the project. The versioning for this process can be viewed below.

V1.0.1 pushed successfully to master, retained on branch 101branch.
V1.0.2 (not yet functional) pushed successfully to branch 102branch.
V1.0.3 pushed successfully to branch 103branch, and to master. App is fully functional.
V1.0.4 pushed successfully to branch 104branch. App is fully functional. Integration testing to complete on-branch before merging with master.

### Versioning

Although it would be best practice to merge and delete branches, for the purpose of this project I have left versions on individual branches under nomenclature 10nbranch where n dictates versioning, so that my repository's architecture evidences the evolution of my project.

v1.0.0 – adds test bands and genres to memory via routes. No update or delete methods. Not MVP.

V1.0.1 - added routes to update the name of the most recently added band, and delete the most recently added band from the database. Functional on first test. 

V1.0.2- added basic form functionality to enter a band, added test suite test_app.py with simple tests based on GET and POST requests (returning status code 200/405 from the request appropriately; etc. Pushed to master

v1.0.3- App runs through Jenkins with a Gunicorn command, has SelectField functionality to choose a venue.

V1.0.4- unit testing completed, HTML coverage report generated. 82% coverage. Integration testing completed, but unsure how to evidence this in report.

## Authors
Isaac Lister



[erd1]: https://imgur.com/72Z78v9.png
[architect]: https://i.imgur.com/97kaPBX.png
[basemodel]: https://i.imgur.com/h4uInpn.png
[erd2]: https://i.imgur.com/pknce7J.png
[erd3]: https://i.imgur.com/ZKmOaJ8.png
[frontend1]: https://i.imgur.com/1ynshAO.png
[frontend2]: https://i.imgur.com/6niJak1.png
[frontend3]: https://i.imgur.com/KWigCtB.png
[frontend4]: https://i.imgur.com/YhwzEMl.png
[frontend5]: https://i.imgur.com/EqByfAM.png
[gunicorn]: https://i.imgur.com/4Kv9Rpf.png
[shell]: https://i.imgur.com/iNZLIIM.png
[risk]: https://i.imgur.com/yNkv5VK.png
[test]: https://i.imgur.com/yxA33O4.png
[trello]: https://i.imgur.com/4Lzs2UY.png
[myci]: https://imgur.com/Sw84peN.png


