# STEP 1: Import main library
import pandas as pd
import plotly_express as px
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# STEP 2: Page Setting
# st.set_page_config(
#     page_title="Social App",
#     page_icon=":file-bar-graph:",
# )
#
# # STEP 3: Page Setting
# st.title("Main Page")

# STEP 4: MENU BAR
with st.sidebar:
    selected = option_menu(
        menu_title=None, #required, you hide menu title None
        options=['Home', 'Facebook', 'Twitter', 'Linked', 'Contact'],
        #Optional you can add icon menu
        #https://icons.getbootstrap.com/
        icons=['house','facebook','twitter','linkedin','envelope'],
        menu_icon='cast',
        default_index=0
    )
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Facebook":
    st.title(f"You have selected {selected}")
if selected == "Twitter":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")
# # Create page
# # 1
# if "options" not in st.session_state:
#     st.session_state['options'] = ""
#
# options = st.text_input('Input a text here', st.session_state['options'])
# submit = st.button("Submit")
# if submit:
#     st.session_state["options"] = options
#     st.write('You have enterd:', options)
