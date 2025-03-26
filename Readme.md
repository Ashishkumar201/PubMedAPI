# PubMed Paper Fetcher

## Description
A Python CLI tool to fetch and filter research papers from PubMed API.

## Installation
1. Install Python 3.10+
2. Install Poetry: `pip install poetry`
3. Install dependencies: `poetry install`

## Usage
Run the following command to fetch papers:
```sh
python main.py <search query >  -f results.csv -d

Search query refers to the topic the user is going to search for example:
"cancer" 
"Covid19"
Also users can configure their search with specified query 
as '"covid-19" and 2024'
this will search for cases for searched query in the particular year 


The structure of project is as there 
major files
Fetcher
processor
writer 
main file controls the code of internal files
fetcher files extracts data from the API URL
the processor file processes the data extracted and hence
the file calleda s writer throws the content processed to the csv file to view



#Future Development

Looking for developing the interface of the application so that it can be deployed at a server on vercel or some other platform to view and use by the person viewing the code


