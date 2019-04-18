# Web_Scraping-Problem_Statement

Web Scraping program for extracting data from the website of Directory of Cities, Towns & Region of India, into  a CSV File.

## Built With 
* Language: Python
* Environment: Jupter Notebook
* Libraries: BeautifulSoup, Pandas


## Solution Implemented

Created an empty Pandas DataFrame <br/>
Started by extracting the home page HTML file into a BeautifuSoup object <br/>
Iterated through the names of the states extracting each link <br/>
To handle different level in each state, created a recursive function, with the terminating condition of finding the final table of the city list <br/>
Converted to CSV <br/>
* The function iterated through all the letters,  extracting each link, 
* Finally on finding the table, appended each entry into the DataFrame , and returned the dataframe



## Author

Aditya Bansal
