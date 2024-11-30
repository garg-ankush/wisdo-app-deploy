from insert_bq_data import insert_data
import streamlit as st # type: ignore
import time

st.title('Insert data into Bigquery Example')

# Text input
user_input_1 = st.number_input(
    label='Input a number',
    value=1,
    step=1
)
user_input_2 = st.text_input(
    label='Input text', 
    placeholder='Type or paste your text here...'
)

# Classification button
if st.button('Insert', type='primary'):
    if user_input_1 and user_input_2:
        rows_to_insert = [{
                "ID": round(time.time()),
                "input_1": user_input_1,
                "input_2": user_input_2
            }]
        try:
            insert_data(data=rows_to_insert)
            # Success message
            st.success('Insert Complete!')
            
        except Exception as e:
            st.error(f'An error occurred: {str(e)}')
    else:
        st.warning('Please fill in the input fields before inserting.')