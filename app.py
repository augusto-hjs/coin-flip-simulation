import streamlit as st

st.header('Flipping a coin')

number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Execute')

if start_button:
	st.write(f'Running the experiment with {number_of_trials} attempts.')

st.write('Not yet a functional app. Under development.')
