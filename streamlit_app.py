import streamlit as st
import pandas as pd
import plotly.express as px
from src.wordcount import count_words
APP_TITLE = "MapReduce Word Count Explorer"

st.set_page_config(page_title=APP_TITLE, layout="wide")
st.markdown('''
<style>
.block-container {padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1180px;}
[data-testid="stMetricValue"] {font-size: 1.65rem;}
.small-note {color: #5f6368; font-size: 0.92rem;}
</style>
''', unsafe_allow_html=True)


st.title(APP_TITLE)
st.caption("A local simulator for the mapper/reducer logic used in Hadoop word-count coursework.")
text = st.text_area("Input text", "Big data systems process big logs, big documents, and streaming text data for analytics.", height=180)
counts = count_words(text)
df = pd.DataFrame(counts.most_common(25), columns=["word", "count"])
st.metric("Unique terms", len(counts))
st.plotly_chart(px.bar(df, x="word", y="count"), use_container_width=True)
st.dataframe(df, use_container_width=True, hide_index=True)
