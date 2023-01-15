import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from helper_funcs import loss_order_func


st.set_page_config(
    page_title="Form",
    page_icon="clipboard",
    initial_sidebar_state="expanded",
    layout="centered",
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

selected = option_menu(
    menu_title="",
    options=[ "Record Loss Order", "View Loss Orders",  "Edit Form"],
    orientation="horizontal",
)


if "authentication_status" in st.session_state or "username" in st.session_state:

    if st.session_state["authentication_status"]:
        if selected == "Record Loss Order":
            loss_order_func.record_loss_order()
        elif selected == "Edit Form":
            loss_order_func.edit_form()
        elif selected == "View Loss Orders":
            loss_order_func.view_loss_orders()

    elif st.session_state["authentication_status"] == False:
        st.error("Username/password is incorrect")

    elif st.session_state["authentication_status"] == None:
        st.warning("Visit Home Screen To Login or Register")


else:
    login_btn = st.button("Login")
    if login_btn:
        switch_page("Home")
    st.warning("Visit Home Page To Login or Register")
