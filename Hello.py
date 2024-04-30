# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('connections.mysql', type='sql')

# Perform query.
df = conn.query('SELECT first_name from user;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.first_name}")