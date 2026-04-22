here i  am documenting some of the  important concept of eda

# some of the important ouputs:
#comparing the social_media_hours with math_score using the  scatterplot
<img width="640" height="480" alt="socialvsmath" src="https://github.com/user-attachments/assets/cf4e0326-d50a-4bcc-abe7-5a545b282f6f" />

here it comes with the -ve correlation

#now comparing the study hours with math score
it generates the +ve corelation
<img width="640" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/36e12f40-a5a0-4678-9277-a1c03bd253bb" />


#attendance vs math score
the correlation between attendance_rate and math score 0.1334278647832626 by which we can say it is weak relation<img width="640" height="480" alt="socialvsmath" src="https://github.com/user-attachments/assets/334f9381-ab8c-46b0-b066-531d77d95875" />


# understanding the all the numerical columns relationship using heatmap

<img width="1736" height="925" alt="image" src="https://github.com/user-attachments/assets/3d6521cc-8c00-45d6-ae3d-ebc3521b3842" />


by doing the analysis we can say that relationship between math_score and studyhours_perday it is strong postive relation but not perfect  with value of 0.5 by observing the graph

#Inorder to analysis the single column data   we used the histogram with equal bins 
<img width="640" height="480" alt="histplotgraph" src="https://github.com/user-attachments/assets/b934a727-c49f-4c74-9c17-3aca3cec3be4" />

# Then using boxplot
<img width="640" height="480" alt="boxplotcurve" src="https://github.com/user-attachments/assets/4f28ed23-f816-49d0-a563-27fc6c6bae99" />


here by seeing this we say that

1st quartile lies in score 40 by which we can say 25% of the students score are below 40

3rd quartile lies in score 60 by which we can say 75% of the students score are below 40

50% of the people score are lying between 40 to 60

minimum value can 15 and maximum value can 85 and outlier value can 99 and 0.17


#here  working with countplot inorder to measure the count of the categacial data distribution
<img width="640" height="480" alt="countplot" src="https://github.com/user-attachments/assets/5692b21c-5e75-4958-b699-030afd30c316" />

measuring the male and female student  distribution


#then pairplot to comapare all the numerical column with visual inorder to identify the pattern


<img width="1536" height="754" alt="pairplot1" src="https://github.com/user-attachments/assets/636f58a1-4574-40e9-af7b-d65f5d4d11b1" />

with selective column
<img width="749" height="749" alt="pairplot2" src="https://github.com/user-attachments/assets/d2639ff5-a20c-49a3-b5e9-df8e73854c8c" />

#pairplot with hue to add the 3rd demension with hue="gender" 
#noted that in hue we can pass only categorial data only


<img width="1536" height="754" alt="pairplot" src="https://github.com/user-attachments/assets/bf12f8cc-0cc2-44f4-a35c-0de5a6049667" />


where data  will be colored to indicate the distribution of group data

here digaonal graph is kde curve of the group data falling in that range providing  extra demension  using hue="gender" concept

if the overlapping is high then data is normally distributed and less overlapping then data is spread-out
