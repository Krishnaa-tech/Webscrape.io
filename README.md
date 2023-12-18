[![GitHub license](https://img.shields.io/github/license/Krishnaa-tech/Webscrape.io)](https://github.com/Krishnaa-tech/Webscrape.io/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/Krishnaa-tech/Webscrape.io.svg)](https://GitHub.com/Krishnaa-tech/Webscrape.io/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/Krishnaa-tech/Webscrape.io.svg)](https://GitHub.com/Krishnaa-tech/Webscrape.io/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Krishnaa-tech/Webscrape.io.svg)](https://GitHub.com/Krishnaa-tech/Webscrape.io/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub watchers](https://img.shields.io/github/watchers/Krishnaa-tech/Webscrape.io.svg?style=social&label=Watch)](https://GitHub.com/Krishnaa-tech/Webscrape.io/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/Krishnaa-tech/Webscrape.io.svg?style=social&label=Fork)](https://GitHub.com/Krishnaa-tech/Webscrape.io/network/)
[![GitHub stars](https://img.shields.io/github/stars/Krishnaa-tech/Webscrape.io.svg?style=social&label=Star)](https://GitHub.com/Krishnaa-tech/Webscrape.io/stargazers/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Krishnaa-tech/Webscrape.io/HEAD)
[![Gitter](https://badges.gitter.im/Krishnaa-tech/Webscrape.io.svg)](https://gitter.im/Krishnaa-tech/Webscrape.io?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg) 
![Python 3.11.6](https://img.shields.io/badge/Python-3.11-brightgreen.svg) ![scikit-learnn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg)


<div align="center">
  <h1>Webscrape.io</h1>
  <h3>The Best News Scrapper to categorise News Articles!</h3>
</div>

<p align="center">
  <a href="/scaped_data/classified_articles_data.csv">Obtained Dataset</a> &#xa0; | &#xa0;
  <a href="/model/test_classified_articles_data.csv">Test Dataset</a> &#xa0; | &#xa0;
  <a href="/scaped_data/scrape.py">Web Scrapping Code</a> &#xa0; | &#xa0;
  <a href="/model/model.ipynb">Jupyter Notebook</a> &#xa0; 
</p>

## About ##

This project aims to scrape a news article website to collect the articles with their links, then classify the articles using Text Classification model(s) based on their categories from the [News Website](https://www.hindustantimes.com).


## Instructions 
1. **Install the requirements:** ```pip install -r requirements.txt``` <br>
2. Run the [`scrape.py`](/scaped_data/scrape.py) for scrapping the Articles from [News Website](https://www.hindustantimes.com). <br>
3. The [`obtained dataset`](/scaped_data/classified_articles_data.csv) will be released after web scraping from there use [`model.ipynb`](/model/model.ipynb) for classifying the articles in different categories.
4. Testing the model using [`test dataset`](/model/test_classified_articles_data.csv) and using the pickle file `trained_model.pkl` for using training model weights in [`test_model.ipynb`](/model/test_model.ipynb) file.

<h2> Results & Observations</h2>

<div align="center">
    <p><strong>Training ACCURACY</strong> before Hyperparameter Tuning: <strong>78%</strong></p>
    <p><strong>Training ACCURACY</strong> after Hyperparameter Tuning: <strong>82%</strong></p>
</div>

<div align="center"> <img src="model/test_accuracy.png" alt="Screenshot" /></div>
<div align="center" id="top">
  <img src="model/confusion_matrix_before_boosting.png"  alt="Profile Readme Generator" />
    
  <img src="model/confusion_matrix_after_boosting.png" alt="Profile Readme Generator" />

</div>

<h4 align = "left"> Contributors </h2>
<p align="left">
  <a href="https://github.com/krishnaa-tech">Krish Goyal</a> &#xa0;
</p>
