import pandas as pd
import sqlite3

# ---------------- PART 1: READING FILES ----------------

# 1. Read customers table from chinook.db
conn = sqlite3.connect('chinook.db')
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("Customers Table (First 10 rows):")
print(customers_df.head(10))

# 2. Load iris.json into a DataFrame
iris_df = pd.read_json('iris.json')
print("\nIris Dataset Shape:", iris_df.shape)
print("Iris Column Names:", iris_df.columns)

# 3. Load titanic.xlsx
titanic_df = pd.read_excel('titanic.xlsx')
print("\nTitanic Dataset (First 5 rows):")
print(titanic_df.head())

# 4. Read Flights parquet file
flights_df = pd.read_parquet('flights.parquet')
print("\nFlights Dataset Info:")
print(flights_df.info())

# 5. Load movie.csv
movies_df = pd.read_csv('movie.csv')
print("\nMovie Dataset (Random 10 rows):")
print(movies_df.sample(10))


# ---------------- PART 2: EXPLORING DATAFRAMES ----------------

# 1. Modify iris DataFrame
iris_df.columns = iris_df.columns.str.lower()  # Rename columns to lowercase
iris_selected = iris_df[['sepal_length', 'sepal_width']]  # Select specific columns
print("\nSelected Columns from Iris Dataset:")
print(iris_selected.head())

# 2. Titanic DataFrame filtering
titanic_filtered = titanic_df[titanic_df['Age'] > 30]  # Filter age > 30
gender_counts = titanic_df['Sex'].value_counts()  # Count male and female passengers
print("\nTitanic Passengers (Age > 30):")
print(titanic_filtered.head())
print("\nTitanic Gender Counts:")
print(gender_counts)

# 3. Flights DataFrame
flights_selected = flights_df[['origin', 'dest', 'carrier']]
unique_destinations = flights_df['dest'].nunique()
print("\nSelected Columns from Flights Dataset:")
print(flights_selected.head())
print("\nNumber of Unique Destinations in Flights Dataset:", unique_destinations)

# 4. Movies DataFrame filtering and sorting
long_movies = movies_df[movies_df['duration'] > 120]  # Filter duration > 120 min
sorted_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print("\nLongest Movies (Sorted by Director Facebook Likes):")
print(sorted_movies.head())


# ---------------- PART 3: CHALLENGES AND EXPLORATIONS ----------------

# 1. Iris Dataset: Statistical calculations
iris_stats = iris_df.describe().T[['mean', '50%', 'std']]
print("\nIris Dataset Statistics:")
print(iris_stats)

# 2. Titanic Dataset: Min, Max, Sum of Age
titanic_age_stats = titanic_df['Age'].agg(['min', 'max', 'sum'])
print("\nTitanic Age Statistics:")
print(titanic_age_stats)

# 3. Movies Dataset Analysis
top_director = movies_df.groupby('director_name')['director_facebook_likes'].sum().idxmax()
longest_movies = movies_df.nlargest(5, 'duration')[['title', 'director_name']]
print("\nDirector with the Most Facebook Likes:", top_director)
print("\nTop 5 Longest Movies and Their Directors:")
print(longest_movies)

# 4. Flights Dataset: Missing Values Handling
missing_values = flights_df.isnull().sum()
flights_df.fillna(flights_df.mean(), inplace=True)  # Fill NaN with column mean
print("\nMissing Values in Flights Dataset (Before Filling):")
print(missing_values)
print("\nMissing Values After Filling:")
print(flights_df.isnull().sum())

print("\n--- ALL TASKS COMPLETED SUCCESSFULLY ---")

