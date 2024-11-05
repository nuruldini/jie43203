import pandas as pd
import streamlit as st

file_path = 'https://raw.githubusercontent.com/nuruldini/jie43203/refs/heads/main/onlinefoods.csv'

df = pd.read_csv(file_path)

st.write(df)
st.dataframe(df)
import numpy as np
np.corrcoef(df.Age, df.Family_size)

import numpy as np
np.cov(df.Age, df.Family_size)

chisqt = pd.crosstab(df.Marital_Status, df.Occupation, margins=True)
st.write(chisqt)

from scipy.stats import chi2_contingency
import numpy as np


value = np.array([chisqt.iloc[0][0:5].values,
                  chisqt.iloc[1][0:5].values])
st.write(chi2_contingency(value)[0:3])

df.isnull().sum()


duplicate = df.duplicated()
st.write("Duplicate rows in DataFrame:", duplicate.sum())

cleaned_df = df.drop_duplicates()

num_duplicates_removed = df.shape[0] - cleaned_df.shape[0]

duplicate = cleaned_df.duplicated()
st.write("Duplicate rows in DataFrame:", duplicate.sum())

import pandas as pd
import matplotlib.pyplot as plt



age = df['Age']


plt.figure(figsize=(8, 6))
plt.boxplot(age)
plt.title('Boxplot of Age')
plt.ylabel('Age')
plt.grid(True)
plt.show()

st.pyplot(plt.gcf())


st.button("Regenerate")
