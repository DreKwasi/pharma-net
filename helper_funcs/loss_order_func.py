import streamlit as st


def view_loss_orders():
    pass


def record_loss_order():
    st.title("Order Entry Form")
    placeholder = st.empty()
    with placeholder.form("Record Order"):
        facility_location = st.text_input("Facility Location")
        client_type = st.selectbox(
            "Client Type",
            options=["Guest", "Regular"],
            help="Is Client Guest or Regular",
        )
        form_col1, form_col2 = st.columns([1,1])
        product_name = form_col1.selectbox(
            "Product Name",
            options=("Paracetamol", "Augmentin", "Amoxyl"),
            help="Name of the Product (Brand Name is Best)",
        )
        requested_quantity = form_col2.number_input(
            "Requested Quantity", min_value=1, step=1, help="Packs Are With Respect to Product Type"
        )
        dosage_form = st.selectbox(
            "Dosage Form",
            options=[""],
            help="Tablets, Caplets etc.",
        )
        form_col3, form_col4 = st.columns([1,1])
        
        medication_type = form_col3.selectbox(
            "Medication Type",
            options=["Herbals", "Orthodox"],
            help="Herbals or Orthodox",
        )

        brand = form_col4.text_input("Brand")
        info = st.text_area("Additional Comments")
        date = st.date_input("Upload Date")
        button = st.form_submit_button("Submit")


def edit_form():
    pass
