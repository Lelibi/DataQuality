import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline  # Isso garante que os gráficos sejam exibidos no Colab

class DataQuality:
    def __init__(self):
        """Inicializa a classe, solicita o nome do arquivo de dataset e gera o relatório automaticamente."""
        self.df = self.load_dataset()
        if self.df is not None:
            self.categorical_columns = self.get_categorical_columns()
            self.numeric_columns = self.get_numeric_columns()
            self.generate_report(self.categorical_columns, self.numeric_columns)

    def load_dataset(self):
        """Solicita o nome do arquivo de dataset e o carrega."""
        file_name = input("Digite o nome do arquivo do dataset (com extensão, por exemplo: dados.csv): ")
        try:
            df = pd.read_csv(file_name)
            print(f"Dataset '{file_name}' carregado com sucesso!")
            return df
        except FileNotFoundError:
            print(f"Arquivo '{file_name}' não encontrado. Verifique o nome e tente novamente.")
            return None
    
    def get_categorical_columns(self):
        """Solicita as colunas categóricas ao usuário."""
        return input("Digite as colunas categóricas separadas por vírgula: ").split(',')
    
    def get_numeric_columns(self):
        """Solicita as colunas numéricas ao usuário."""
        return input("Digite as colunas numéricas separadas por vírgula: ").split(',')

    def count_nulls(self):
        """Contagem de valores nulos por coluna."""
        if self.df is not None:
            null_counts = self.df.isnull().sum()
            print("Contagem de valores nulos por coluna:")
            print(null_counts)
            return null_counts

    def count_unique(self):
        """Contagem de valores únicos por coluna."""
        if self.df is not None:
            unique_counts = self.df.nunique()
            print("\nContagem de valores únicos por coluna:")
            print(unique_counts)
            return unique_counts
    
    def value_counts(self, categorical_columns):
        """Mostra a contagem de valores para colunas categóricas."""
        if self.df is not None:
            for col in categorical_columns:
                print(f"\nValue counts para a coluna categórica '{col}':")
                print(self.df[col].value_counts())
    
    def describe_numerics(self):
        """Mostra estatísticas descritivas para colunas numéricas."""
        if self.df is not None:
            numeric_desc = self.df.describe()
            print("\nEstatísticas descritivas para colunas numéricas:")
            print(numeric_desc)
            return numeric_desc
    
    def plot_categorical_distribution(self, categorical_columns):
        """Gera gráficos de distribuição para colunas categóricas."""
        if self.df is not None:
            for col in categorical_columns:
                plt.figure(figsize=(10, 6))
                sns.countplot(data=self.df, x=col)
                plt.title(f"Distribuição da coluna categórica: {col}")
                plt.xticks(rotation=45)
                plt.show()  # Garantir que o gráfico seja mostrado
    
    def plot_numeric_distribution(self, numeric_columns):
        """Gera gráficos de distribuição para colunas numéricas."""
        if self.df is not None:
            for col in numeric_columns:
                plt.figure(figsize=(10, 6))
                sns.histplot(self.df[col], kde=True)
                plt.title(f"Distribuição da coluna numérica: {col}")
                plt.show()  # Garantir que o gráfico seja mostrado
    
    def generate_report(self, categorical_columns, numeric_columns):
        """Gera um relatório completo com todas as análises."""
        if self.df is not None:
            print("===== Relatório de Qualidade de Dados =====")
            self.count_nulls()
            self.count_unique()
            self.value_counts(categorical_columns)
            self.describe_numerics()
            self.plot_categorical_distribution(categorical_columns)
            self.plot_numeric_distribution(numeric_columns)
            print("===== Fim do Relatório =====")
