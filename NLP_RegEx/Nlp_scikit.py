## Import the cohen_kappa_score function from the 'metrics' module of the scikit-learn library
from sklearn.metrics import cohen_kappa_score
from sklearn import metrics
### Define two lists named 'a1' and 'a2'
a1 = ['ADJ', 'AUX', 'NOUN', 'VERB', 'VERB']
a2 = ['ADJ', 'VERB', 'NOUN', 'NOUN', 'VERB']

## #Use the cohen_kappa_score() function to calculate agreement between the lists
# print(cohen_kappa_score(a1, a2))

####### ----------->
# ## Define a list named 'gold_standard' and 'predictions'.
gold_standard = ['ADJ', 'ADJ', 'AUX', 'VERB', 'AUX', 'NOUN', 'NOUN', 'ADJ', 'DET', 'PRON']
predictions = ['NOUN', 'ADJ', 'AUX', 'VERB', 'AUX', 'NOUN', 'VERB', 'ADJ', 'DET', 'PROPN']
data = metrics.accuracy_score(gold_standard, predictions)
# print(data)
pos_tags = set(gold_standard + predictions)
pos_tags = list(sorted(pos_tags))
# print(pos_tags)
####   confusion_matrix() function for automatically generating confusion matrices.
# print(metrics.confusion_matrix(gold_standard, predictions))

# ## Calculate precision between the two lists for each class (part-of-speech tag)
precision = metrics.precision_score(gold_standard, predictions, average=None, zero_division=0)
# print(precision)
###### Combine the 'pos_tags' set with the 'precision' array using the zip() function; cast the result into a dictionary
# print(dict(zip(pos_tags, precision)))

# ##Calculate precision between the two lists and take their average
macro_precision = metrics.precision_score(gold_standard, predictions, average='macro', zero_division=0)
# print(macro_precision)

# print(metrics.classification_report(gold_standard, predictions, zero_division=0))
