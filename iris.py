import panda as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

data = pd.read_csv('C:\Users\emtra\OneDrive\Documentos\programação\Banco de dados\Analise_de_dados\iris\iris.data')
print(data.head())