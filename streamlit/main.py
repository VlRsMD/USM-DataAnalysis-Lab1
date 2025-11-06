from processing.data_processor import EnergyDataProcessor
from processing.correlation import EnergyCorrelationAnalyzer
from processing.app import EnergyApp

def run_analysis():
    processor = EnergyDataProcessor("streamlit/data/data.csv")
    df = processor.df

    print("📊 Statistici descriptive pentru tipurile de energie:")
    print(processor.descriptive_stats())

    analyzer = EnergyCorrelationAnalyzer(df)
    print("Correlație între ora și fotovoltaic:", analyzer.correlation_fotovolt_hour())
    analyzer.heatmap_energy_vs_hour()
    analyzer.heatmap_energy_vs_month()

    print("Analiza finalizată. Graficele au fost generate.")
    return df


if __name__ == "__main__":
    df = run_analysis()
    app = EnergyApp(df)
    app.run()
