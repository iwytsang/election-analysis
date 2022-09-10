# Election Analysis

## Overview of Election Audit

### Purpose
The purpose of the analysis is to assist Tom and his manager Seth, both Colorado board of elections employees, in an election audit of results. In addition to the breakdown of the results by candidate name, number of votes, and percentage of votes, the election commission also requested some additional data to complete the audit which included the voter turnout for each county, the percentage of votes for each county, as well as the county with the highest turnout.


## Election-Audit Results
Once the python script was run, we were able to analyze the results from the election_results.csv file and output synthesized data onto the election_analysis.txt file as shown below.

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
The Python script that was created in order report our U.S. congressional election results is a great tool that can be used for any other elections in order to count the number of candidates, total number of votes, percentage of votes, and then output the results onto a separate text file.
To use it for other elections that have more candidates, we could modify the script to only print out the name, number of votes, and percentage of votes for the top 3 candidates in the election. We could also print out the top 3 counties with the most voter turnouts. 

