import os
import numpy as np

from datetime import datetime
from dateutil.relativedelta import relativedelta

from data_generator import generate_advisors, generate_commodities, generate_export_wins

if __name__ == "__main__":
    np.random.seed(seed=42)

    commodities_data = {
        "metals": ["gold", "silver", "bronze", "steel", "lead", "titanium"],
        "alcohol": ["gin", "rum", "vodka", "whiskey", "brandy"],
        "fruit": ["apples", "bananas", "lemons", "limes", "cherries"],
        "vegetables": ["carrots", "cabbages", "turnips", "potatoes"],
        "animals": ["chickens", "cows", "goats", "pigs", "zebras"],
    }
    commodities_cats_frequency = ["metals"] * 15 + ["alcohol"] * 5 + ["fruit"] * 25 + ["vegetables"] * 20 + ["animals"] * 25

    gen_id = "starter"
    output_location = f"./input_data/{gen_id}"
    os.makedirs(output_location, exist_ok=True)

    gen_advisors = generate_advisors(output_location, 137)
    commodity_id_lookup = generate_commodities(output_location, commodities_data)

    end_date = datetime.today()
    delta = relativedelta(months=3)
    start_date = end_date - delta

    generate_export_wins(output_location, gen_advisors, commodities_data,
                          commodity_id_lookup, commodities_cats_frequency,
                          start_date, end_date)
