import requests
import sqlite3
from bs4 import BeautifulSoup
import pandas as pd

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_title TEXT,
        company_name TEXT,
        location TEXT,
        job_description TEXT,
        application_link TEXT,
        UNIQUE(job_title, company_name, location)
    )
""")
conn.commit()

# Step 3: Scrape the Job Listings Page
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

new_jobs = []

for job in jobs:
    job_title = job.find("h2", class_="title").text.strip()
    company_name = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    job_description = job.find("div", class_="description").text.strip()
    application_link = job.find("a")["href"]

    cursor.execute("SELECT * FROM jobs WHERE job_title=? AND company_name=? AND location=?",
                   (job_title, company_name, location))

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?)",
                       (job_title, company_name, location, job_description, application_link))
        new_jobs.append((job_title, company_name, location, job_description, application_link))

conn.commit()
conn.close()

print(f"New jobs added: {len(new_jobs)}")
import sqlite3
import pandas as pd


def export_jobs(filter_by="location", value=""):

    conn = sqlite3.connect("jobs.db")

    if filter_by not in ["location", "company_name"]:
        print("Invalid filter. Use 'location' or 'company_name'.")
        return

    query = f"SELECT * FROM jobs WHERE {filter_by}=?"
    df = pd.read_sql_query(query, conn, params=(value,))

    filename = f"filtered_jobs_{filter_by}_{value.replace(' ', '_')}.csv"

    df.to_csv(filename, index=False)

    conn.close()

    print(f"Filtered jobs saved to {filename}")


