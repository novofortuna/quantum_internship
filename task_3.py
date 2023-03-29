import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

def get_predictions():
    df_train = pd.read_csv('data/internship_train.csv')
    
    X = np.expand_dims(((df_train['6']**2 + df_train['7'])).to_numpy(), 1)
    y = df_train.loc[:,'target']

    model_LR = LinearRegression()
    model_LR.fit(X, y)

    df_test = pd.read_csv('data/internship_hidden_test.csv')
        
    X_test = np.expand_dims(((df_test['6']**2 + df_test['7'])).to_numpy(), 1)
    
    predictions = model_LR.predict(X_test)
    
    pd.DataFrame(predictions, columns=['y_pred']).to_csv('data/preds.csv', index = False)
    

if __name__ == "__main__":
    get_predictions()

