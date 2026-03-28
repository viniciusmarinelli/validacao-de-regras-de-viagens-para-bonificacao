from src.data_processing import data_processing
from src.bonus_rules import third_leg, lean_cattle_saturday
from src.report import generate_report


trips_file = "./data/trips_sample.csv"
drivers_file = "./data/drivers_sample.xlsx"

dataset = data_processing(trips_file, drivers_file)

result_third_leg = third_leg(dataset)
result_lean_cattle_saturday = lean_cattle_saturday(dataset)

generate_report(result_third_leg, result_lean_cattle_saturday)