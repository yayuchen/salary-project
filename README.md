# Understanding individuals salary distribution based on job descriptions
## Salary prediction


-----------------------------------------------------------------------------------------------------------------------------------------



## Table of contents

### [Problem](#why-this-problem)
* **WHY** this problem?
*  Purpose

### [Data examine](https://nbviewer.jupyter.org/github/yayuchen/salary-project/blob/main/notebooks/examine/data%20statistical%20examine.ipynb)
* Examine statistical information
* Target determine
* Clean data

### [Data explore](https://nbviewer.jupyter.org/github/yayuchen/salary-project/blob/main/notebooks/explore/data%20exploration.ipynb)
* Feature exploration with target
* Feature correlation with heatmap plot

### [Data develop](https://nbviewer.jupyter.org/github/yayuchen/salary-project/blob/main/notebooks/develop/data%20develop.ipynb)
* Pre-processing categorical features with **Label encoding**
* **Grouping** categorical features
* Create new statistical features by grouped data
* Model tuning: use **RandomizedSearchCV** and **GridSearchCV**
* Model evaluation: Using **cross validation** evaluate models performance by **MSE**

### Data deploy
* Using [**flask**](https://github.com/yayuchen/salary-project/blob/main/docker/app.py) for app backend to web
* Using dockerfile to create image and deploy to cloud 

### [Conclusion](#conclusions)
* [**Salary prediction OOP**](https://nbviewer.jupyter.org/github/yayuchen/salary-project/blob/main/notebooks/SalaryPrediction_OOP.ipynb)
* Summary
* Business benefit




-----------------------------------------------------------------------------------------------------------------------------------------



## Problem

### **Why** this problem?

> When a business open a vacancy, HR would have a communication with management about vacancy position, the most common questions would be what title for the position, applicant qualifications, and these would impact on any applicant's salary and benefit if the business decide to hire them. 

### Purpose:

> * Utilizing collection of job description for individual roles to analyse how factors impact on individual salary.                                  
> * Determining any differences between different industries, majors or degrees.      

> * Considering business conditions, like location, size of business, number of employees and use this project as reference.

> * Understanding the correlation of salary with years of experience and workplace distance away from metropolis, then base on this project, it can provide a good reference for HR to compose a fair hiring description.
> 

### Conclusions

#### Summary: 

> **Job types:**

>> * The strongest correlation is job type, the job type which salary mean below 100 is **25%** of all individuals, only a job role as **JUNIOR** or **JANITOR**.
>> 
>> * Compare the highest and lowest salary avg in job type. (**70 vs 145**)
>> 
>> * The top 3 high salary industry is **oil, financa and web**, the average salary is over 120, even the job role as a junior in these 3 industry, the lowest income still higher than other industries at same level.
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
>>>* Job types **BELOW** group mean: **60%**(other roles) vs **40%**(Junior & Janitor).                                                     
>>>* Job types **ABOVE** group mean: **93%**(other roles) vs **7%**(Junior & Janitor).

>> Comparing origin features, only **years of experience** and **milesFromMetropolis** have higher importance scores.
>> 

# Business benefit:

> From dataset's statistical information, we know that if any individual has more relative experience, the average salary is 1.3 times higher. But, **Experience** isn't equal **Ability**. If someone's capable to perform well than more experiences person, business can save more budget from hiring right person who doesn't have much experiences. Besides, management can utilize the spare 30% of budget as award or bonus and don't need to shorten or extend other budget plans.
> 
