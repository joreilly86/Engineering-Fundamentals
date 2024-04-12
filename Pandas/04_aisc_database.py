import pandas as pd

# Constants
load = 80  # kip
load_factor = 1.6
length_ft = 50  # feet
max_depth_in = 36  # inches

# Load the Excel file
df = pd.read_excel('aisc-shapes-database-v16.0.xlsx', sheet_name='Database v16.0')

# Convert relevant columns to numeric types
columns_to_convert = ['d', 'Zx', 'W']
df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

# Calculate the factored load
factored_load = load * load_factor

# Calculate the required maximum moment (kip-ft)
max_moment = factored_load * (length_ft / 4)

# Convert the maximum moment to kip-in by multiplying by 12 (1 ft = 12 in)
max_moment_kip_in = max_moment * 12

# Filter beams by depth, checking moment capacity, and ensuring only W shapes
suitable_beams = df[
    (df['d'] <= max_depth_in) & 
    (df['Zx'] * 36 >= max_moment_kip_in) &  # Assuming a yield stress of 36 ksi
    (df['Type'].str.strip().str.startswith('W'))  # Filter only W shapes
]

# Sort by weight to find the lightest beam
lightest_beam = suitable_beams.sort_values(by='W', ascending=True).head(1)

# Required Section Modulus
required_Zx = max_moment_kip_in / 36  # 36 ksi is the yield stress for A36 steel
print("Required Section Modulus:", required_Zx, "in^3")

# Display the lightest suitable W shape beam
print("The lightest suitable W shape beam that can resist a 50 kip point load at midspan within the given constraints:")
print(lightest_beam[['AISC_Manual_Label', 'd', 'Zx', 'W']])
