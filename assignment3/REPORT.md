# Report
> Group/Collaborator:
> Yijie Lu (pennkey: luyijie), Yuzhou Lin (pennkey: yzlin)

## Baseline Models (Yijie Lu, Yuzhou Lin)
### All Complex
We categorized all words as complex and got an accuracy of 41.8% in the test dataset.
### Length Threshold
We iterated through all possible lenghth threshold from the shortest to longest word and found the threshold of 8 gives us the best accuracy. Using word length 8 as our threshold, we achieved an accuracy of 72.8% in the train dataset and 74.5% in the test dataset.
### Frequency Threshold
We iterated through all possible n-gram frequencies of the words in the train dataset and found the threshold of 8253948 gives us the best accuracy. Using n-gram frequency 8253948 as our threshold, we achieved an accuracy of 67.2% in the train dataset and 68.4% in the test dataset.

## Machine Learning Models (Yijie Lu, Yuzhou Lin)
From the train dataset, we extracted 2 features (word length & word frequency) from every word and put them in a numpy array where each row represents a word with 2 features.
### Naive Bayes
Using sklearn's built-in naive bayes classifier, we achieved an accuracy of 54.175% in the train dataset and 51.4% in the test dataset.
### Logistic Regression
Using sklearn's built-in logistic regression classifier, we achieved an accuracy of 55.775% in the train dataset and 56.9% in the test dataset.

### Extra Credit Part (Yijie Lu)
1.Decision Tree
Using sklearn's built-in decision tree classifier, we achieved an accuracy of 77.8% in the train dataset and 78.3% in the test dataset.
The algorithm finds an optimal threshold to split on each feature and generates a decision tree.
2.Random Forest:
Using sklearn's built-in decision tree classifier, we achieved an accuracy of 77.95% in the train dataset and 79.1% in the test dataset.
The algorithm uses an ensemable of decision trees outputs the majority class.
3.AdaBoost:
Using sklearn's built-in decision tree classifier, we achieved an accuracy of 76.925% in the train dataset and 78.1% in the test dataset.
The algorithm uses decision stump as its base and repeatedly train the model with lower weight on samples that were correctly classified and larger weight on samples incorrectly classified. Eventually we reach a working classifier.

## Reflection (Yuzhou Lin)
### How long did this assignment take you?
Approximately 7 hours for in total
### What were some things you liked and didn't like?
liked: very clear instruction for steps to follow (README)  
didn't like: the training & test performances for Bayes/Logit are only slightly higher than 0.5  
### Tell me a joke! (from Quora)
Interviewer: What’s your biggest strength?  
Me: I’m an expert in Machine Learning.  
Interviewer: What’s 9 + 10 ?  
Me: I’m 3.  
Interviewer: Not even close. It’s 19.  
Me: It’s 16.  
Interviewer: Wrong. It's still 19.  
Me: It’s 18.  
Interviewer: No, it’s 19… Arghhh  
Me: It’s 19.  
Interviewer: You are hired.  
