import streamlit as st
import pandas as pd

# 1. Text Elements
st.markdown('# Text Elements')

st.text('1.2. Displaying Basic Text')
st.title('This is the title')
st.header('This is the header')
st.subheader('This is the subheader')
st.text('This is the text')
st.caption('This is the caption')
st.divider()
st.write('This is the write')
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [10, 20, 30, 40]})
st.write('Display a DataFrame using st.write', df)

st.text('1.4. Displaying Markdown')
st.markdown('# This is a Markdown title')
st.markdown('## This is a Markdown header')
st.markdown('### This is a Markdown subheader')
st.markdown('this is the markdown')
st.markdown('this is ** the markdown ** ')
st.markdown('this is _the markdown_')
st.markdown('this is *the markdown*')
st.markdown('this is **_ the markdown _** ')

st.text('1.6. Displaying Formatting and Display Tools')
st.code('x=134')
st.latex(r'''a + ar + a r^2 ''')

# 2. Media Elements
st.markdown('# Media Elements')
st.text('2.1. Displaying Media Elements')

# Image (Using the working online URL from your tutorial)
st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQi0jEyMDd9&auto=format&fit=crop&w=1487&q=80', caption='Sunrise by the mountains')

# Audio (Replaced placeholder path with a live online test track)
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

# Video (Only ONE working YouTube link—no downloads needed!)
st.video('https://www.youtube.com/watch?v=X2aa5nZBZYo')
