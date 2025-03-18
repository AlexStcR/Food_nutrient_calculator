#Nutrient finder application
import pandas as pd


def load_food_database():
    """Load and prepare the food database"""
    df = pd.read_csv('cleaned_usda_foods.csv')
    df.fillna(0, inplace=True)
    #print(df.head(20))
    return df
def nutrition_calculator(df):
    # Ask user for input
    food = input("Enter the food item: ").strip().lower()
    amount = float(input("Enter the amount (in grams): ").strip())

    # Find the food item in the database
    food_item = df[df['description'].str.lower() == food]

    if food_item.empty:
        print("Food item not found in the database.")
        return

    # Calculate total nutrients
    total_calories = (food_item['calories'].values[0] / 100) * amount
    total_protein = (food_item['protein'].values[0] / 100) * amount
    total_carbs = (food_item['carbs'].values[0] / 100) * amount
    total_fat = (food_item['fat'].values[0] / 100) * amount

    # Display the results
    print(f"\nNutritional Information for {amount}g of {food_item['description'].values[0]}:")
    print(f"Calories: {total_calories:.2f} kcal")
    print(f"Protein: {total_protein:.2f} g")
    print(f"Carbs: {total_carbs:.2f} g")
    print(f"Fat: {total_fat:.2f} g")

# Run the calculator
nutrition_calculator(load_food_database())
