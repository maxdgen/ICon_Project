import data
import models

if __name__ == '__main__':
    cvd_data = data.CvDData()
    
    # plotting data graphs
    cvd_data.plot_heatmap()
    cvd_data.plot_cardiovascular_disease()
    cvd_data.plot_age()
    cvd_data.plot_gender()
    cvd_data.plot_smoke()
    
    # Decision Tree (DT) model to predict cardiovascular disease
    dt_model = models.CvDDecisionTree(cvd_data)
    dt_model.predict()
    dt_model.plot_confusion_matrix()
    dt_model.metrics_calculation()
    dt_model.print_metrics()
    
    # Logistic Regression (LR) model to predict cardiovascular disease
    lr_model = models.CvDLogisticRegression(cvd_data)
    lr_model.predict()
    lr_model.plot_confusion_matrix()
    lr_model.metrics_calculation()
    lr_model.print_metrics()
    
    # Support Vector Machine (SVM) model to predict cardiovascular disease
    svm_model = models.CvDSupportVectorMachine(cvd_data)
    svm_model.predict()
    svm_model.plot_confusion_matrix()
    svm_model.metrics_calculation()
    svm_model.print_metrics()
    
    # Random Forest (RF) model to predict cardiovascular disease
    rf_model = models.CvDRandomForest(cvd_data)
    rf_model.predict()
    rf_model.plot_confusion_matrix()
    rf_model.metrics_calculation()
    rf_model.print_metrics()
    
    # ADAptive BOOSTing (AB) model to predict cardiovascular disease
    ab_model = models.CvDAdaBoost(cvd_data)
    ab_model.predict()
    ab_model.plot_confusion_matrix()
    ab_model.metrics_calculation()
    ab_model.print_metrics()
    
    # K-nearest neighbors (K-NN) model to predict cardiovascular disease
    knn_model = models.CvDKNearestNeighbors(cvd_data)
    knn_model.predict()
    knn_model.plot_confusion_matrix()
    knn_model.metrics_calculation()
    knn_model.print_metrics()
    
    # Precision-Recall Space and ROC Space to comparate models
    models_list = [dt_model, lr_model, svm_model, rf_model, ab_model, knn_model]
    models.ROC_space(models_list)
    models.precision_recall_space(models_list)