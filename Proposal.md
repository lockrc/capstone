## Metadata section
Name: REI Dashboard <br>
Developer: RJ Lock

## Project Overview
### Description: 
REI pays $14,000 per year to a company called Lucid to produce a dashboard for them and they are still unhappy with the result. They want it to be customizable and the one that they are paying for is not customizable at all without calling the company and asking for them to change it.
### Outline:

#### Must Have:
*	Pull data from the two databases that REI uses to store their data
*	Store data in a common database that can then be accessed by the dashboard tool that is being used
*	Create a dashboard that meets the needs of the REI officials

#### Want to have:
*	Use current framework that was created to pull the data out of the databases
*	Take data and use multiple plotting services to give different options to REI for ways to display their data

### Users
The users would be the REI officials but would obviously have possible commercial application since they currently pay another company to handle the data combination and graphing. This could be applied to many other people who need data graphed. There is obviously a need since the current company is being paid $14000 dollars and are not meeting the relatively simple needs of the REI officials

## Similar Existing Work
The existing framework: https://github.com/stephen-bunn/neat <br>
I have the existing framework that was created last semester for pulling data from the two databases and making it available. The problem is that the documentation is lacking and it is very hard to decipher how the pieces are meant to work or how you are supposed to get data out. This is what I will start with looking at and trying to get working. If I cannot get it working then this would be what I would have to create for the first part of the project. After that I would need to extend the project to storing the data in another database and using that to create the dashboard.

## Previous Experience
I have experience with python which the scripting will be done in. I wrote scripts for a power company to write information to and from a database. My experience with the Blue Ridge music center project in my database class also gave me experience that will be helpful in working with the databases.

## Technology
I will use Python to write all my scripts to pull data out of the existing databases and put it into the new database. I will use Atom to write my code and use the existing linting plugin. I will use python’s existing unittest framework. I will use the package manager pip. I will write python scripts that use the unittest framework to automatically check that my tests pass, my code is formatted and that I do not have lint. I plan on using grafana to make the first dashboard and should I have extra time make dashboards using other tools such as plotly.

I will follow the specifications listed here: http://appstate-neat.readthedocs.io/en/latest/source/getting-started.html#end-users. These were the specifications that were provided by the creators of the framework that I will start by attempting to use.

## Risk Areas
*	I do not have any experience with the two databases that hold the data from all of REI’s sensors. Those two are Mongodb and Rethinkdb. I plan on reading up on the basic ways of interacting with those Databases and testing those commands on test databases. 
*	I also do not have experience with using the software grafana or plotly so I will need to create a test dataset and use those to plot the data.
*	I have never created a database before so I will need to read up on how to create a database using python and test that I can add data. I can get a .csv file and add it to the database since that will be necessary during the project anyway. I have also talked with Dr. Russell and he is willing to help me if I need assistance with figuring out the database.

