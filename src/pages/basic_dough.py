import textwrap

import streamlit as st

from instructions import INGREDIENTS, TIPS, HYDRATION_HELP, DOUGHBALL_SIZE_HELP


st.set_page_config(
    page_title="Basic Pizza Dough",
    page_icon="🍕",
)

st.title("🍕 Basic Pizza Dough")

METHOD = textwrap.dedent("""
    ### Method

    - Combine the water (tepid, like 25°C) and yeast and stir well
        - add a few grams of honey or raw sugar to kickstart the yeast
        - allow to sit for a few mins until the yeast starts frothing
            - if the mixture doesn't froth, you know your yeast is no good
    - Mix flour and salt well (a whisk is good for this)
    - Combine it all together and mix until it's all well incorporated
    - Turn on a flat surface shape into a ball, coat with olive oil and cover
      - you could ["stretch and fold"](https://www.youtube.com/watch?v=mwtTZK7_t08) the dough a few times
      - don't use more flour as this alters the four-water ratio
      - use slightly wet hands to work with the dough
      - a dough scraper makes working with the much easier
      - simply cover with the mixing bowl
    - rest for 15 mins (repeat a few times)
      - the dough should already be far smoother and a little supple
      - stretch and fold a few times
      - shape into a ball and lightly coat with olive oil
    - rest in the fridge in something air tight (to prevent drying out)
      - 8-12 hours is good
    - remove from the fridge and warm to room temperature over an hour
    - divide into individual dough balls
      - light coating of olive oil
      - cover in cling film and then tea towel
    - rest for an hour or so and then bake
""").strip()

with st.expander("📖 Instructions", expanded=False):
    st.markdown(INGREDIENTS)
    st.markdown(METHOD)
    st.markdown(TIPS)

# User input
dough_ball_count = st.number_input(
    "Number of dough balls", value=4, min_value=1, step=1
)
dough_ball_size = st.number_input(
    "Dough ball size in grams",
    value=250,
    min_value=50,
    step=25,
    help=DOUGHBALL_SIZE_HELP,
)
dough_hydration = st.slider(
    "Hydration",
    value=65,
    min_value=50,
    max_value=80,
    step=1,
    format="%d%%",
    help=HYDRATION_HELP,
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
