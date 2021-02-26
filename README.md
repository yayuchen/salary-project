# Understanding individuals salary distribution based on job description
## Salary prediction
-----------------------------------------------------------------------------------------------------------------------------------------

## Table of contents

### Problem

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

### Conclusion

-----------------------------------------------------------------------------------------------------------------------------------------

### The problem:
> 





# salary prediction project

## Data statistics examine:
**Looking for the most importance factor could impact on salary trend.**
  
## Discover:

+ Load data: 
  - import module and load essential dataset
+ Clean data: 
  - determine missing or duplicated values 
  - examine statistical details 
  - reveal target data distribution 
  - review upper and lower outlier data
+ Explore data:
  - plot each features distribution and correlation with salary
  - transform categorical feature values with correspond salary mean
  - plot heatmap with mean values to measure features correlaion with salary
    
## Develop:
+ Feature engineering:
  - label encoding categorical features 
  - grouping categorical features and calculate groups statistics( target central tendency and target percentiles ) 
  - merge new data as new features
+ Model tuning:
  - use RandomizedSearchCV and GridSearchCV to optimize model parameters 
  - create model by optimized parameters 
  - test model 
  - select the best model
  - examine feature importances
    
## Deploy:
+ deploy the best model on test dataset and get prediction results 
+ save results

## Comment
**MSE decreased, new feature groups mean it the most importances feature.**
