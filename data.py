import matplotlib.pyplot as plt
import pandas as pd
from seaborn.matrix import heatmap

class CvDData:
    def __init__(self):
        self.data = pd.read_csv('cardio_train.csv', sep = ';').drop(labels = 'id', axis = 1)
        
        # converting ages from days to years
        self.data['age'] = self.data['age'] / 365
        self.data['age'] = self.data['age'].astype('int')
    
    def get_data(self):
        return self.data
    
    def get_dimension(self):
        return len(self.data.columns)
    
    def get_cardio_averages(self):
        averages = {}
        positives = self.data[self.data['cardio'] == 1]
        
        averages['systolic'] = int(positives['ap_hi'].mean())
        averages['diastolic'] = int(positives['ap_lo'].mean())
        # determination of the BMI (Body Mass Index)
        weights = self.data['weight']
        heights = (self.data['height'] / 100)
        BMI = weights / (heights * heights)
        averages['BMI'] = BMI.mean()
        
        return averages
    
    def get_training_data(self):
        X = self.data.drop(columns = 'cardio')
        y = self.data['cardio']
        return X, y
    
    def plot_cardiovascular_disease(self):
        plt.style.use('seaborn-dark')
        self.data['cardio'].value_counts(sort = False).plot.bar(title = 'Cardiovascular disease', rot = 0)
        plt.show()
        
    def plot_gender(self):
        plt.style.use('seaborn-dark')
        self.data['gender'].value_counts(sort = False).plot.bar(title = 'Genders', rot = 0)
        plt.show()
        
    def plot_age(self):
        plt.style.use('seaborn-dark')
        ages = []
        
        for next_age in range(0, 100, 10):
            for age in self.data['age']:
                if age >= next_age and age <= (next_age + 9):
                    interval = '%d-%d' % (next_age, (next_age + 9))
                    ages.append(interval)
        pd.DataFrame(ages).value_counts(sort = False).plot.bar(title = 'Ages', xlabel = 'Age ranges', rot = 0)
        plt.show()
    
    def plot_smoke(self):
        plt.style.use('seaborn-dark')
        self.data['smoke'].value_counts(sort = False).plot.bar(title = 'Smokers', rot = 0)
        plt.show()
    
    def plot_heatmap(self):
        heatmap(self.data.corr(), annot = True)
        plt.show()