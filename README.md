# Regression_project
# Project description with goals:
* This is a notebook where I analyze drivers of the property tax assessed values of single family properties that had a transaction during 2017 within the zillow dataset from MySQL. Using the data science pipeline, I grab the data, prepare it, explore it, visualize it, train models on it, and use statistical testing in order to answer questions about the data.


# Initial hypotheses and/or questions I have of the data, ideas:
* The main question I'm asking of the data is 'What are the main drivers of the property tax assessed values of single family properties that had a transaction during 2017?' and subsequently 'What can I recommend on what works or doesn't work in predicting these homes' values?'
* More specifically, my initial hypothesis is that the area of the house and county are the biggest drivers in tax value, because bigger houses cost more and prices of homes vary from county to county.

# Data Dictionary:
|Feature|Dtype, Description|
|:--------|:-----------|
|bedrooms|	int64, Number of bedrooms in the house|
|bathrooms|	float64, Number of bathrooms in the house|
|area|	int64, Area of house in square feet|
|taxvalue|	int64, Property tax assessed values of single family properties that had a transaction during 2017|
|yearbuilt|	int64, Year the house was built|
|taxamount|	float64, Tax amount on house|
|county|	object, County (LA, Orange, Ventura)|

# Project planning:
* Aquire data from MySQL
 
* Prepare data
  * Using my function from prepare, I renamed the columns and droped null values. Additionally I changed datatypes for appropriate columns and renamed fips to actual county names and encoded county.
 
* Explore data in order to find the drivers of the property tax assessed values of single family properties that had a transaction during 2017
   * Answer the following initial questions
       * What are the biggest drivers of higher tax value? 
       * Why do some properties have a much higher value than others when they are located so close to each other?
       * Why are some properties valued so differently from others when they have nearly the same physical attributes but only differ in location?
       * Is having 1 bathroom worse for property value than having 2 bedrooms?
      
* Develop a model to predict the property tax assessed values of single family properties that had a transaction during 2017
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on RMSE and r2 scores
   * Evaluate the best model on test data


# Instructions or an explanation of how someone else can reproduce my project and findings (What would someone need to be able to recreate my project on their own?):
* In order to recreate this project, another user would need similar acquire and prepare files, and a MySQL account to log in, with the credentials in your acquire file.


# Key findings, recommendations, and takeaways from my project:
## My main takeaway: I recommend that we predict the value of single family properties that cost less than $750k with our polynomial regression model using area, number of bathrooms, and county.  
