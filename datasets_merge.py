import pandas as pd

# read the CDC data
cdc = pd.read_csv('./United_States_COVID-19_Community_Levels_by_County.csv')
# I will choose just the most recent week's data availablke in the dataset (March 9, 2023)
cdc = cdc.loc[cdc['date_updated'] == '2023-03-09']

# NIH datasets. Need to skip the first few rows (this is where the data begins)
# NEED TO SKEIP DIFFERENT NUMBER OF ROWS FOR EACH DATASET. LOOK AT YOUR DATA TO FIGURE OUT HOW MANY TO SKIP
nih_education = pd.read_csv('./HDPulse_data_bachelors_degree.csv', error_bad_lines=False, skiprows=5)
nih_income = pd.read_csv('./HDPulse_data_income.csv', error_bad_lines=False, skiprows=4)
nih_poverty = pd.read_csv('./HDPulse_data_poverty.csv', error_bad_lines=False, skiprows=4)



# merge all dataframes into one based on the County name
final_df = pd.merge(cdc, nih_education, how='left', left_on='county', right_on='County')          # nih education dataset
final_df = pd.merge(final_df, nih_income, how='left', left_on='county', right_on='County')        # nih income dataset
final_df = pd.merge(final_df, nih_poverty, how='left', left_on='county', right_on='County')       # nih poverty dataset

# export the final result!
#final_df.to_csv('your file path goes here')
