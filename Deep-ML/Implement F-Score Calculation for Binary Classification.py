import numpy as np

def f_score(y_true, y_pred, beta):
    """
    Calculate F-Score for a binary classification task.

    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: The weight of precision in the harmonic mean
    :return: F-Score rounded to three decimal places
    """
	"""
	# Recall = TP/(TP+FN)
	# Precision = TP/(TP+FP)
  Fβ = (1 + β**2) * (precision * recall) / β**2*precision + recall

Precision is Preferred When False Positives are Costly
   - Fraud detection, spam filtering, medical diagnostics, or any situation where acting on a false positive has high consequences.
Recall is Preferred When False Negatives are Costly 
   - Disease screening, search engines, criminal identification, or any case where missing a positive instance is a serious error.

Balancing Precision and Recall with the F-beta Score
   - Increase beta to more than one to make recall more important.
   - To emphasize precision reduce beta below one.
	
 """
    tp, fn, fp = 0, 0, 0
    
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            tp += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            fp += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            fn += 1
    
    # Avoid division by zero
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    # Avoid division by zero in F-score calculation
    if precision == 0 and recall == 0:
        return 0.0
    
    f_score_value = (1 + beta**2) * (precision * recall) / ((beta**2 * precision) + recall)
    return round(f_score_value, 3)
