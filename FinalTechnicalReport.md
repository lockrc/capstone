# Final Technical Report

#### REI Dashboard Project by: RJ Lock
#### May 6, 2018
## Abstract
Brief 200-300 word description of project objectives, methods and results.

This project is designed to replace Appalachian State University's Renewable Energy Initiative (REI) dashboard that they use to display the generation by the renewables on campus. They currently pay $14,000 per year to a company and are still unhappy with the service they receive. They pay more than 10% of their budget on this dashboard and they are dissatisfied with the product. I created a new version with python scripts, a MYSQL database, and a Grafana server. My solution gives much of the functionality that they want from their dashboard. It gives more features that they wanted from their current dashboard and allows them to host it on Appalachian's campus for much cheaper than $14,000 per year.

## Keywords
Python, Renewable Energy, Solar Thermal, Grafana, Photovoltaic, csv, JSON, XML

## Table of Contents and Lists of Figures and Tables
* [Introduction and Project Overview](#introduction-and-project-overview)
* [Design Development and Test](#design-development-and-test)
  + [Design](#design)
  + [Development](#development)
  + [Test](#test)
* [Results](#results)
* [Conclusions and Future Work](#conclusions-and-future-work)
* [References](#references)

## Introduction and Project Overview 
(800-1200 words) 

This section should be written assuming your reader has zero knowledge of your work and its background. You must bring the reader from "zero" to a level where they can understand the main ideas and results of your work. (This should be derived primarily from your Final Project Description document)

Introduces the problem, objectives, and the users (or customers) of project results, context of problem and issues that affect solution choices
Describes relevant background information. May include any alternative solutions (are there existing solutions or similar systems? give references) in terms of strengths and weaknesses.
Describe value or benefits of your solution and results
Problem scope--problems addressed and not addressed
Figures and system diagrams where possible to illustrate problems and solutions.
Summary of features

This project was created to move the data from the Renewable Energy Initiative at Appalachian State University to a new dashboard. The Renewable Energy Initiative (REI) currently pays approximately $14,000 per year to a company to host a dashboard that graphs all of their renewable energy project data. They are not happy with their current solution because their current solution does not allow them any ability to modify the dashboards in any way. Any changes that they want made to the dashboards they need to call and have the company make the changes and this can take up to a week. This solution does not meet their needs very well and costs them more than 10% of their annual operating budget to continue using the dashboard. This solution is not optimal and so is being replaced by the dashboard hosted on campus and using the Grafana graphing software.

At this time REI has 7 projects with ongoing data requirements. There are also many projects that are in the process of being created. This solution allows them to more easily add new systems and add them to their own dashboard rather than having to work through a company. This also allows them to directly look at their data with transparency and understand how the data is being processed. With their current solution there is processing in the background and that does not allow for them to understand if their data is even completely correct because they do not know how the company is processing their data before it shows up on the dashboard.

This solution allows for REI to easily add new systems and to have authority over how their data is processed. This also allows them complete autonomy in the ability to edit and update their dashboards as they please. They also wished for more granularity in their data because their current solution only allows for 1-hour increments and does not automatically update all of the graphs.

There are many graphing solutions out there but Grafana provides a perfect one because it is an out of the box solution that handles the web portion so that REI can simply add new pages whenever they want without having to do any web programming.

My solution immediately handles the problems that REI has with their current solution. It also provides an immediate benefit of cost savings.

## Design Development and Test 
(800-1200 words)

### Design 
* Libraries and Python version
   * Python 3.6 [1]
   * pysftp [2]
   * mysql.connector [3]
   * pytz [4]
   * untangle [5]
   * requests [6]

This project is separated into 3 files: sftppull.py, processfiles.py, mamac.py.
  
sftppull.py - This is the main script that handles pulling the csv files and processing them all and inserting them into the database.
  
processfiles.py - This file simply contains the methods to process all of the csv files and to process the enphase system.
  
mamac.py - This file processes the Mamac system's XML and aggregates the data over each 15 minute period.

### Development
Before each step in the process I created little test files to learn how each library worked and make sure that I could get it working in isolation before adapting it to my project.

Development started with everything being located on my machine. I began by getting the grafana server and MYSQL server running on my machine. After that I moved on to get static files from the current dashboard and wrote a file to upload them. That file is importScript.py. After that, I moved on to pulling files from a file server located on campus and pulled all of the csv files. I began by processing these files for just one system Library Circle. Once I had that working I moved on to the other systems first the Broyhill wind turbine. After I got the wind turbine operating correctly, I moved to process the Solar Thermal systems. I started with Summit and once it was functional I used that code to process all of the Solar Thermal Systems.

I next moved to process the legends photovoltaic system. This system is managed by a company called enphase. All of the data is sent to enphases servers and has to be retrieved through their API. The API used web calls to return the information in JSON format. I used requests to pull the data and the python JSON library to process the JSON before inserting it into the database.

The Mountain Array at Raley Traffic Circle is the system with the most complications. It is a site hosted on Appalachian State's network that is a live representation of the data. It has 4 catagories for which it holds the data: minute, hour, day, month. The problem comes that we want data for 15-minute intervals. This means the minutes have to be added up and posted. This process took longer than expected to get correct. It eventually ended up being a sepereate file that wakes up every minute to accumulate the data and post it when it is a 15-minute interval.

### Test

Testing was done manually for my project. Each new system that got added had to be compared to the existing dashboard as well as the csv files to make sure that they matched. The comparison to the old dashboard was not an exact comparison because the timeframes were different (1-hour increments for old dashboard, 15 minute for new). The csv files matched exactly what was in the database.

## Results
(800-1200 words)

Actual results of project. Describe how well you met your objectives, feature by feature. A table of results will help to summarize this.
This section describes final system in terms of features completed and actual performance of the system under test.
Include discussion of problems encountered, accuracy of estimates
Use figures and diagrams whenever possible

|Feature|Status|
|------|------|
|Pulling csv files|Success|
|Processing Library Circle|Success|
|Processing Wind|Success|
|Processing Solar Thermal|Mostly Successful|
|Moving Everything to Server|Success|
|Processing Mamac|Success|
|Processing Enphase|Incomplete|
|Live Data|Incomplete|
|Backfill Data|Incomplete|
|Other Graphing Solutions|Incomplete|
|Download|Incomplete|

### Overall
The overall objectives were very close to being met. There were multiple "strech" goals that were not achieved. The stability needs to be worked on because it only seems to run for about a week at a time before it crashes. I have been unable to narrow down the root cause despite outputting to a file.

### Pulling csv files from file server
Successful at pulling the csv files from the file server.

### Processing Library Circle
Library Circle is the only photovoltaic system that is on the Obvius data server [9]. The csv files get processed correctly in processfiles.py and 

### Processing Wind
The Broyhill wind turbine is also on the Obvius data server and has csv files that hold the many data points kept on the wind turbine [9].

### Process Solar Thermal
There are 4 solar thermal systems on Appalachian's Campus. These systems all have the same csv layout so they all use the same format to be inserted into the database. The solar thermal is not completely correct because the method that I chose to calculate the production is not the preferred method, but I did not find that out until the end. It is very close but not exactly the same.

### Moving to server
Everything has been moved over to the server and is now located at http://asurei-data.appstate.edu.

### Processing Mamac
The mamac system gives the production in minute increments and is aggregated to be on a 15 minute scale. This system is for the Mountain Array near Raley Traffic Circle. The data is aggregated and processed in mamac.py.

### Processing Enphase
The enphase system is the system that monitors legends photovoltaic system. This system provides a JSON output that gives the production information for the last hour. It is processed by processfiles.py. The data put into the database for this is not correct I have not finished setting up the processing for this data.

### Live Data
The live data did not make it into the final product. I ran out of time to complete this feature. It was really more of a stretch goal than a goal I expected to be able to reach.

### Backfill Data
The data only goes back as far as the csv's were available and the full back data was never added to the database. The legends and mountain array don't have back data to add.

### Other Graphing Solution
This goal was created because I expected that I would complete my project well before the end of the semester and would need to add more to the project. The idea was that I would use other services like plot.ly to create multiple versions of the dashboards to give multiple options.

### Download
The ability to download selected data is something that was requested late in the development process and was the least likely feature to be completed because of the late addition and the other features left to be completed.

## Conclusions and Future Work
(400-800 words)

Briefly summarize problem, approach and results
Describe your conclusions and "lessons learned" regarding the results
Describe utility of results
Suggest areas for further study and/or development

### Conclusions
The project is mostly done. The project will need more work to more substantially meet the needs that REI has. However, this project is a strong start and can easily be continued for a complete solution. The basic setup allows for expansion by a future developer and allows for easy updates should they need to add systems.

### Future work
The crashing issue will need to be solved. It is likely an error with reaching either of the websites or the database. The future work will also need to include the backfill of data and implementing live data and the ability to download the data.

## References
Provide references in standard ACM format (numbers in text correspond to numbered references here).
List all references to code used as part of your system (libraries, etc.)

[1] https://www.python.org/ <br>
[2] https://pysftp.readthedocs.io/en/release_0.2.9/ <br>
[3] https://dev.mysql.com/downloads/connector/python/ <br>
[4] http://pytz.sourceforge.net/ <br>
[5] https://github.com/stchris/untangle <br>
[6] http://docs.python-requests.org/en/master/ <br>
[7] http://asurei-data.appstate.edu <br>
[8] https://buildingos.com/s/appstate/storyboard <br>
[9] http://www.obvius.com/
