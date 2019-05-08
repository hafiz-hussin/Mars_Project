## References:
- [Linear Regression with lags (Video)](https://www.youtube.com/watch?v=9R0mz_gfhBs&list=PLm4W7_iX_v4Msh-7lDOpSFWHRYU_6H5Kx&index=3)
- 

### Linear Regression
- Linear regresssion with lags?
- 

### Weka: Classifier

### Weka: Forecast
- Number of time units to forecast: 14
- Time stamp: Date
- Periodicity: Daily

#### What happened with missing values?

#### Default configuration

#### Lag Creation Tab
- Tick Remove leading instances with unknown lag values?

#### Evaluation on training data

#### Evaluation on test data
- 1, 7, 14 steps ahead comparisons
- why overshooting values propagates from 7 to 14 steps ahead?

### Simplify the model
- customise periodic attributes (select none)
- use custom lag length (min-max 7)
- lag creation more options: uncheck `Include products of time` and `Included products of time and lagged variables`

### Weka: Experimenter