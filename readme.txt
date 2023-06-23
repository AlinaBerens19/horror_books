Horror Library Website
This is a horror library website that allows users to explore and discover a wide collection of horror books, authors, and related information. The website is built using Next.js 13 for the frontend and Django REST Framework for the backend.

Features
Browse a vast collection of horror books.
Search for books by title, author, or genre.
View detailed information about books, including summaries, ratings, and reviews.
Create an account and log in to personalize your experience.
Rate and review books to share your opinions.
Bookmark books to save them for later.
Discover popular and trending horror books.
Explore featured authors and their works.
Get recommendations based on your reading preferences.
Mobile-responsive design for seamless browsing on different devices.
Tech Stack
The website is built using the following technologies:

Frontend:

Next.js 13 - A React framework for building server-rendered and statically-generated websites.
React - A JavaScript library for building user interfaces.
Typescript - Local scoped CSS styling for components.
Axios - A promise-based HTTP client for making API requests.


Backend:

Django REST Framework - A powerful and flexible toolkit for building Web APIs with Django.
Django - A high-level Python web framework.
PostgreSQL - A robust and scalable relational database.
Django ORM - Object-relational mapping for interacting with the database.
JWT - JSON Web Tokens for user authentication and authorization.

Getting Started
To set up the project locally, follow these steps:

Clone the repository: git clone <repository-url>

Navigate to the project directory: cd horror-library-website

Set up the frontend:

Install dependencies: cd frontend && npm install
Start the development server: npm run dev
The frontend will be accessible at http://localhost:3000.

Set up the backend:

Create a virtual environment (optional but recommended): python -m venv venv
Activate the virtual environment:
On macOS and Linux: source venv/bin/activate
On Windows: venv\Scripts\activate.bat
Install dependencies: pip install -r requirements.txt
Set up the database and perform migrations: python manage.py migrate
Start the Django development server: python manage.py runserver
The backend API will be accessible at http://localhost:8000.

Configuration

Frontend:

API base URL: Update the NEXT_PUBLIC_API_BASE_URL in .env.local file to match your backend API URL.
Backend:

Database: Update the database settings in settings.py to match your PostgreSQL configuration.
CORS: Configure CORS settings in settings.py to allow frontend requests from the correct origins.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


Acknowledgements
This project was inspired by our love for horror literature and the desire to create a dedicated platform for horror enthusiasts.
We would like to express our gratitude to the developers of Next.js and Django REST Framework for providing powerful tools and frameworks for building web applications.