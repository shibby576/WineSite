# Learn how to deploy a ML model to production

Live site: https://winesite.herokuapp.com/

Most of my personal experience with building and training machine learning models has been in an exploratory sense, building models in Jupyter notebooks, which were never really useful to end users. I wanted to understand how to take this more theoretical experience and apply it in a practical way, understanding the requirements and challenges of building a full stack application that leverages machine learning. To do this, I set out to solve a personal problem with a simple web application that leverages a basic ML model.

In addition, while I had developed static web pages in the past, I had never built/deployed a website in a full stack capacity, so this project also pushed me to learn the fundamentals of web development.

Learning objectives:
<br>-How to deploy a basic ML model in production 
<br>-How to deploy a website
<br>-Build a basic web app with python and html/css

Problem: As a novice wine enthusiast, I often spend an awkward amount of time wandering around my local wine shops trying to find the best bottle of wine in my price range. The issue is that for any given variety and price range there are typically a few wines that meet the criteria but it's difficult for me to tell which one might be "better". What if there were a tool to tell me which might be better in a more objective way?

Solution: Something that could predict the quality of wine based on attributes I can identify by looking at the bottle in store. 

Features: A web application that takes input about wine, in this case Alcohol contents and sulfate level, and outputs predicted wine quality.

Technology, products & methods used:
<br>-Data analysis in Python (Pandas, numpy, Matplotlib) 
<br>-Model training and testing with Python (Scikit-learn)
<br>-Python for application code (Flask)
<br>-HTML/CSS for front end (Bootstrap)
<br>-Heroku for app hosting

Data analysis & Model: https://github.com/shibby576/WineSite/blob/main/analysis/analysis_notebook.ipynb
Live final solution: https://winesite.herokuapp.com/

## Steps
### Train model and determine inputs

### Design product

### Write application

### Deploy

## Lessons learned
### Model usability was impacted by data scaling
To achieve more accurate predictions, I used MinMaxScaler to scale all training data to values between 0-1. A side effect of this is that to make a prediction, the model must take values from 0-1 as an input. This formatting is quite different than the standard X% Alcohol content that most people are used to, so i had to 
