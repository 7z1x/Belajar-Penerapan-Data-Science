import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
import warnings
warnings.filterwarnings("ignore")

def run_prediction():

    df = pd.read_csv('employee_data.csv')

    label = df['Attrition'].fillna(df['Attrition'].mode()[0])
    df_features = df.drop(columns=['Attrition'])
    encoded_features = pd.get_dummies(df_features)
    encoded_features.columns = [col.replace('_', ' ').title() for col in encoded_features.columns]

    normalizer = StandardScaler()
    normalized_data = normalizer.fit_transform(encoded_features)

    balancer = SMOTE(random_state=42)
    x_balanced, y_balanced = balancer.fit_resample(normalized_data, label)

    model_path = 'model_attrition_xgboost.pkl'
    trained_model = joblib.load(model_path)
    hasil_prediksi = trained_model.predict(normalized_data)

    df['Attrition Prediction'] = hasil_prediksi
    df.columns = [col.replace('_', ' ').title() for col in df.columns]

    save_path = 'predicted_attrition.csv'
    df.to_csv(save_path, index=False)
    print(f"Hasil prediksi disimpan di: {save_path}")

if __name__ == '__main__':
    run_prediction()
