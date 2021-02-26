# Understanding individuals salary distribution based on job descriptions
## Salary prediction


-----------------------------------------------------------------------------------------------------------------------------------------



## Table of contents

### [Problem](#purpose)

### [Data determine](https://github.com/yayuchen/salary-project/blob/main/examine/data%20statistical%20examine.ipynb)
* Examine statistical information
* Target determine
* Clean data

### [Data exploration](https://github.com/yayuchen/salary-project/blob/main/explore/data%20exploration.ipynb)
* Feature exploration with target
* Feature correlation with heatmap plot

### [Data develop](https://github.com/yayuchen/salary-project/blob/main/develop/data%20develop.ipynb)
* Pre-processing categorical features with **Label encoding**
* **Grouping** categorical features
* Create new statistical features by grouped data
* Model tuning: use **RandomizedSearchCV** and **GridSearchCV**
* Model evaluation: Using **cross validation** evaluate models performance by **MSE**

### [Conclusion](#results)



-----------------------------------------------------------------------------------------------------------------------------------------



## Purpose:

> Utilizing collection of job description for individual roles to analysis how factors impact on salary.                                  
> Determining any differences between different industries.                                                                                
> Understanding how different of salary between years of experience and workplace distance away from metropolis.
> 
## Covering:

> Statistical examine of dataset
> Features exploration 
> Features preprocessing
> Model develop
> 


# What to optimize?

> For future study, collect more features like individual departments, or consider any commission included in salary, it might help to understand how features impact on salary more precisely.
> 

### Results:

> **Job types:**

>> The strongest correlation is job type, the job type which salary mean below 100 is **25%** of all individuals, only a job role as **junior** or **janitor**.
>> 
>> Compare the highest and lowest salary avg in job type. (**70 vs 145**)
>> 
>> The top 3 high salary industry is **oil, financa and web**, the average salary is over 120, even the job role as a junior in these 3 industry, the lowest income still higher than other industries at same level.
>
> **Degrees:**

>> The average salary with the degree level above high school is **1.2 times Higher** than high school or none degree level.

> **Major:**

>> Any individual with major, the average salary is **1.3 times Higher** than without major.

> **Years of experience:**

>> The average of experience is **12** years, the salary above the 12 yrs is **1.3 times Higher** than below.

> **Miles from metropolis:**

>> Average distance is **49.5** miles, the average is **1.2 times Less** if workplace distance over average miles.

> **New features: Grouping categorical features**

>> New feature **group mean** become the most important feature for train dataset.
>>>Job types **BELOW** group mean: **60%**(other roles) vs **40%**(Junior & Janitor).                                                     
>>>Job types **ABOVE** group mean: **93%**(other roles) vs **7%**(Junior & Janitor).

>> Comparing origin features, only **years of experience** and **milesFromMetropolis** have higher importance scores.
