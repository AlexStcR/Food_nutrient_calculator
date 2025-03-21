# USDA Food Data Cleaning and Nutritional Analysis

This repository contains a Jupyter Notebook and Python scripts for cleaning and preparing USDA food data for nutritional analysis. The processed dataset is optimized for calculating calories, protein, carbohydrates, and fat per 100g serving.

## Overview
The USDA food datasets are cleaned, standardized, and merged to create a consistent nutritional database. Key steps include:
- Handling mixed data types and missing values.
- Standardizing food names and serving sizes.
- Calculating nutrient values per 100g for easy comparison.

## Datasets Used
1. **food.csv**: Metadata for food items (e.g., descriptions, categories).
2. **nutrient.csv**: Nutrient definitions (e.g., energy, protein).
3. **food_nutrient.csv**: Nutrient amounts per food item.
4. **food_portion.csv**: Serving size information.

## Data Cleaning Steps
1. **Standardization**:
   - Converted food names to lowercase and trimmed whitespace.
   - Removed test entries (e.g., rows containing "test").
   - Dropped duplicates using `fdc_id` (unique food identifier).

2. **Serving Size Handling**:
   - Filtered gram-based measurements for consistency.
   - Assigned a default serving size of 100g for items without portion data.

3. **Nutrient Mapping**:
   - Identified key nutrients: Energy (1008), Protein (1003), Carbohydrates (1005), Fat (1004).
   - Merged nutrient data with food metadata.

4. **Final Adjustments**:
   - Calculated nutrient values per 100g using:  
     `(nutrient value) × (100 / serving size)`.
   - Renamed columns for clarity (e.g., `Energy` → `calories`).

## Output
The cleaned dataset (`cleaned_usda_foods.csv`) includes:
- `description`: Food name.
- `calories`: Energy per 100g (kcal).
- `protein`: Protein content per 100g (g).
- `carbs`: Carbohydrates per 100g (g).
- `fat`: Total fat per 100g (g).

## Usage
### Load the Cleaned Data
```python
import pandas as pd
df = pd.read_csv('cleaned_usda_foods.csv')
```
## Nutrition Calculator
Run nutrition_calculator.py to estimate nutrients for a custom serving size:
```
python nutrition_calculator.py
```

## Example output:

```
Nutritional Information for 20g of banana:
Calories: 67.20 kcal
Protein: 0.00 g
Carbs: 15.71 g
Fat: 0.21 g
```
## Files
Food_data_cleaning (2).ipynb: Jupyter Notebook with full cleaning workflow.

nutrition_calculator.py: Script for nutrient calculations.

cleaned_usda_foods.csv: Final cleaned dataset.

## Dependencies
Python 3.9+

pandas

## Credits
Data source: USDA FoodData Central.

License: Public domain (CC0).

Contributing
Issues and pull requests are welcome! For major changes, open an issue first to discuss improvements.

License
MIT

Copy
