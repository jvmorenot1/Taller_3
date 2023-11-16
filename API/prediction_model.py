from joblib import load
import pandas as pd
import shap

class PredictionModel:

    def __init__(self, model_version):
        if model_version == 1:
            self.model = load("models/churn-v1.joblib")
        else:
            self.model = load("models/churn-v2.joblib")

    def make_predictions(self, data):
        predicted = self.model.predict_proba(data)
        classesName = {
            0: "False",
            1: "True"
        }
        classes = list(map(lambda x : classesName[x],self.model.classes_))
        results = []
        # Pair together classes and their corresponding probability
        for prediction in predicted:
            result = dict(zip(classes, prediction))
            results.append(result)
        return results

    def modelFunc(self,X):
        return self.model["classifier"].predict_proba(X)[:,1]
    
    def explain_prediction(self, data, num_features):
        cols = [f.split("__")[1] for f in self.model[:-1].get_feature_names_out()]
        # Transforms input right before the classifier
        X_t = pd.DataFrame(self.model[:-1].transform(data),columns=cols)

        # Takes transformed variables and apply classifier, then calculate shap values
        explainer = shap.Explainer(self.modelFunc, X_t)
        shap_values = explainer(X_t)
        results = []

        for shap_val in shap_values.data:
            variables_cont = dict(zip(cols, shap_val))
            # Return the n elements with higher contributions
            result = dict(sorted(variables_cont.items(), key=lambda item: abs(item[1]),reverse=True)[:num_features])
            results.append(result)
        return results

