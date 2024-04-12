[# #027 - Data Structures for Civil/Structural Engineers: Pandas 101](https://open.substack.com/pub/flocode/p/027-data-structures-for-civilstructural?r=tbs50&utm_campaign=post&utm_medium=web)

# 🐍 Python for Engineering Examples

This repository contains Python scripts that demonstrate the power of pandas for handling and analyzing engineering data. These examples are part of the [Flocode Engineering Insights newsletter](flocode.substack.com) and serve as practical tutorials for applying Python in various engineering contexts.

## Overview of Examples

### Case Study 1: Structural Health Monitoring
This example is narrative and included in the newsletter. No code for this one. This example will be covered in [flocodes courses](flocode.dev/courses).

### Case Study 2: Analyzing Flow Data
This script utilizes pandas to import, process, and analyze river flow data from a CSV file. Key operations include:
- **Data Loading**: Reads data from `flows.csv`, interpreting date columns correctly.
- **Data Inspection**: Uses methods like `df.head()`, `df.info()`, and `df.describe()` to understand the structure and statistics of the data.
- **Data Filtering**: Filters records where flow values exceed a certain threshold.
- **Data Aggregation**: Groups data by day to calculate daily mean flow rates.
- **Data Visualization**: Plots flow data over time using matplotlib to visualize trends.
- **Data Resampling**: Converts the data frequency from hourly to daily mean values.
- **Missing Data Handling**: Identifies and removes rows with missing data.
- **Data Export**: Writes the cleaned data back to a CSV file.

### Case Study 3: Construction Project Management
This example is narrative and included in the newsletter. No code for this one. This example will be covered in [flocodes courses](flocode.dev/courses).

### Case Study 4: Analyzing AISC Steel Beam Data with Pandas
This script demonstrates how to select an optimal W-shape steel beam from an Excel database that can support a specified load under given constraints using pandas. Key functionalities include:
- **Data Loading**: Imports data from an Excel file containing various beam properties.
- **Data Preparation**: Converts necessary columns to numeric types to facilitate calculations.
- **Engineering Calculations**:
  - Computes the factored load based on specified load and load factor.
  - Determines the required maximum bending moment.
  - Filters beams based on depth and moment capacity to ensure they meet design requirements.
- **Optimization**: Identifies the lightest beam that meets all the criteria.
- **Output**: Displays the specifications of the selected beam, including its weight and dimensions.

## Contributing

Flocode welcomes contributions! Please feel free to contribute by submitting issues and pull requests to the project repository.

For all things Python for civil and structural engineering, come visit [flocode.dev](flocode.dev) 🌊

[![Visit flocode.dev](https://img.shields.io/badge/Visit-flocode.dev-blue?style=for-the-badge&logo=appveyor)](https://flocode.dev).

## Licence

This work is licensed under the MIT License.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Contact

For more information, feedback, or questions, please visit  [flocode.dev/contact](https://flocode.dev/contact) or submit an issue in this repository.

Thank you for visiting our Python for Engineering repository. We hope these examples help you in your engineering projects and learning journey!
