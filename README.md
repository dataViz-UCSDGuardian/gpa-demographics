# UCSD Demographics and GPA Disttributions

###Title:  
Family Income's Effect on GPA  
###Authors:  
Alex Yang  
Halle Davis  

###Timeline:  
11/22/16  Project started  
02/13/17  GPA vs. Income [added by Halle Davis]  

###Summary:  
This visualization shows that throughout time GPA is very dependent on one's family income.
Namely, the two variables are positively correlated. 

###Key Points:   
- Definition of Brackets/Income Groups  
  High >98401  
  Med High 65601-98400  
  Med Low 32801-65600  
  Low 32800
- You can tell that the relationship is extremely striking/strong/consistent between income and GPA because the lines /never/ overlap
- I obtained bubble size parameter by  
  N = Number of students in that group  
  N/10 - 28.9 = Size of bubble  
  because I wanted the bubbles to never be more than 150 or less than 30.
  Bubble size and N also have a correlation of 1 so no information is lost.

###Sources:  
http://studentresearch.ucsd.edu/publications/degrees.html

###Libraries:  
plotly

###Final Visualizations  
https://plot.ly/~halle.davis/196/income-and-mean-gpa-over-the-years/
https://plot.ly/~halle.davis/198/income-and-mean-gpa-over-the-years/
