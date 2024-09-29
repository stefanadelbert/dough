import streamlit as st

st.title("🍕 Poolish Pizza Dough")

with st.expander("Instructions", expanded=False):
    st.markdown("""
    ### Preferment (Poolish)
    - flour and water
    - 3g dry yeast
    - tsp honey (optional)
    Mix water, yeast and honey and leave for 5mins. If it's foaming, your yeast is active, but if not try again with other yeast.
    Stir in flour so that all flour is wet. Cover (cling film + tea towel) and leave at room temp for 1hr. Fridge 8-16hrs - this is what makes all the difference!

    ### Bulk ferment
    Mix (gently) water with poolish and put aside. Mix salt (2-3% of total flour mass) with flour (whisk is good). Now put it all together and combine well.
    Stretch and fold several times at half hour intervals. Use water on your hands and work quickly to avoid the dough sticking. It'll be SUPER wet and sticky.
    This dough should rest for a few hours (2hrs).

    ### Shape
    Divide into dough balls and let them rest (1hr).

    ⚠️ Use strong flour (W 280-330) and non-iodised salt. See _W Index_ for more details.

    📝 See https://www.gigacalculator.com/calculators/pizza-dough-calculator.php to check.
    """)
# A user input form to capture size of dough ball in grams and number of dough balls.

dough_ball_size = st.number_input("Enter dough ball size in grams", value=250, min_value=50, step=25)
dough_ball_count = st.number_input("Enter number of dough balls", value=4, min_value=1, step=1)
dough_hydration = st.slider("Enter dough hydration", value=65, min_value=50, max_value=80, step=1, format="%d%%")
salt_percentage = st.slider("Enter salt percentage", value=2.5, min_value=1.0, max_value=3.0, step=0.1, format="%f%%")
dough_weight = dough_ball_size * dough_ball_count
flour_weight = dough_weight / (1 + dough_hydration/100)
water_weight = dough_weight - flour_weight
salt_weight = flour_weight * salt_percentage / 100
    
st.markdown(f"""
- Total dough weight: `{dough_weight:.0f}g`
- Flour weight: ``{flour_weight:.0f}g``
- Water weight: ``{water_weight:.0f}g``
- Salt weight: ``{salt_weight:.0f}g``
""")
