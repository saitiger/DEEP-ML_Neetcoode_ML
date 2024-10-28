import numpy as np
def recall(y_true, y_pred):
  """
  Mnemonics to Remember 
  Precision and Recall
  
  Precision **Predicted** from **Pre**cision positive: TP/(TP+FP)
  Recall is **Real** from **Re**call : TP/(TP+FN)

  Sensitivity : TP/(TP+FN)
  Specificity : TN/(TN+FP)

  Mnemonics to Remember 
  
  SNIP (Sensitivity Is Positive)
  SPIN (Specificity Is Negative)
  """
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    false_negatives = np.sum((y_true == 1) & (y_pred == 0))
    return round(true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0.0,3)
