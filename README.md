# salary prediction project

## Define
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