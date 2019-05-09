## References:
- [Advanced Data Mining with Weka - timeseriesForecasting package (Video)](https://www.youtube.com/watch?v=NLTLUmt77-E)
- [Advanced Data Mining with Weka - Looking at forecasts (Video)](https://www.youtube.com/watch?v=NDwn7G8zTOU)
- [Advanced Data Mining with Weka (Slide)](https://drive.google.com/file/d/0B2tuXEy73YswQ3A2VW9GUlFabUk/view)

### Linear Regression
- Linear regresssion with lags?
- 

### Weka: Classifier

### Weka: Forecast

#### Basic Configuration
- Number of time units to forecast: 14
- Time stamp: Date
- Periodicity: Daily
- Perform Evaluation: Yes

#### What happened with missing values?

#### Default configuration

#### Lag Creation Tab
- Tick Remove leading instances with unknown lag values?

#### Evaluation on training data

#### Evaluation on test data
- 1,7,14 steps ahead graph comparisons
- why overshooting values propagates from 7 to 14 steps ahead?

### Simplify the model
- customise periodic attributes (select none)
- use custom lag length (min-max 7)
- lag creation more options: uncheck `Include products of time` and `Included products of time and lagged variables`

### Weka: Experimenter