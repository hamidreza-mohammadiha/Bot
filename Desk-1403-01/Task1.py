import pandas as pd

def filter_and_count_unique_stops(file1, file2, date):
    # Read the Excel files
    data1 = pd.read_excel(file1)
    data2 = pd.read_excel(file2)

    # Filter rows based on the 'gun' value for each file
    filtered_data1 = data1[data1['gun'] == date]
    filtered_data2 = data2[data2['gun'] == date]

    # Get the list of 'guzergah kodu' from filtered data1
    guzergah_kodu_list = filtered_data1['guzergah kodu'].unique()

    # Filter data2 rows where 'guzergah kodu' exists in data1's 'guzergah kodu' list
    final_filtered_data2 = filtered_data2[filtered_data2['guzergah kodu'].isin(guzergah_kodu_list)]

    # Count unique 'durak kodu'
    unique_stops = final_filtered_data2['durak kodu'].nunique()

    return unique_stops

# Set the file paths for the two Excel files
file1_path = "1.xlsx"
file2_path = "2.xlsx"

# Perform the operations for the two dates
unique_stops_15032023 = filter_and_count_unique_stops(file1_path, file2_path, "15.03.2023")
unique_stops_03082023 = filter_and_count_unique_stops(file1_path, file2_path, "03.08.2023")

print(f"Number of unique stops on 15.03.2023: {unique_stops_15032023}")
print(f"Number of unique stops on 03.08.2023: {unique_stops_03082023}")
