import pandas as pd
import streamlit as st
import numpy as np
from narwhals.stable.v1 import DataFrame

st.write("# My own Chart")

chart_data=pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)