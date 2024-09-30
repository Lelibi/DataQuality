import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataQuality:
    def __init__(self, file_name):
        """Inicializa a classe e carrega o dataset"""
        self.df = self.load_dataset(file_name)
        if self.df is not None:
            self.categorical_columns, self.numeric_columns = self.identify_columns()
            self.generate_report()

    def load_dataset(self, file_name):
        """Carrega o dataset a partir de um arquivo CSV."""
        try:
            df = pd.read_csv(file_name)
            print(f"Dataset '{file_name}' carregado com sucesso!")
            return df
        except FileNotFoundError:
            print(f"Arquivo '{file_name}' não encontrado. Verifique o nome e tente novamente.")
            return None

    def identify_columns(self):
        """Identifica colunas categóricas e numéricas automaticamente."""
        categorical_columns = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        numeric_columns = self.df.select_dtypes(include=['number']).columns.tolist()

        print(f"Colunas categóricas identificadas: {categorical_columns}")
        print(f"Colunas numéricas identificadas: {numeric_columns}")

        return categorical_columns, numeric_columns

    def count_nulls(self):
        """Contagem de valores nulos por coluna."""
        null_counts = self.df.isnull().sum()
        print("\n===== Contagem de valores nulos por coluna =====")
        print(null_counts)
        return null_counts

    def count_unique(self):
        """Contagem de valores únicos por coluna."""
        unique_counts = self.df.nunique()
        print("\n===== Contagem de valores únicos por coluna =====")
        print(unique_counts)
        return unique_counts

    def value_counts(self):
        """Aplica .value_counts() nas colunas categóricas."""
        print("\n===== Value counts nas colunas categóricas =====")
        for col in self.categorical_columns:
            print(f"\nValue counts para a coluna '{col}':")
            print(self.df[col].value_counts())

    def describe_numerics(self):
        """Mostra estatísticas descritivas para colunas numéricas usando .describe()."""
        print("\n===== Estatísticas descritivas para colunas numéricas =====")
        numeric_desc = self.df.describe()
        print(numeric_desc)
        return numeric_desc

    def plot_categorical_distribution(self):
        """Gera gráficos de distribuição para colunas categóricas."""
        print("\n===== Gráficos de distribuição para colunas categóricas =====")
        for col in self.categorical_columns:
            plt.figure(figsize=(10, 6))
            sns.countplot(x=self.df[col], palette='Set2')
            plt.title(f'Distribuição da coluna categórica: {col}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    def plot_numeric_distribution(self):
        """Gera gráficos de distribuição para colunas numéricas."""
        print("\n===== Gráficos de distribuição para colunas numéricas =====")
        for col in self.numeric_columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.df[col], kde=True, color='blue')
            plt.title(f'Distribuição da coluna numérica: {col}')
            plt.tight_layout()
            plt.show()

    def generate_report(self):
        """Gera o relatório completo de contagem de nulos, únicos, value_counts, describe e gráficos de distribuição."""
        print("\n===== Gerando Relatório de Qualidade de Dados =====")
        self.count_nulls()
        self.count_unique()
        self.value_counts()
        self.describe_numerics()
        self.plot_categorical_distribution()
        self.plot_numeric_distribution()
        print("\n===== Fim do Relatório =====")

# Exemplo de uso
# dq = DataQuality('seu_arquivo.csv')
