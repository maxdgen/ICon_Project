import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, confusion_matrix, ConfusionMatrixDisplay,
                             f1_score, precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from data import CvDData

class CvDModel:
    def __init__(self, model_name: str, cvd_data: CvDData, test_size: float = 0.5):
        self.model_name = model_name
        self.scores = {}
        
        X, y = cvd_data.get_training_data()
        
        # splitting our data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = test_size,
                                                                                random_state = np.random.RandomState(0))
        
        # creating a transformer object
        column_transformer = make_column_transformer((OneHotEncoder(), ['gender', 'smoke', 'alco', 'active']),
                                                     (StandardScaler(), ['age', 'height', 'weight', 'ap_hi',
                                                                         'ap_lo', 'cholesterol', 'gluc']),
                                                     remainder = 'passthrough')
        
        # transforming the training features
        self.X_train = column_transformer.fit_transform(self.X_train)
        self.X_train = pd.DataFrame(data = self.X_train, columns = column_transformer.get_feature_names_out())
        
        # transforming the training data
        self.X_test = column_transformer.transform(self.X_test)
        self.X_test = pd.DataFrame(data = self.X_test, columns = column_transformer.get_feature_names_out())
    
    def get_model_name(self):
        return self.model_name
    
    def predict(self):
        pass
    
    def metrics_calculation(self):
        self.scores['accuracy'] = accuracy_score(self.y_test, self.predictions)
        self.scores['precision'] = precision_score(self.y_test, self.predictions)
        self.scores['recall'] = recall_score(self.y_test, self.predictions)
        self.scores['f1'] = f1_score(self.y_test, self.predictions)
    
    def get_metrics(self):
        return self.scores
    
    def print_metrics(self):
        print('Metrics for the model ' + self.model_name + ':')
        print('accuracy  : ' + str(self.scores['accuracy']))
        print('precision : ' + str(self.scores['precision']))
        print('recall    : ' + str(self.scores['recall']))
        print('f1        : ' + str(self.scores['f1']))
    
    def get_values(self):
        tp = self.c_matrix[1, 1]
        fp = self.c_matrix[0, 1]
        tn = self.c_matrix[0, 0]
        fn = self.c_matrix[1, 0]
        return tp, fp, tn, fn
    
    def plot_confusion_matrix(self):
        d_matrix = ConfusionMatrixDisplay(confusion_matrix = self.c_matrix)
        d_matrix.plot()
        
        plt.grid(False)
        plt.title('CM ' + self.model_name)
        plt.show()

class CvDDecisionTree(CvDModel):
    def __init__(self, cvd_data: CvDData, test_size: float = 0.5):
        CvDModel.__init__(self, 'Decision Tree (DT)', cvd_data, test_size)
    
    def predict(self):
        # building and fitting the classifier
        self.model = DecisionTreeClassifier(max_depth = 15)
        self.model.fit(self.X_train, self.y_train)
        
        # making predictions
        self.predictions = self.model.predict(self.X_test)
        
        self.c_matrix = confusion_matrix(self.y_test, self.predictions)

class CvDLogisticRegression(CvDModel):
    def __init__(self, cvd_data: CvDData, test_size: float = 0.5):
        CvDModel.__init__(self, 'Logistic Regression (LR)', cvd_data, test_size)
    
    def predict(self):
        # building and fitting the classifier
        self.model = LogisticRegression()
        self.model.fit(self.X_train, self.y_train)
        
        # making predictions
        self.predictions = self.model.predict(self.X_test)
        
        self.c_matrix = confusion_matrix(self.y_test, self.predictions)

class CvDSupportVectorMachine(CvDModel):
    def __init__(self, cvd_data: CvDData, test_size: float = 0.5):
        CvDModel.__init__(self, 'Support Vector Machine (SVM)', cvd_data, test_size)
    
    def predict(self):
        # building and fitting the classifier
        self.model = SVC(kernel = 'sigmoid')
        self.model.fit(self.X_train, self.y_train)
        
        # making predictions
        self.predictions = self.model.predict(self.X_test)
        
        self.c_matrix = confusion_matrix(self.y_test, self.predictions)

class CvDRandomForest(CvDModel):
    def __init__(self, cvd_data: CvDData, test_size: float = 0.5):
        CvDModel.__init__(self, 'Random Forest (RF)', cvd_data, test_size)
    
    def predict(self):
        # building and fitting the classifier
        self.model = RandomForestClassifier(max_depth = 20)
        self.model.fit(self.X_train, self.y_train)
        
        # making predictions
        self.predictions = self.model.predict(self.X_test)
        
        self.c_matrix = confusion_matrix(self.y_test, self.predictions)

class CvDAdaBoost(CvDModel):
    def __init__(self, cvd_data: CvDData, test_size: float = 0.5):
        CvDModel.__init__(self, 'ADAptive BOOSTing (AB)', cvd_data, test_size)
    
    def predict(self):
        # building and fitting the classifier
        self.model = AdaBoostClassifier()
        self.model.fit(self.X_train, self.y_train)
        
        # making predictions
        self.predictions = self.model.predict(self.X_test)
        
        self.c_matrix = confusion_matrix(self.y_test, self.predictions)

class CvDKNearestNeighbors(CvDModel):
    def __init__(self, cvd_data: CvDData, test_size: float = 0.5):
        CvDModel.__init__(self, 'K-nearest neighbors (K-NN)', cvd_data, test_size)
    
    def predict(self):
        # building and fitting the classifier
        self.model = KNeighborsClassifier(n_neighbors = 10)
        self.model.fit(self.X_train, self.y_train)
        
        # making predictions
        self.predictions = self.model.predict(self.X_test)
        
        self.c_matrix = confusion_matrix(self.y_test, self.predictions)

def ROC_space(models_list):
    for model in models_list:
        tp, fp, tn, fn = model.get_values()
        fpr = (fp / (fp + tn))
        tpr = (tp / (tp + fn))
        plt.plot(fpr, tpr, 'k.')
        plt.text(fpr * (0.98), tpr * (0.93),
                 model.get_model_name().split('(')[1].split(')')[0], fontsize = 9)
    
    plt.title('ROC Space')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.axis([0, 1, 0, 1])
    plt.show()

def precision_recall_space(models_list):
    for model in models_list:
        model_scores = model.get_metrics()
        plt.plot(model_scores['recall'], model_scores['precision'], 'k.')
        plt.text(model_scores['recall'] * (0.98), model_scores['precision'] * (0.93),
                 model.get_model_name().split('(')[1].split(')')[0], fontsize = 9)
    
    plt.title('Precision-Recall Space')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.axis([0, 1, 0, 1])
    plt.show()
