import pandas as pd

FILE_PATH_1 = 'Closed_window.csv'
FILE_PATH_2 = 'Open_window.csv'
FILE_PATH_3 = 'urban_noise_levels.csv'

def load_and_analyze(file_path, location_name):
    try:
        df = pd.read_csv(file_path, sep=',')
        
        avg_noise = df['dBa'].mean()
        max_noise = df['dBa'].max()
        min_noise = df['dBa'].min()
        
        print(f"--- Analysis: {location_name} ---")
        print(f" Average Noise Level: {avg_noise:.2f} dBA")
        print(f" Maximum Noise Level: {max_noise} dBA")
        print(f" Minimum Noise Level: {min_noise} dBA")
        print("---------------------------------")
        
        df = df.rename(columns={'dBa': location_name})
        return df
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except KeyError:
        print(f"Error: Column dBa not found in file {file_path}. Check CSV headers.")
        return None

df1 = load_and_analyze(FILE_PATH_1, "Спальний район")
df2 = load_and_analyze(FILE_PATH_2, "Центр міста")
df3 = load_and_analyze(FILE_PATH_3, "Місто")
