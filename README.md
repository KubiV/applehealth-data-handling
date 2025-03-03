# Apple Health Data - Handling

## Overview
This project processes data from Apple Health. It contains two main scripts:
- **hr.py**: Exports the daily heart rate from an exported Apple Health XML file into a CSV format for a specific date.
- **hr2.py**: Exports or filters data from the Apple Health XML file for a given date range and creates a CSV file.

The project also includes **viewHR.py**, which loads the CSV data and plots the heart rate time series.

## Usage

### Export data for a specific day:
```bash
python hr.py export.xml 2024-02-20 output.csv
```
If no output file is specified, the data will be printed to the console.

### Export data for a date range:
```bash
python hr2.py export.xml 2024-02-20 2024-02-25 output.csv
```
If no output file is specified, the results will be printed to the console.

### Data Visualization:
First, create a CSV file using one of the above commands. Then run:
```bash
python viewHR.py
```
Adjust the `start_date` and `end_date` variables within `viewHR.py` to display the desired time range.

## Project Structure
- **hr.py**: Script for processing data for a single day.
- **hr2.py**: Script for processing data for a date range.
- **viewHR.py**: Script for visualizing CSV data.

## Requirements
- Python 3.x
- Packages: pandas, matplotlib

## Installation
Install the required Python packages using pip:
```bash
pip install pandas matplotlib
```

## Original Project
This project is based on the original work available at:
https://gist.github.com/tillson/97d95b3e34b2c4e668b42912bc2df91e

