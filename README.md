
# Rescue API

This is the back-end of the **Rescue App**, developed with Flask. It provides RESTful endpoints to manage data related to emergency situations.

## 🚀 Technologies Used

- **Python 3.8+**
- **Flask**
- **SQLite**
- **SQLAlchemy**

## 📁 Project Structure

- `app.py` – Main file that initializes the Flask application.
- `model/` – Contains data models defined with SQLAlchemy.
- `schemas/` – Defines serialization schemas with Marshmallow.
- `database/` – Scripts and files related to the SQLite database.
- `logger.py` – Logging configuration for the application.
- `requirements.txt` – List of project dependencies.

## ⚙️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/lucassamel/rescue-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd rescue-api
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   flask run --host 0.0.0.0 --port 5000
   ```

For development, it's helpful to use auto-reload mode:

```bash
flask run --host 0.0.0.0 --port 5000 --reload
```

Access `http://localhost:5000/` in your browser to verify the API is running.

## 🔗 Front-end Integration

This API is designed to work in conjunction with the front-end available at: [lucassamel/rescue-app-front](https://github.com/lucassamel/rescue-app-front).

Make sure the API is running before starting the front-end to ensure proper communication between components.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

For more information or to explore the code, visit the GitHub repository: [lucassamel/rescue-api](https://github.com/lucassamel/rescue-api).
