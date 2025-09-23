import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np # linear algebra

data=pd.read_csv("C:/Users/david/OneDrive/Documentos/my_study_env/my_projects/dataframes/spambase.data")
print(data.shape)

data.isna().any().any()

# Dataset information
print(data.info())

# Summary statistics
print(data.describe())

sns.countplot(x=data['spam'])
plt.title('Distribution of Spam and Non-Spam Emails')
plt.show()

data.hist(bins=20, figsize=(20, 15))
plt.show()

correlations = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=False)
plt.title('Correlation Matrix')
plt.show()

