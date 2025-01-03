# Quran-ul-Fehm

Quran-ul-Fehm is a web application designed to provide users with easy access to Islamic content such as Quranic verses, Islamic events, prayers (duas), and personalized features like prayer alarms and user settings.

## Features

- **Islamic Calendar**: View and track important Islamic events.
- **Quranic Verses**: Display Quranic verses in Arabic, with Urdu and English translations.
- **Prayer Alarms**: Set alarms for prayer times and customize notifications.
- **Islamic Prayers (Duas)**: A collection of duas with translations.
- **User Settings**: Manage preferences like dark mode and prayer notifications.

## Requirements

- Python 3.x
- Django 3.x or higher
- PostgreSQL (or another database backend)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/MehmoodAbbasi/Quran-ul-Fehm.git
    cd Quran-ul-Fehm
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the server**:

    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/` to access the application.

## Contributing

Feel free to fork and contribute to this project by creating pull requests for any improvements or fixes.

## License

This project is licensed under the MIT License.
