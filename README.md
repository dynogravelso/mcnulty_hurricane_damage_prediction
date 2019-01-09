## Project McNulty

![](mcnulty.jpg)

#### Objective

Forecasting the degree of hurricane damage is important to determine the appropriate response in order to mitigate damage and the loss of lives. A model used for screening weather systems would be impactful as support for making early decisions when weather systems first appear in the ocean.

#### Results

* Created a random forest classification model capable of predicting the severity of hurricane damage based on data from NOAA to predict damage based on location, wind speed and other simple features (F2 Score = 0.48)
* Created flask app for easy access to the model. This tool can be used as a very quick initial screening tool to assess the approximate severity of the damage. The prediction is calculated instantaneously and can be used by the general public and weather observatories alike.

[Project McNulty Final Slides](mcnulty_hurricane.pdf)

##### Project prompt is as follows:

#### Back story:

Using data from the web (API or scraped) or one of the optional supplied data sets (possibly in conjunction with your own data), create models using supervised learning techniques. Extend your findings with a flask website and/or OPTIONAL D3 visualization.

Note you can work as a 'group' (with other folks working on the same data source as you) for 
brainstorming, design, additional data, etc. However, the final projects will be individual.


#### Data:

 * **acquisition**: download, api's, scraping, etc.
 * **storage**: PostgreSQL
 * **example sources**:  (see [sql_data_sets](sql_data_sets.md) for descriptions and links to data.)
  - NYC Transportation
  - Traffic Fatalities
  - US Health Insurance Marketplace
  - Militarized Interstate Disputes
  - Sports, Sports, and More Sports!
  - The Simpson's
  - Climate Change
  - Python StackOverflow Questions 


#### Required Skills & Tools

* supervised learning
* SQL
* flask

#### Deliverable/communication:

  * organized project repository
  * slide presentation
  * visual and oral communication in presentations
  * write-up of process and results

#### Design:

   * iterative design process
   * "MVP"s and building outward

#### More information:

Data sources for this project are all about options. We can choose from a number of [pre-selected](sql_data_sets.md) data sets. We can also use our own data (either scraped from the web or pulled from api's) or supplement the pre-selected data with some of our own. Either way, we will be honing our database skills by storing data in PostgreSQL and doing some of our analysis there.[^1]

[^1]: If the project does not have a significant SQL component, then additional (intermediate and advanced) [SQL challenges](../../challenges/challenges_questions/09-sql) must be completed.

We'll also learn about many supervised learning methods that can be used to predict outcomes for our projects. And we can showcase those results with a flask website or D3 visualization.
