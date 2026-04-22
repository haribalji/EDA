import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("studentperformances.csv")

#inorder to understand the data 
print(df.info())#it gives the data info


print(df.head())
print(df.isnull().sum())  # check missing values

df = df.dropna()  # remove missing rows (simple approach)
print(df.describe())


#comparing the social_media_hours with math_score using the  scatterplot
plt.scatter(df["social_media_hours"], df["math_score"])
plt.xlabel("social_media_hours ")
plt.ylabel("Math Marks")
plt.title("social_media_hours vs Math Marks (negative corelation)")
plt.show()


# formula to measure  the relationship between 2 variables 
print("the correlation between socialmedia and math score",df["social_media_hours"].corr(df["math_score"]))

plt.scatter(df["study_hours_per_day"], df["math_score"])
plt.xlabel("Study Hours")
plt.ylabel("Math Marks")
plt.title("Study Hours vs Math Score (Positive Relationship Observed)")
plt.show()

#it is for tracking  the attendance and  math marks
plt.scatter(df["attendance_rate"], df["math_score"])
plt.xlabel("Attendance")
plt.ylabel("Math Marks")
plt.show()


#heatmap example
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()


#--inorder to understand the univariate(single column) histplot
sns.histplot(df["math_score"], kde=True)
#kde--it is added to have smooth curve on the histogram
#kernel density estimate
plt.show()



#BOXPLOT TO IDENTIFY THE SUMMARY OF THE DATA SET
sns.boxplot(x=df["math_score"])
plt.show()


#to visualize the categorial data
sns.countplot(x="pass_fail", data=df)
plt.show()


#working with pairplot with student performace dataset
sns.pairplot(df)
plt.show()

#pairplot with extra dimensoinal

sns.pairplot(df, hue="gender")
plt.show()



