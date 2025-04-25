# tweetX - Microblogging Website 🐦
tweetX Screenshot:

![image](https://github.com/user-attachments/assets/f6d03c40-03ac-4299-b0e2-ea47cb20f219)

![image](https://github.com/user-attachments/assets/bd377945-887b-42e7-a93c-5ebec96ad754)

![image](https://github.com/user-attachments/assets/ccebffbf-5c2a-4e89-8e37-861533c80366)

## Features ✨

- Create, edit, and delete tweets
- User authentication (login/register)
- Responsive design
- Image uploads
- Search functionality

## Technologies Used 🛠️

- **Backend**: Django 4.0+
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (Development)
- **Other**: Font Awesome, Django Crispy Forms

## Prerequisites 📋

- Python 3.9+
- Django
- Git

## Installation 💻

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tweetX.git
   cd tweetX
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit the .env file with your settings
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Create superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

7. Run development server:
   ```bash
   python manage.py runserver
   ```

8. Access the application at:
   ```
   http://localhost:8000
   ```
   Admin panel:
   ```
   http://localhost:8000/admin
   ```

## Project Structure 📂

```
tweetX/
├── tweetX/               # Main app
│   ├── migrations/       # Database migrations
│   ├── static/           # Static files
│   ├── templates/        # HTML templates
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py
│   ├── models.py         # Database models
│   ├── urls.py           # URL routing
│   ├── views.py          # View functions
│   └── ...
├── .env.example          # Environment variables template
├── .gitignore
├── manage.py
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel configuration
└── README.md
```

## Configuration ⚙️

Create a `.env` file in project root (based on `.env.example`):

```ini
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Running Tests 🧪

```bash
python manage.py test
```

## Contributing 🤝

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

Made with ❤️ by P.Desai.
