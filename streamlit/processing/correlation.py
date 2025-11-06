import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class EnergyCorrelationAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def correlation_fotovolt_hour(self):
        return self.df[['hour', 'fotovolt']].corr().iloc[0, 1]

    def heatmap_energy_vs_hour(self, save_path="heatmap_hour.png"):
        pivot = self.df.groupby('hour')[['carbune','hidro','hidrocarburi',
                                         'nuclear','eolian','fotovolt','biomasa','stocare']].mean()
        plt.figure(figsize=(10,6))
        sns.heatmap(pivot.T, cmap="YlGnBu", annot=False)
        plt.title("Heatmap energie vs ore")
        plt.savefig(save_path)
        plt.close()

    def heatmap_energy_vs_month(self, save_path="heatmap_month.png"):
        pivot = self.df.groupby('month')[['carbune','hidro','hidrocarburi',
                                          'nuclear','eolian','fotovolt','biomasa','stocare']].mean()
        plt.figure(figsize=(10,6))
        sns.heatmap(pivot.T, cmap="YlOrRd", annot=False)
        plt.title("Heatmap energie vs luni")
        plt.savefig(save_path)
        plt.close()