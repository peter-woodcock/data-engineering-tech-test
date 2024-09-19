import csv
import json
import math
import os
import random
from datetime import timedelta

import numpy as np


class TradeAdvisor(object):
    def __init__(self, trade_advisor_id, trade_advisor_job_grade):
        self.trade_advisor_id = trade_advisor_id
        self.trade_advisor_grade = trade_advisor_job_grade


def generate_advisors(output_location_root, number_of_advisors, return_data=True):
    advisors = []
    with open(f'{output_location_root}/advisors.csv', mode='w') as advisors_file:
        csv_writer = csv.writer(advisors_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["advisor_id", "job_grade"])
        for cid in range(1, number_of_advisors + 1):
            advisor_id = f"TA{cid}"
            grade = random.choice(["G6","G7","SEO","HEO"])
            csv_writer.writerow([advisor_id, grade])
            if return_data:
                advisors.append(TradeAdvisor(advisor_id, grade))
    return advisors if return_data else None


def generate_commodities(output_location_root, commodities_to_generate):
    commodities_count_digits = int(math.log10(len(sum(commodities_to_generate.values(), []))) + 1)

    commodities_id_lookup = {k: {} for k, v in commodities_to_generate.items()}
    with open(f'{output_location_root}/commodities.csv', mode='w') as commodities_file:
        csv_writer = csv.writer(commodities_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["commodity_code", "commodity_description", "commodity_category"])
        index = 1
        for category in commodities_to_generate:
            for commodity in commodities_to_generate[category]:
                commodity_code = f"C{str(index).zfill(commodities_count_digits)}"
                csv_writer.writerow([commodity_code, commodity, category])
                commodities_id_lookup[category][commodity] = commodity_code
                index += 1
    return commodities_id_lookup


def generate_export_wins(output_location_root, advisors, commodities,
                          commodities_id_lookup, commodities_cats_frequency,
                          start_datetime, end_datetime):
    open_files = open_export_wins_sinks(output_location_root, start_datetime, end_datetime)
    commodities_cats_count = len(commodities.keys())
    num_days = (end_datetime - start_datetime).days
    all_days = [start_datetime + timedelta(days=d) for d in range(0, num_days + 1)]
    advisor_frequency_type = [int(num_days / 14), int(num_days / 10), int(num_days / 7), int(num_days / 5),
                               int(num_days / 4), int(num_days / 3)]

    for advisor in advisors:
        num_export_win_days = random.choice(advisor_frequency_type)
        num_cats = random.randint(1, commodities_cats_count)
        advisor_export_win_days = sorted(random.sample(all_days, num_export_win_days))
        cats = random.sample(commodities_cats_frequency, num_cats)
        for day in advisor_export_win_days:
            export_win = {
                "trade_advisor_id": advisor.trade_advisor_id,
                "export_win": generate_export_win(commodities, commodities_id_lookup, cats),
                "date_of_export_win": str(day + timedelta(minutes=random.randint(168, 1439)))
            }
            open_files[to_canonical_date_str(day)].write(json.dumps(export_win) + "\n")

    for f in open_files.values():
        f.close()


def to_canonical_date_str(date_to_transform):
    return date_to_transform.strftime('%Y-%m-%d')


def open_export_wins_sinks(output_location_root, start_datetime, end_datetime):
    root_export_wins_dir = f"{output_location_root}/export_wins/"
    open_files = {}
    days_to_generate = (end_datetime - start_datetime).days
    for next_day_offset in range(0, days_to_generate + 1):
        next_day = to_canonical_date_str(start_datetime + timedelta(days=next_day_offset))
        day_directory = f"{root_export_wins_dir}/d={next_day}"
        os.makedirs(day_directory, exist_ok=True)
        open_files[next_day] = open(f"{day_directory}/export_wins.json", mode='w')
    return open_files


def generate_export_win(commodities, commodity_code_lookup, cats):
    num_items_in_export_win = random.randint(1, 3)
    export_win = []
    commodity_category = random.choice(cats)
    for commodity in [random.choice(commodities[commodity_category]) for _ in range(0, num_items_in_export_win)]:
        commodity_code = commodity_code_lookup[commodity_category][commodity]
        export_win.append({
            "commodity_code": commodity_code,
            "value": random.randint(1, 2000)
        })
    return export_win
