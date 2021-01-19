OVERVIEW

1) Training data has been extracted from www.auto.ru using the code from auto_ru_parser.ipynb. 
2) Notebook sf-dst-car-price-prediction-v16-vlad-zadvornev.ipynb is a copy of my notebook used for kaggle competition. It can be
executed locally if contents of own_train_set_20210115.rar and test.csv.zip are extracted into the same folder.
3) IMPORTANT: please see the notebook for detailed comments. Every action I performed has a comment.

WHAT HAS BEEN DONE

1) Data from training dataset has been explored, cleaned and enriched.
2) New features have been created.
3) Multiple algorithms have been tested in sf-dst-car-price-prediction-v16-vlad-zadvornev.ipynb after data preparation phase.
RandomForestRegressor has shown the best result. I am sure that the result could have been better if I succeeded in hyperparameter 
tuning. However, I couldn't do it - the job took too long to execute.
4) Stacking RandomForestRegressor with CatBoost hasn't improved the result.

WHAT COULD HAVE BEEN DONE BETTER

1) More new features could have been generated.
2) Another attempt of tuning hyperparameters for RandomForestRegressor could have been made (maybe with less parameters it could succeed).
