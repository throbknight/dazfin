
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV
csv_file = 'sample.csv'  # Replace with your actual file path
df = pd.read_csv(csv_file)

# Strip any leading/trailing spaces from column names to avoid issues
df.columns = df.columns.str.strip()

# Define category mapping based on keywords
category_keywords = {
    'Supercharging and EV': ['TESLA SUPERCHARGER', 'TESLA SUBSCRIPTION', 'TESLA RESERVATION'],
    'Health and Insurance': ['KAISER', 'HOSPITAL', 'DENTAL', 'PHARMACY'],
    'Auto and Transportation': ['DIGITAL FEDERAL CREDIT', 'DCU', 'CARWASH', 'CAR RENTAL'],
    'Utilities and Recurring Bills': ['LYCAMOBILE', 'INTERNET', 'UTILITY'],
    'Groceries and Essentials': ['FARM 2 COOK', 'HARELI FRESH', 'COSTCO', 'WALMART', 'BAKERY'],
    'Dining and Food': ['CHICK-FIL-A', 'BURGER KING', 'STARBUCKS', 'TACO BELL', 'MCDONALD'],
    'Entertainment and Leisure': ['DISNEYPLUS', 'AMC', 'NETFLIX', 'TIDAL', 'FOSSIL RIM'],
    'Travel and Hotels': ['PRICELN', 'MARRIOTT', 'HOTEL', 'PARKING', 'AIRLINES', 'ONESTOPPARKING'],
    'Retail and Shopping': ['JOCKEY', 'GAP', 'SAMSONITE', 'IKEA', 'AMAZON', 'NORTH FACE'],
    'Indian Specialty Stores and Food': ['DESI CHOWRASTHA', 'DESI DISTRICT', 'INDIA MEALS', 'MALABAR', 'KUPPANNA', 'DELHI6'],
    'Refunds and Returns': ['CASHBACK', 'REFUND', 'STATEMENT CREDIT'],
    'Payments and Credits': ['INTERNET PAYMENT', 'THANK YOU PAYMENT']
}

# Function to auto-categorize
def categorize(description):
    description_upper = description.upper()
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in description_upper:
                return category
    return 'Miscellaneous Merchandise'  # Default category

# Apply categorization
df['AutoCategory'] = df['Description'].apply(categorize)

# Summarize spending by new categories
summary = df.groupby('AutoCategory')['Amount'].sum().sort_values()



# Smart search function
def smart_search(term):
    term_upper = term.upper()
    matches = df[df['Description'].str.upper().str.contains(term_upper)]
    return matches
search = input("What should I search for in your transactions: ")
# Example usage of smart search
search_results = smart_search(search)
#
# # Displaying relevant columns of the search results
# print(search_results[['Trans. Date', 'Description', 'Amount', 'AutoCategory']])
# Adjust Pandas display settings to show all columns fully
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    print(search_results[['Trans. Date', 'Description', 'Amount', 'AutoCategory']])
# Print the total amount
total_amount = search_results['Amount'].sum()
print(f"\nTotal Amount for all transactions: ${total_amount:.2f}")