# Introduction:
This project focuses on analyzing student performance data using Exploratory Data Analysis (EDA). The objective is to identify key factors that influence academic performance, particularly math scores.

# Dataset Overview

The dataset contains 10,000 student records with 23 features, study habits, and academic scores. The variables include study hours, attendance rate, social media usage, and  math scores.


# Data Cleaning (Missing Values)
A data quality check was performed, and no missing values were found in the dataset.


# some of the important ouputs:

# comparing the social_media_hours with math_score using the scatterplot with log-scale

<img width="640" height="480" alt="studyvsmathwithlog" src="https://github.com/user-attachments/assets/7759d5ca-8737-45c4-8d87-5b1c11b10fc9" />


# what is shown :
The graph illustrates the relationship between students  mathematics scores and their social media usage, highlighting how social media activity may impact students performance in mathematics.

# What is the observation
The scatter plot shows a negative correlation between social media usage and math marks.
This means that as social media usage increases, math marks tend to decrease.
However, the points are widely spread out, indicating that the relationship is weak.




# now comparing the study hours with math score how they impact
it generates the +ve corelation
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/36e12f40-a5a0-4678-9277-a1c03bd253bb" />

# what is shown :
The graph illustrates the relationship between students  mathematics scores and  study hours usage, explaining how study hours  may impact students performance in mathematics.

# What is the observation
by seeing the graph we can say that study hours increase the maths marks also increase and the 
points moving from the left to right in the upward direction which is clearly stating that it is positive corealtion and  the points is spread and moving upward so it is moderate realtionship ,by seeing this we can finally come to conclusion that student  study more hours will tend to gain more marks




# here we are explain about the relationship between attendance vs math score


<img width="640" height="480" alt="mathvsatt" src="https://github.com/user-attachments/assets/769b7a6c-c0d7-47d6-bbfe-65da6e4b7720" />

# what is shown :
The graph illustrates the relationship between students  mathematics scores and attendance , explaining how attendance  may impact students performance in mathematics.

# What is the observation

as here the attendance increase the maths marks also increase but the data is spread so we can say it is +ve corelation and weak relationships
and correlation value also indicating that 0.1334278647832626 


# Here comparing  all the numerical columns relationship using heatmap

<img width="1736" height="925" alt="image" src="https://github.com/user-attachments/assets/3d6521cc-8c00-45d6-ae3d-ebc3521b3842" />




here in this graph all the numerical feature is compared with each other and diagonal is compared with itself so it's value is 1 ,
red colour is indicating +ve corealation 
blue colour is indicating -ve corealtion 
fade light color is indicating the weak relationship 
observing the graph for mathscore with social media it indicating the negative correaltion as value is -0.22 
# we know that
1 perfect +ve correlation
0.7 to 1 strong +ve correlation 
0.4 to 0.7 moderate +ve correlation 
0.4 to 0 weak +ve correlation 
0 - no correlation
0 to -.4 weak -ve correlation 
-0.4 to -.7 moderate -ve correlation 
-0.7 to -1 strong -ve correlation 
1 is perfect -ve correlation

by doing the analysis we can also say that relationship between math_score and studyhours_perday it is strong postive relation but not perfect  with value of 0.5 by observing the graph

# Inorder to analysis the single column data   we used the histogram with equal bins  size
<img width="640" height="480" alt="histplotgraph" src="https://github.com/user-attachments/assets/b934a727-c49f-4c74-9c17-3aca3cec3be4" />


The histogram with KDE shows the distribution of math scores. The data is unimodal(one peak area) , indicating that most students scored between 40 and 60. The distribution appears bell shape which indicating it is normal and symmetric, with fewer observations in the lower and higher score ranges, forming the tails.


# Then using boxplot
<img width="640" height="480" alt="boxplotcurve" src="https://github.com/user-attachments/assets/4f28ed23-f816-49d0-a563-27fc6c6bae99" />


# what is shown

here boxplot is used to give the summary of the given dataset feature
where it speaks about 
minimum value ,maximum value,1st quartile ,2nd quartile ,3rd quartile and outliers of the given feature
 
here by seeing this we say that

1st quartile lies in score 40 by which we can say 25% of the students score are below 40(left side line)

3rd quartile lies in score 60 by which we can say 75% of the students score are below 60(right side line)

blue color area indicating 50% of the people score are lying between 40 to 60 

minimum value can 15 and maximum value can 85 and outlier value can 99 and 0.17


# Here using  countplot inorder to count the frequency of categorical  data distribution

<img width="640" height="480" alt="countplotforgrade" src="https://github.com/user-attachments/assets/202b05a2-b5c3-4963-bf9e-ebda6177dafa" />


here just calculating the frequency of the  categorical data feature as here we have taken the grade categorical feature which has A ,B,C,D,F 
# What is the observation :
By Observing the grade categorical we can see that grade 'F' is secured by more no of students ,which indicating that more no of failures occured



# Here  pairplot is used to  compare all the numerical column with visuals inorder to identify the pattern with selective column

<img width="749" height="749" alt="pairplot2" src="https://github.com/user-attachments/assets/d2639ff5-a20c-49a3-b5e9-df8e73854c8c" />

# By Observation from the above graph
The pairplot is used to compare multiple numerical features simultaneously. The diagonal plots represent the distribution of each feature, showing that all three scores follow an approximately normal distribution. The off-diagonal scatter plots show the relationships between variables. The upper and lower triangles are symmetric and convey the same information. From the scatter plots, we observe a strong positive correlation between math, reading, and writing scores, indicating that students who perform well in one subject tend to perform well in others.

# pairplot with hue to add the 3rd demension with hue="gender" 
# noted that in hue we can pass only categorcial data only

<img width="1536" height="754" alt="pairplot" src="https://github.com/user-attachments/assets/bf12f8cc-0cc2-44f4-a35c-0de5a6049667" />

The hue parameter adds a third variable (categorical) to the visualization,
It separates the data using colors
Blue → Male
Orange → Female

In diagonal the graphs appears smooth and wavely 
if smooth(bell shape) then in each bin no of male and female students are equal because of which the curve overlap and they appear smooth
if wavely (wave like structure ) means then in each bin their is different count of male and female
The off-diagonal scatter plots show the relationships between variables and which people dominated there(male or female)


# conclusion

The analysis indicates that study hours have a moderate positive relationship with student performance, while attendance shows a weak positive relationship. Social media usage has a weak negative association with marks. Additionally, the dataset contains slightly more failing students than passing students, suggesting a mild imbalance in performance outcomes. Overall, study habits appear to have a stronger influence on performance compared to other factors.
