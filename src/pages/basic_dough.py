import streamlit as st

st.set_page_config(
    page_title="Basic Pizza Dough",
    page_icon="🍕",
)

st.title("🍕 Basic Pizza Dough")

with st.expander("📖 Instructions", expanded=False):
    st.markdown(
        """
    ### Hydration
    The lower the hydration, the drier the dough. The drier the dough, the crispier the base. The wetter the dough, the lighter and chewier the base, but the easier it will burn.
    - 50% would be very dry
    - 65% is a good middle ground
    - 70% is quite wet and recommended for Neopolitan style
    - 80% would be veyr wet and hard to work with

    ### Preparation

    ##### Resting time
    The longer the dough rests, the softer the raw flour becomes and the easier it becomes to digest.

    ### Ingredients

    ⚠️ Use strong flour (W 280-330) and non-iodised salt. See _W Index_ for more details. The stronger the flour the longer it can ferment and remain strong and elastic. Dough from weak flour will fall apart

    ### References

    📝 See https://www.gigacalculator.com/calculators/pizza-dough-calculator.php to check.
    """
    )

# User input
dough_ball_count = st.number_input(
    "Number of dough balls", value=4, min_value=1, step=1
)
dough_ball_size = st.number_input(
    "Dough ball size in grams", value=250, min_value=50, step=25, help="250g makes a 10\" base"
)
hydration_help = """\
- 50% would be very dry
- 65% is a good middle ground
- 70% is quite wet and recommended for Neopolitan style
- 80% would be very wet and hard to work with\
"""
dough_hydration = st.slider(
    "Hydration", value=65, min_value=50, max_value=80, step=1, format="%d%%", help=hydration_help
)
salt_percentage = st.slider(
    "Salt percentage", value=2.5, min_value=1.0, max_value=3.0, step=0.1, format="%f%%", help="Salt adds flavour and is quite subjective."
)

# Calculations
dough_weight = dough_ball_size * dough_ball_count
flour_weight = dough_weight / (1 + dough_hydration / 100 + salt_percentage / 100)
water_weight = flour_weight * dough_hydration / 100
salt_weight = flour_weight * salt_percentage / 100

st.markdown(f"""
```
{dough_ball_count} balls x {dough_ball_size}g = {dough_weight:.0f}g at {dough_hydration}% hydration
```

|Ingredient|Weight|
|---|---|
|Flour|{flour_weight:.0f}g|
|Water|{water_weight:.0f}g|
|Salt |{salt_weight:.0f}g|
""")
