# expense_tracker


Expense Tracker is a simple, user-friendly Django-based web application for tracking personal finances. It allows users to manage their expenses and income efficiently by categorizing transactions, visualizing trends, and maintaining organized records.

Features

User Authentication: Secure login/logout functionality.

Transaction Management:

Add, edit, delete, and view transactions.

Categorize transactions as income or expense.

Import transactions from CSV files.

Dynamic Filters: Filter transactions by category, type, and date.

Pagination: Smooth loading of large datasets with infinite scroll.

Data Visualization: Insights into total income, total expenses, and category-wise breakdowns.

Technologies Used

Backend: Django

Frontend: HTML, CSS, JavaScript, HTMX

Database: SQLite (default, can be configured to PostgreSQL or others)

Styling: Tailwind CSS

Import/Export: Django Import-Export library

Installation and Setup

Follow these steps to set up the project locally:

Clone the repository:

git clone https://github.com/popzon99/expense_tracker.git
cd expense_tracker

Create and activate a virtual environment:

python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

Install the required dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Create a superuser for admin access:

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Open your browser and navigate to:

http://127.0.0.1:8000/

Importing Transactions

Use the "Import Transactions" page to upload a CSV file with the following format:

amount: The amount for the transaction.

type: Either income or expense.

date: Date of the transaction in the format YYYY-MM-DD.

category: The category name (must match an existing category)
Contributing

