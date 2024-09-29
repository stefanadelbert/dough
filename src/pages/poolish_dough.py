import streamlit as st

st.set_page_config(
    page_title="Poolish Pizza Dough",
    page_icon="🍕",
)


st.title("🍕 Poolish Pizza Dough")

with st.expander("Instructions", expanded=False):
    st.markdown(
        """
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
    """
    )

# User input
dough_ball_count = st.number_input(
    "Number of dough balls", value=4, min_value=1, step=1
)
dough_ball_size = st.number_input(
    "Dough ball size in grams",
    value=250,
    min_value=50,
    step=25,
    help='250g makes a 10" base',
)

dough_weight = dough_ball_size * dough_ball_count

hydration_help = """\
- 50% would be very dry
- 65% is a good middle ground
- 70% is quite wet and recommended for Neopolitan style
- 80% would be very wet and hard to work with\
"""
dough_hydration = st.slider(
    "Hydration",
    value=65,
    min_value=50,
    max_value=80,
    step=1,
    format="%d%%",
    help=hydration_help,
)
salt_percentage = st.slider(
    "Salt percentage",
    value=2.5,
    min_value=1.0,
    max_value=3.0,
    step=0.1,
    format="%f%%",
    help="Salt adds flavour and is quite subjective.",
)
poolish_weight = st.slider(
    "Poolish weight",
    key="poolish_weight",
    value=st.session_state.get("poolish_weight", dough_weight / 2),
    min_value=0.0,
    max_value=float(dough_weight),
    step=50.0,
    format="%fg",
    help="",
)

poolish_flour_weight = poolish_weight / 2
poolish_water_weight = poolish_weight / 2

flour_weight = dough_weight / (1 + dough_hydration / 100 + salt_percentage / 100)
remaining_flour_weight = flour_weight - poolish_flour_weight
water_weight = flour_weight * dough_hydration / 100
remaining_water_weight = water_weight - poolish_water_weight
salt_weight = flour_weight * salt_percentage / 100

if any(x < 0 for x in [remaining_flour_weight, remaining_water_weight]):
    st.warning("Too much poolish!", icon="⚠️")


st.markdown(
    f"""
```
{dough_ball_count} balls x {dough_ball_size}g = {dough_weight:.0f}g at {dough_hydration}% hydration
```"""
)

col1, col2 = st.columns(2)
col1.markdown(
    f"""
#### Poolish
|Ingredient|Weight|
|---|---|
|Poolish flour|{poolish_flour_weight:.0f}g|
|Poolish water|{poolish_water_weight:.0f}g|
"""
)
col2.markdown(
    f"""
#### Bulk ferment
|Ingredient|Weight|
|---|---|
|Flour|{remaining_flour_weight:.0f}g|
|Water|{remaining_water_weight:.0f}g|
|Salt |{salt_weight:.0f}g|
"""
)
