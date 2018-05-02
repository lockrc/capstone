# Final Technical Report

#### REI Dashboard Project
#### RJ Lock
#### May 6, 2018
## Abstract
Brief 200-300 word description of project objectives, methods and results.



## Keywords
Python, Renewable Energy, Solar Thermal, grafana, Photovoltaic, csv

## Table of Contents and Lists of Figures and Tables
TOC should list sections, titles up to second level headings with hyperlinks to subsequent sections
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

This project was created to move the data from the Renewable Energy Initiative at Appalachian State University to a new dashboard. The Renewable Energy Initiative (REI) currently pays approximately $14,000 per year to a company to host a dashboard that graphs all of their renewable energy project data. They are not happy with their current soulution because their current solution does not allow them any ability to modify the dashboards in any way. Any changes that they want made to the dashboards they need to call and have the company make the changes and this can take up to a week. This solution does not meet their needs very well and costs them more than 10% of their annual operating budget to continue using the dashboard. This soultion is not optimal and so is being replaced by the dashboard hosted on campus and using the grafana graphing software.

At this time REI has 7 projects with ongoing data requirements. There are also many projects that are in the process of being created. This soulution allows them to more easily add new systems and add them to their own dashboard rather than having to work through a company. This also allows them to direcly look at their data with transparency and understand how the data is being processed. With their current solution their is processing in the background and that does not allow for them to understand if their data is even completely correct because they do not know how the company is processing their data before it shows up on the dashboard.

This solution allows for REI to easily add new systems and to have authority over how their data is processed. This also allows them complete autonomy in the ability to edit and update their dashboards as they please. They also wished for more granularity in their data because their current solution only allows for 1 hour increments and does not automatically update all of the graphs.

There are many graphing solutions out there but grafana provides a perfect one because it is an out of the box soultion that handles the web portion so that REI can simply add new pages whenever they want without having to do any web programming.

My solution immediately handles the problems that REI has with their current soultion. It also provides a immediate benefit of cost savings.

## Design Development and Test 
(800-1200 words)
This section describes your design and test approach. Subsections should include:

### Design 
* Libraries and Python version
   * Python 3.6 [1]
   * pysftp [2]
   * mysql.connector [3]
   * pytz [4]
   * untangle [5]
   * requests [6]
   
Describe system components (e.g. software modules/components, libraries, etc.), interfaces, and operations. Use figures to illustrate your description, for example: photos, block diagrams, class diagrams, state diagrams, flow charts, tables, etc.

### Development
Before each step in the process I created little test files to learn how each library worked and make sure that I could get it working in isolation before adapting it to my project.

Describe how system was developed (for example, order of subsystem development and how risks were addressed early)

Development started with everything being located on my machine. I began by getting the grafana server and MYSQL server running on my machine. After that I moved on to get static files from the current dashboard and wrote a file to upload them. That file is importScript.py. After that I moved on to pulling files from a file server located on campus and pulled all of the csv files. I began by processing these files for just one system Library Circle. Once I had that working I moved on to the other systems first the Broyhill windturbine. After I got the windturbine operating correctly I moved to process the Solar Thermal systems. I started with Summit and once it was functional I used that code to process all of the Solar Thermal Systems.

I next moved to process the legends photovoltaic system. This system is managed by a company called enphase. All of the data is sent to enphases servers and has to be retrieved through their API. The API used web calls to return the information in JSON format. I used requests to pull the data and the python json library to process the json before inserting it into the database.

The mountain array at raley traffic circle is the system with the most complications. It is a site hosted on appalachians network that is a live representaiton of the data. It has 4 catagories for which it holds the data minute, hour, day, month. The problem comes that we want data for 15 minute intervals. This means the minutes have to be added up and posted. This process took longer than expected to get correct. It eventually ended up being a sepereate file that wakes up every minute to accumulate the data and post it when it is a 15 minute interval.

### Test
Describe your test approach (what was tested, how tested, what was not tested). You should organize this by feature (as you did for the System Features assignment).

As a guide to the level of detail, someone with your level of experience should be able to substantially reproduce your work from the descriptions in this section along with Introduction section.

Testing was done manually for my project. Each new system that got added had to be compared to the existing dashboard as well as the csv files to make sure that they matched. The comparison to the old dashboard was not an exact comparison because the timeframes were different (1 hour increments for old dashboard, 15 minute for new). The csv files matched exactly what was in the database.

## Results 
(800-1200 words)

Actual results of project. Describe how well you met your objectives, feature by feature. A table of results will help to summarize this.
This section describes final system in terms of features completed and actual performance of the system under test.
Include discussion of problems encountered, accuracy of estimates
Use figures and diagrams whenever possible

The objectives were very close to being met. The only thing that was not completed was the ability to pull live data.

## Conclusions and Future Work 
(400-800 words)

Briefly summarize problem, approach and results
Describe your conclusions and "lessons learned" regarding the results
Describe utility of results
Suggest areas for further study and/or development

This project is mostly complete there are still a few pieces left to complete. There is a request for live data as well as the ability to have people select any data that they want from each system.

## References
Provide references in standard ACM format (numbers in text correspond to numbered references here).
List all references to code used as part of your system (libraries, etc.)

[1] https://www.python.org/
[2] https://pysftp.readthedocs.io/en/release_0.2.9/
[3] https://dev.mysql.com/downloads/connector/python/
[4] http://pytz.sourceforge.net/
[5] https://github.com/stchris/untangle
[6] http://docs.python-requests.org/en/master/
