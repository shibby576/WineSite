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

Live final solution: https://winesite.herokuapp.com/

## Steps
### Train model and determine inputs
I primary drink red wine, so I used the red wine quality data set from UCI. Since all of the values are continuous, I decided to use a simple linear regression as my model. The original data set has 11 features to predict quality, but I ended up only including Alcohol and Sulfate level as inputs to my model. This is partially because these were the only features that had significant impact on model performance but also because these are two values that can be determined/estimated by looking at the bottle in a store. I can see how this ability to have useful inputs dictates the viability of more complicated models. 

Another decision I made during training that had product impacts was the decision to scale my training data. I used MinMaxScaler to scale all training data to values between 0-1, which as a side effect, meant that the model must take values from 0-1 as an input. This became a hurdle when building the UI and giving users a logical way to input alcohol and sulfate levels.

Lastly, the packaging of the model was actually quite easy. I used the python pickle module to serialize my model into a pkl file, which I then included and called in my application.

Overall, im not happy with the performance of the model, which really takes away from the value of the product, however "good enough" is okay to me in this context as there are other more imporant learning objectives for this project. 

Full analysis & Model here: https://github.com/shibby576/WineSite/blob/main/analysis/analysis_notebook.ipynb

### Design product
With the primary use case being to identify quality while in store, I knew that I needed to take a mobile first approach. This meant optimizing the layout to work well on mobile, but also making sure that the input elements are easy to use on mobile. I used a bootstrap sign up form example and modified it to fit my needs. 

One interesting design issue here was identifying how the values for alcohol and sulfate level should be input. I ended up choosing to used defined values in a dropdown for several reasons:
<br>1-Sulfate levels are not defined on bottles. This means that a user will need to look at the wine or read the label to estimate the amount of sulfates in it. This lent itself well to the idea of just defining ranges like high, medium, and low that the user can select.
<br>2-Because the model only takes scaled data 0-1, these input values are not logical to users. For example, how would a user know the 14% alcohol is really equivalent to .9 in our training data? So dropdowns were a useful workaround, which allowed the application to do this conversion for the user. 
<br>3-Drop downs are quick and easy on phones whereas sliders and number inputs can be a little more difficult. 
HTML file here: https://github.com/shibby576/WineSite/blob/main/templates/index.html

### Write the application
I used some basic flask tutorials to figure this part out. The one addition that I made was the logic to take the prediction value from the model, which is the scaled decimal value, and scale it up into a round number between 0 and 10 as it originally was in the data. To come up with this formula, I had to compare the distribution of scaled training data values to the distribution of the original values, then put some basic logic in app.py to apply it. 
app code: https://github.com/shibby576/WineSite/blob/main/app.py

### Deploy
I might have had the most trouble here. I spun my wheels for a few hours trying to make this work on GCP, but then decided to try Heroku as it seemed more straightforward. While i was able to get my application to deploy more easily, it consistently died when running. It turns out the fine print about project structure, dependencies, and for heroku the procfile really matter, giving me a new appreciation for the logistical hurdles engineers deal with. 
Live final solution: https://winesite.herokuapp.com/

## Final summary
This project gave me a great intro into the unique challenges of building a model that end users will interact with and also made me more confident in building web applications. There is a lot wrong with this project, including a model accuracy and some usability issues, but overall it helped me achieve many of my learning objectives. 
