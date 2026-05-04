import streamlit as st
import pandas as pd

# 1. Setup & Design
st.set_page_config(page_title="AI Moonshot Predictor", page_icon="💿")
st.title("📀 AI Album Decay Predictor")
st.markdown("---")

# 2. Load the Data
df = pd.read_csv("data.csv")

# 3. Search Bar
search_query = st.text_input("🔍 Search for an album (e.g., SOS, GNX):")

if search_query:
    # Filter data based on search
    match = df[df['Album'].str.contains(search_query, case=False)]
    
    if not match.empty:
        album_data = match.iloc[0] # Take the first match
        
        st.header(f"Results for {album_data['Album']}")
        
        # 4. Display AI Ratings
        col1, col2, col3 = st.columns(3)
        col1.metric("Innovation", f"{album_data['Innovation']}/10")
        col2.metric("Marketability", f"{album_data['Marketability']}/10")
        col3.metric("Production", f"{album_data['Production']}/10")
        
        st.subheader(f"AI Prediction: {album_data['Prediction']} Weeks in Top 10")

        # 5. The "Metacritic Reviews" Expander
        with st.expander("📄 View Metacritic reviews used in this calculation"):
            st.write(album_data['Review_Text'])
            st.info("The AI analyzed the linguistic sentiment of these specific reviews to generate the scores above.")

        # 6. The "Reveal Actual Weeks" Button
        if st.button("👁️ Reveal Actual Billboard Weeks"):
            st.write(f"### Actual Result: **{album_data['Actual_Weeks']} Weeks**")
            
            # Show a comparison
            diff = album_data['Actual_Weeks'] - album_data['Prediction']
            if diff > 0:
                st.write(f"Note: The AI underestimated this album by {diff} weeks.")
            else:
                st.write(f"Note: The AI overestimated this album by {abs(diff)} weeks.")
    else:
        st.error("No album found with that name. Try 'SOS' or 'GNX'.")
else:
    st.info("Enter an album name above to begin the AI analysis.")

st.markdown("---")
st.caption("Project: AI Moonshot | Tool: Gemini + Streamlit")
