import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class EnergyApp:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def run(self):
        st.title("⚡ Analiza Interactivă a Energiei")

        start_date = st.sidebar.date_input("Start date", self.df['date'].min())
        end_date = st.sidebar.date_input("End date", self.df['date'].max())
        energy_types = st.sidebar.multiselect(
            "Select energy types",
            ['carbune','hidro','hidrocarburi','nuclear','eolian','fotovolt','biomasa','stocare'],
            default=['carbune','hidro','nuclear']
        )

        df_filtered = self.df[
            (self.df['date'] >= pd.to_datetime(start_date)) &
            (self.df['date'] <= pd.to_datetime(end_date))
        ]

        st.subheader("📊 Evoluția tipurilor de energie selectate")
        st.line_chart(df_filtered.set_index('date')[energy_types])

        st.subheader("📑 Date filtrate (primele 10 rânduri)")
        st.dataframe(df_filtered.head(10))

        st.subheader("📈 Vizualizări avansate")

        if st.checkbox("Producția lunară pe tipuri"):
            monthly = self.df.groupby(['year','month'])[['carbune','hidro','hidrocarburi',
                                                         'nuclear','eolian','fotovolt','biomasa']].sum()
            fig, ax = plt.subplots(figsize=(12,6))
            monthly.plot(kind="bar", stacked=True, ax=ax)
            ax.set_title("Producția lunară pe tipuri de energie")
            st.pyplot(fig)

        if st.checkbox("Sold zilnic (2024-2025)"):
            daily = self.df.groupby(self.df['date'].dt.date)['sold'].sum()
            fig, ax = plt.subplots(figsize=(12,6))
            daily.plot(ax=ax)
            ax.set_title("Sold zilnic 2024-2025")
            st.pyplot(fig)

        if st.checkbox("Seria temporală pe sold"):
            fig, ax = plt.subplots(figsize=(12,6))
            ax.plot(self.df['date'], self.df['sold'], color='red')
            ax.set_title("Seria temporală pe sold")
            st.pyplot(fig)

        if st.checkbox("Peek-ul producției pe ore"):
            hourly = self.df.groupby('hour')['productie'].mean()
            fig, ax = plt.subplots(figsize=(10,6))
            hourly.plot(kind="bar", ax=ax)
            ax.set_title("Peek-ul producției pe ore")
            st.pyplot(fig)

        if st.checkbox("Consumul mediu pe zilele săptămânii"):
            weekly = self.df.groupby('weekday')['consum'].mean()
            order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
            weekly = weekly.reindex(order)
            fig, ax = plt.subplots(figsize=(10,6))
            weekly.plot(kind="bar", ax=ax)
            ax.set_title("Consumul mediu pe zilele săptămânii")
            st.pyplot(fig)

        if st.checkbox("Producția medie lunară 2024-2025"):
            monthly = self.df.groupby(['year','month'])['productie'].mean()
            fig, ax = plt.subplots(figsize=(12,6))
            monthly.plot(ax=ax)
            ax.set_title("Producția medie lunară 2024-2025")
            st.pyplot(fig)

        if st.checkbox("Comparare consum vs producție"):
            fig, ax = plt.subplots(figsize=(12,6))
            ax.plot(self.df['date'], self.df['consum'], label="Consum")
            ax.plot(self.df['date'], self.df['productie'], label="Producție")
            ax.legend()
            ax.set_title("Comparare consum și producție")
            st.pyplot(fig)
