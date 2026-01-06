import os 
import sys
import numpy as np
import pandas as pd 
import seaborn as sns 
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from imblearn.over_sampling import SMOTE
import warnings
warnings.filterwarnings("ignore")

from sklearn.metrics import accuracy_score,roc_auc_score  ,confusion_matrix,classification_report,recall_score,f1_score,precision_score

from InsurenceClaim.Config.ConfigurationManagerConfig import ConfigurationManagerConfig
from InsurenceClaim.Entity.Config_Entity import *

from InsurenceClaim import logger

class DataModel:
    def __init__(self,config:DataModelConfig):
        self.config=config
    def DataModel(self,x_train,x_test,y_train,y_test):
        logger.info(f"++++++++++++++++++++ Define Model and Hyperparameters ++++++++++++++++++++")
        models={
            "LogisticRegression":LogisticRegression(solver=self.config.Logistic_Regression.solver,
                                                    max_iter=self.config.Logistic_Regression.max_iter,
                                                    class_weight=self.config.Logistic_Regression.class_weight,
                                                    random_state=self.config.Logistic_Regression.random_state,
                                                    C=self.config.Logistic_Regression.c
                                                    ),
            "RandomForestClassifier":RandomForestClassifier(n_estimators=self.config.Random_Forest.n_estimators,
                                                            max_depth=self.config.Random_Forest.max_depth,
                                                            class_weight=self.config.Random_Forest.class_weight,
                                                            random_state=self.config.Random_Forest.random_state
                                                            ),
            "DecisionTreeClassifier":DecisionTreeClassifier(class_weight=self.config.Decision_Tree.class_weight,
                                                            random_state=self.config.Decision_Tree.random_state,
                                                            max_depth=self.config.Decision_Tree.max_depth),
            "KNeighborsClassifier":KNeighborsClassifier(n_neighbors=self.config.KNeighbors.n_neighbors),
            "SVM":SVC(kernel=self.config.SVM.kernal,
                      probability=self.config.SVM.probability,
                      class_weight=self.config.SVM.class_weight,
                      random_state=self.config.SVM.random_state),
            "GradientBoostingClassifier":GradientBoostingClassifier(random_state=self.config.Gradient_Boosting.random_state),
            "AdaBoostClassifier":AdaBoostClassifier(random_state=self.config.AdaBoost.random_state),
            "XGBoostClaasifier":XGBClassifier(scale_pos_weight=(len(y_train[y_train==0]) / len(y_train[y_train==1])),
                                              use_label_encoder=self.config.XGBoost.use_label_encoder,
                                              eval=self.config.XGBoost.eval_metric,
                                              random_state=self.config.XGBoost.random_state
                                              ),
            "LightGBMClassifier":LGBMClassifier(random_state=self.config.LightGBM.random_state,
                                                class_weight=self.config.LightGBM.class_weight),
            "CatBoostClassifier":CatBoostClassifier(verbose=self.config.CatBoost.verbose,
                                                    random_state=self.config.CatBoost.random_state)


        }
        metrics_dict = {}
        best_model = None
        best_model_name = None
        best_score = -1

        for name,model in models.items():
            logger.info(f"...Training {name}....")
            model.fit(x_train,y_train)
            preds=model.predict(x_test)
            probs=model.predict_proba(x_test)[:,1]

            acc=accuracy_score(y_test,preds)
            auc=roc_auc_score(y_test,probs)
            rec=recall_score(y_test,preds)
            f1=f1_score(y_test,preds)
            prec = precision_score(y_test, preds)
            

            logger.info(f"\n📊 {name} Performance:")
            logger.info(f"Accuracy: {acc:.4f}")
            logger.info(f"ROC-AUC: {auc:.4f}")
            logger.info(classification_report(y_test, preds))

            cm = confusion_matrix(y_test, preds)
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title(f"{name} Confusion Matrix")
            plt.xlabel("Predicted"); plt.ylabel("Actual")
            plt.show()
            logger.info(f" Name {name} \n    Accuracy Score : {acc} \n    ROC AUC Score : {auc}  ")
            logger.info(f" ++++++++++++++++++ Saving the Metrics ++++++++++++++++++ ")


            metrics_dict[name] = {
                "Accuracy": acc,
                "Precision": prec,
                "Recall": rec,
                "F1-Score": f1,
                "ROC-AUC": auc
            }

            logger.info(f"{name} Performance:")
            logger.info(f"  Accuracy: {acc:.4f}")
            logger.info(f"  Precision: {prec:.4f}")
            logger.info(f"  Recall: {rec:.4f}")
            logger.info(f"  F1: {f1:.4f}")
            logger.info(f"  ROC-AUC: {auc:.4f}")

            # Weighted average score (can tweak)
            weighted_score = (0.4 * auc) + (0.3 * f1) + (0.3 * acc)
            if weighted_score > best_score:
                best_model = model
                best_model_name = name
                best_score = weighted_score


             
        logger.info("\n Best Model Selected:", best_model_name)
        logger.info(f"Weighted Score: {best_score:.4f}")

        #best_model_path = Path(self.config.root_dir)  f"{best_model_name.lower()}_production.pkl"
        with open(self.config.root_dir, "wb") as f:
            pickle.dump(best_model, f)

        print(f" Best Model Saved to: {self.config.root_dir}")

            # ===============================
            # STEP 7: Save Metrics
            # ===============================
        metrics_dict["Best_Model"] = best_model_name
        metrics_dict["Best_Weighted_Score"] = best_score
        logger.info(metrics_dict)

             



       







