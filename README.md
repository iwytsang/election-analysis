# Election Analysis

## Overview of Election Audit

### Purpose
The purpose of the analysis is to assist Tom and his manager Seth, both of whom are Colorado board of elections employees, to write a Python script that will output into a text file the results of a U.S. congressional election in Colorado. In addition to the breakdown of the results by candidate name, number of votes, and percentage of votes, the election commission also requested some additional data to complete the audit which included the voter turnout for each county, the percentage of votes for each county, as well as the county with the highest turnout.


## Election-Audit Results
Once the python script was completed, we were able to analyze the data of election results from the election_results.csv file and present our findings on the election_analysis.txt file as shown below.

![image](https://user-images.githubusercontent.com/108503112/189497025-df0ee755-7ab4-4218-b9d0-314588ba160b.png)

From the results above, we can answer the following questions about the election:

* **How many votes were cast in this congressional election?**

  369,711 votes were cast in this congressional election.

* **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**

  Jefferson county had 38,855 votes which was 10.5% of the total votes.\
  Denver county had 306,055 votes which was 82.8% of the total votes.\
  Arapahoe county had 24,801 votes which was 6.7% of the total votes.


* **Which county had the largest number of votes?**

  Denver had the largest number of votes with 306,055.


* **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**

  Charles Casper Stockham had  85,213 votes which was 23.0% of the total votes.\
  Diana DeGette had 272,892 votes which was 73.8% of the total votes.\
  Raymon Anthony Doane had 11,606 votes which was 3.1% of the total votes.

* **Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**

  From the results, we can conclude that the candidate that won the election was Diana DeGette. Her winning vote count was 272,892 votes and the percentage of total votes was 73.8%.


## Election-Audit Summary
The Python script that was created to report our U.S. congressional election results is a great tool that can be used for any other election results to count the number of candidates, total number of votes, percentage of votes, and then output the results onto a separate text file. It can also be used to provide a breakdown of the number of votes per county, percentage of total votes for each county, and declare which of the counties had the largest number of votes.

In this particular election, there were only 3 different candidates and 3 different counties. An example of how the script could be modified to use it for other larger-scale elections that have more candidates is that we could change the script to only print out the name, number of votes, and percentage of votes for the top 3 candidates that received the most votes in the election.

Another example of how we could modify the script is that we could also only print out the top 3 counties with the most voter turnouts, their number of votes, and percentage of votes per county. 

