# masconsulting-test-project
Hello everyone, if you get to this point whether you are technical examiner from MAS Global or you are just curios to see several django components interacting in one single project.

For this repository I will be using the following:

#### Language and framework
* Python 3.7
* Django 3.1.7

#### Data Layer
* sqlite3

#### Security
I will also implement some basic security to consume the services with an api key / user pwd


#### The final products for this repo will be:
* A data layer
* An API with two web services, one to consume the MAS Global Consulting API, and another to query the model
* A basic web page for querying employee data

So as you can see I will be showing the MVC model in its full glory with the DJANGO framework.

PD: Since this is a showcase repo, I will be using the master branch for absolutely everything so don't judge me ;)

#### Additional information
* For demonstration purposes I am attaching the sqlite db in the project with some configurations and examples, the configurations include users, passwords and API keys to use the API
* The admin web portal is enabled, you can check out what is going on there with user: admin pwd: 6~A3qx459Vmc?CS%
* API is documented with swagger, you can check it out in the root url, I mean if you are using port 80 you can just checkout the http://localhost
* I am adding the postman collection to test the API in the root of the project
* I set up the requirements.txt file so you can install the required libraries to run the project


#### URLs for the test project
I will assume you will use the port 80 to run the project, if not just add the port to the following URLs

* Swagger info: https://localhost/
* Django admin: https://localhost/admin/
* Web page: http://localhost/webapp/employee/search_employee/
* Web services: http://localhost/api/v1/employees/employee (better to check out the POSTMAN collection I add here)