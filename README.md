
# FastAPI Note Add Project

This project is a simple note-taking app built with **FastAPI** where users can add notes. It uses **MongoDB** as the database.

## Features

- Add new notes with a title, description, and important flag.
- FastAPI as the backend framework.
- MongoDB for note storage.
- Dynamic page updates.

## Requirements

Before you begin, make sure you have the following installed on your system:

- Python 3.7+
- MongoDB (local or hosted)
- pip (Python package installer)

## Setup

### Step 1: Clone the Repository

First, clone the repository to your local machine.

```bash
git clone https://github.com/yourusername/fast-api-note-add.git
cd fast-api-note-add
```

### Step 2: Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

Once inside the virtual environment, install the project dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the `.env` File

Create a `.env` file in the root of the project. Inside this file, add your MongoDB connection URI:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
```

Make sure to replace `<username>`, `<password>`, and `<dbname>` with your MongoDB credentials.

### Step 5: Database Setup

You need a MongoDB database to store notes. Either:

- Use MongoDB Atlas (a cloud MongoDB solution) or
- Run MongoDB locally.

Create a collection named `notes` in your MongoDB database.

### Step 6: Running the Application

To run the FastAPI app, use `uvicorn`. Run the following command:

```bash
uvicorn app:app --reload
```

The application should now be running at:

```bash
http://127.0.0.1:8000
```

## Project Structure

```bash
fast-api-note-add/
├── api/
│   └── app.py          # Main FastAPI application file
├── db.py               # MongoDB connection configuration
├── templates/          # HTML templates for rendering
├── static/             # Static files (CSS, JS)
├── .env                # Environment variables (Mongo URI)
├── requirements.txt    # Project dependencies
└── README.md           # This README file
```

## Routes

- **GET /**: Display the form to add notes and show existing notes.
- **POST /**: Add a new note to the database.

## License

This project is licensed under the MIT License.
