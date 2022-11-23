import cufflinks as cf
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Population Dashboard',
    page_icon='',
    layout='wide'
)

cf.set_config_file(sharing='public',theme='ggplot',offline=True)

dataset_url='population_total.csv'

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df_population=get_data()

df_population=df_population.dropna()
df_population=df_population.pivot(index='year',columns='country',values='population')
df_population=df_population[['Mexico','China','United States','India','Brazil']]
code=['MEX','CHN','USA','IND','BRA']


st.title('Population Dashboard')

country_filter=st.selectbox('Select Country',['Mexico','China','United States','India','Brazil'])


df_population_filter=df_population[country_filter]

max_population=np.max(df_population_filter)
growth_population_rate=df_population[country_filter].pct_change().iloc[-1]*100

placeholder=st.empty()

with placeholder.container():
    kpi1,kpi2,kpi3=st.columns(3)
    kpi1.metric(
        label='Latest population',
        value=round(max_population)
    )
    kpi2.metric(
        label='Growth rate',
        value=str(round(growth_population_rate,2))+'%'
    )
    kpi3.metric(
        label='Country',
        value=country_filter
    )


    fig1_col,fig2_col=st.columns(2)
    with fig1_col:
        st.markdown('### Year vs Population')
        chart=df_population_filter.iplot(asFigure=True, kind='line',xTitle='Year',yTitle='Population')
        st.write(chart)

    with fig2_col:
        st.markdown('### Population in 2020')
        df_population_max=df_population[df_population.index.isin([2020])]
        df_population_max=df_population_max.T
        df_population_max=df_population_max.sort_values(by=[2020],ascending=False)
        chart2=df_population_max.iplot(asFigure=True,kind='bar',xTitle='Countries',yTitle='Population')
        st.write(chart2)

    
    st.markdown('### Map Data View')
    df_population_map=df_population[df_population.index.isin([2020])]
    df_population_map=df_population_map.T
    df_population_map=df_population_map.rename(columns={2020:'2020'})
    df_population_map['code']=code
    chart3=df_population_map.iplot(asFigure=True,kind='choropleth',locations='code',z='2020',colorscale='Reds')
    st.write(chart3)
