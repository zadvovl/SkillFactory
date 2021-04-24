This is the last iteration of all. The best result was achieved using a model based on EfficientNetB6 with increased image size (300), batch size 16, number of epoch 8. Result on Kaggle: 0.96659. I believe that a strong base model (EfficientNetB6) as well as image augmentation techniques and ReduceLROnPlateau callback made this result possible. In fact, it looks like ReduceLROnPlateau saved the model from overfitting at epochs 3 and 4. Also, I am glad that EfficientNetB6 didn't throw an OOM error with image size 300.

Previous attempts were made with different settings and proved to be worse than the current result:

1) With the model based on Xception, image size 224, batch size 64, 10 epochs and no batch normalization I managed to achieve 0.94486 on Kaggle.

2) All the attempts to train a model based on EfficientNetB6 with batch size 64 and 32 failed because of OOM error.

What could have been done better:

1) I didn't use fine-tuning techniques apart from transfer learning. I guess the result could be better if I performed the learning iteratively while freezing some layers at each iteration.

2) Even though I tried using albumenation library for image augmentation, it didn't give any useful results. Maybe I simply didn't find a right augmentation technique from this library.

3) I didn't experiment with the head much (apart from adding batch normalization).