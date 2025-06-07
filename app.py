import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from sqlalchemy import create_engine
import psycopg2
from pandasql import sqldf

# Load model
model = joblib.load("Best_model_gb.pkl")

# Page config
st.set_page_config(
    page_title="🏠 House Price Predictor",
    page_icon="💰",
    layout="wide",
)

# For database

# DB_USER = 'postgres'
# DB_PASS = 'password'
# DB_HOST = 'host'
# DB_PORT = 5432
# DB_NAME = 'db_name'



# # Connect to database
# engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


# Read from the cleaned data table
# @st.cache_data(ttl=300)
# def load_data():
#     query = "SELECT * FROM house_data"  # Replace with actual table name
#     return pd.read_sql(query, engine)



section = st.sidebar.radio("Navigate", ["🏠 Price Prediction", "📊 Dashboard", "🧮 SQL Playground"])

if section == "🏠 Price Prediction":
        # Your existing prediction UI (inputs + model)
        st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏡 Smart House Price Predictor</h1>", unsafe_allow_html=True)
        
        st.markdown("---")

    # Input Section
        st.subheader("📋 Enter Property Details")

        col1, col2 = st.columns(2)

        with col1:
            overall_qual = st.slider("🏗️ Overall Quality (1-10)", 1, 10, 5)
            total_sf = st.number_input("📏 Total SF", min_value=100, value=1500)
            garage_cars = st.slider("🚗 Garage Capacity (Cars)", 0, 5, 2)
            gr_liv_area = st.number_input("🛋️ Ground Living Area", min_value=100, value=1500)
            central_air = st.selectbox("🌬️ Central Air Conditioning", ['Yes', 'No'])
            lot_area = st.number_input("🌳 Lot Area (sq ft)", min_value=500, value=8000)
            year_remod = st.number_input("🛠️ Year Remodeled", min_value=1950, max_value=2025, value=2000)
            garage_area = st.number_input("🏚️ Garage Area (sq ft)", min_value=0, value=500)

        with col2:
            age = st.number_input("📅 House Age", min_value=0, max_value=200, value=30)
            garage_yr_blt = st.number_input("🔧 Garage Year Built", min_value=1900, max_value=2025, value=2000)
            bsmt_fin_sf_1 = st.number_input("🏠 Finished Basement SF 1", min_value=0, value=400)
            bsmt_unf_sf = st.number_input("🏗️ Unfinished Basement SF", min_value=0, value=200)
            year_built = st.number_input("🧱 Year Built", min_value=1900, max_value=2025, value=1995)
            overall_cond = st.slider("📊 Overall Condition (1-10)", 1, 10, 5)
            first_flr_sf = st.number_input("🏢 1st Floor SF", min_value=100, value=1200)
            lot_frontage = st.number_input("🚪 Lot Frontage", min_value=20, value=70)

    # Predict button
        st.markdown("---")
        if st.button("🔍 Predict House Price"):
        # Prepare input
            input_data = pd.DataFrame({
                'Overall Qual': [overall_qual],
                'Total SF': [total_sf],
                'Garage Cars': [garage_cars],
                'Gr Liv Area': [gr_liv_area],
                'Central Air': ['Y' if central_air == 'Yes' else 'N'],
                'Lot Area': [lot_area],
                'Year Remod/Add': [year_remod],
                'Garage Area': [garage_area],
                'age': [age],
                'Garage Yr Blt': [garage_yr_blt],
                'BsmtFin SF 1': [bsmt_fin_sf_1],
                'Bsmt Unf SF': [bsmt_unf_sf],
                'Year Built': [year_built],
                'Overall Cond': [overall_cond],
                '1st Flr SF': [first_flr_sf],
                'Lot Frontage': [lot_frontage]
            })

            # Prediction
            prediction = model.predict(input_data)[0]

            st.markdown(
                f"""
                <div style='background-color: #e6f4ea; padding: 30px; border-radius: 12px; text-align: center;'>
                    <h2 style='color: #2e7d32;'>🏡 Estimated Selling Price:</h2>
                    <h1 style='color: #1b5e20;'>💰 ${prediction:,.0f}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

elif section == "📊 Dashboard":
    # df_db = load_data()
    df = pd.read_csv("AmesHousing_Cleaned.csv")
    # st.write("### Raw Data", df.head())

    with st.sidebar:
        st.markdown("## 🧰 Dashboard Filters")
        qual_filter = st.slider("Filter by Overall Quality", 1, 10, (1, 10))
        filtered_df = df[(df['Overall Qual'] >= qual_filter[0]) & (df['Overall Qual'] <= qual_filter[1])]

    st.markdown("---")
    st.markdown("## 📊 Real Estate Data Dashboard (Live from PostgreSQL)")

    ## Summary stats
    st.markdown("### 🔢 Summary Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Price: ", f"${df["SalePrice"].mean():.0f}")
    col2.metric("Avg. Garage Area: ", f"{df['Garage Area'].mean():.0f}sq ft")
    col3.metric("Avg. Overall Quality: ", f"{df['Overall Qual'].mean():.1f}/10")


    # Price Distribution
    st.markdown("### 💵 Price Distribution")
    fig1 = px.histogram(filtered_df, x="SalePrice", nbins=30, title="Distribution of Sale Prices", color_discrete_sequence=["#4CAF50"])
    st.plotly_chart(fig1, use_container_width=True)


    # Scatter Plot: Gr Liv Area vs Sale Price
    st.markdown("### 🛋️ Living Area vs. Sale Price")
    fig2 = px.scatter(filtered_df, x="Gr Liv Area", y="SalePrice", color="Overall Qual", 
                    size="Garage Cars", hover_data=["Year Built"], title="Living Area vs. Price")
    st.plotly_chart(fig2, use_container_width=True)
      
    ## Yearly trend
    st.markdown("### 📅 Sale Price Trend by Year")
    if "Yr Sold" in df.columns:
        fig3 = px.box(filtered_df, x="Yr Sold", y="SalePrice", title="Price Trends Over the Years", color="Yr Sold")
        st.plotly_chart(fig3, use_container_width=True)


elif section == "🧮 SQL Playground":
    st.markdown("## 🧮 SQL Playground")
    st.info("Write SQL queries to explore your PostgreSQL data.")
    df = pd.read_csv("AmesHousing_Cleaned.csv")
    st.write("### Raw Data", df.head())

    default_query = "SELECT * FROM df LIMIT 5;"  # Your table name
    user_query = st.text_area("Write your SQL query below:", default_query, height=150)

    if st.button("▶️ Run Query"):
        try:
            query_df = sqldf(user_query, locals())
            st.success("✅ Query executed successfully!")
            st.dataframe(query_df)

            # visualize numeric column
            numeric_cols = query_df.select_dtypes(include='number').columns.tolist()
            if numeric_cols:
                selected_col = st.selectbox("📈 Visualize Column", numeric_cols)
                st.bar_chart(query_df[selected_col])

        except Exception as e:
            st.error(f"❌ Error: {e}")

    

