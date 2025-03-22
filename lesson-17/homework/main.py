import pandas as pd
import sqlite3

# ===================== MERGING AND JOINING =====================

# Load the chinook.db database
conn = sqlite3.connect('chinook.db')

# Perform an INNER JOIN between customers and invoices on CustomerId
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
invoices_df = pd.read_sql_query("SELECT * FROM invoices", conn)

merged_df = pd.merge(customers_df, invoices_df, on="CustomerId", how="inner")

# Find the total number of invoices per customer
invoice_counts = merged_df.groupby("CustomerId")["InvoiceId"].count()
print("\nTotal Invoices per Customer:")
print(invoice_counts.head())

# Load the movie.csv file
movies_df = pd.read_csv("movie.csv")

# Create two smaller DataFrames
movies_director = movies_df[['director_name', 'color']].dropna()
movies_reviews = movies_df[['director_name', 'num_critic_for_reviews']].dropna()

# Left join
left_join_df = pd.merge(movies_director, movies_reviews, on="director_name", how="left")

# Full outer join
full_outer_join_df = pd.merge(movies_director, movies_reviews, on="director_name", how="outer")

print("\nRows in Left Join:", len(left_join_df))
print("Rows in Full Outer Join:", len(full_outer_join_df))


# ===================== GROUPING AND AGGREGATING =====================

# Load Titanic dataset
titanic_df = pd.read_excel("titanic.xlsx")

# Group Titanic data by Pclass
grouped_titanic = titanic_df.groupby("Pclass").agg({
    "Age": "mean",
    "Fare": "sum",
    "PassengerId": "count"
}).rename(columns={"PassengerId": "Passenger_Count"})

print("\nTitanic Grouped Aggregations:")
print(grouped_titanic)

# Multi-level grouping on movies (by color and director_name)
grouped_movies = movies_df.groupby(["color", "director_name"]).agg({
    "num_critic_for_reviews": "sum",
    "duration": "mean"
}).reset_index()

print("\nMulti-Level Grouping on Movies:")
print(grouped_movies.head())

# Load Flights dataset
flights_df = pd.read_parquet("flights.parquet")

# Group flights by Year and Month
grouped_flights = flights_df.groupby(["Year", "Month"]).agg({
    "FlightNum": "count",
    "ArrDelay": "mean",
    "DepDelay": "max"
}).rename(columns={"FlightNum": "Total_Flights"})

print("\nNested Grouping on Flights:")
print(grouped_flights.head())


# ===================== APPLYING FUNCTIONS =====================

# Function to classify passengers as Child or Adult
def classify_age(age):
    return "Child" if age < 18 else "Adult"

titanic_df["Age_Group"] = titanic_df["Age"].apply(classify_age)
print("\nTitanic Data with Age Group Column:")
print(titanic_df[["Age", "Age_Group"]].head())

# Normalize salaries within each department
employees_df = pd.read_csv("employee.csv")

employees_df["Normalized_Salary"] = employees_df.groupby("Department")["Salary"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

print("\nEmployee Data with Normalized Salaries:")
print(employees_df.head())

# Function to classify movies based on duration
def classify_movie_length(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"

movies_df["Movie_Length"] = movies_df["duration"].apply(classify_movie_length)

print("\nMovies Data with Length Classification:")
print(movies_df[["title", "duration", "Movie_Length"]].head())


# ===================== USING PIPE =====================

# Titanic pipeline: Filter survived passengers, fill missing Age values, and create Fare_Per_Age column
def titanic_pipeline(df):
    return (
        df[df["Survived"] == 1]
        .assign(Age=df["Age"].fillna(df["Age"].mean()))
        .assign(Fare_Per_Age=lambda x: x["Fare"] / x["Age"])
    )

titanic_processed = titanic_df.pipe(titanic_pipeline)

print("\nTitanic Data After Pipeline Processing:")
print(titanic_processed.head())

# Flights pipeline: Filter delays and create Delay_Per_Hour column
def flights_pipeline(df):
    return (
        df[df["DepDelay"] > 30]
        .assign(Delay_Per_Hour=lambda x: x["DepDelay"] / x["AirTime"])
    )

flights_processed = flights_df.pipe(flights_pipeline)

print("\nFlights Data After Pipeline Processing:")
print(flights_processed.head())

print("\n--- ALL TASKS COMPLETED SUCCESSFULLY ---")
