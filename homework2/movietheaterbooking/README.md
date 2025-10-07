# Movie Theater Booking System

A Django-based movie theater seat booking system built for CS4300 Homework 2. This application provides both REST API endpoints and a web interface for managing movie bookings, seat reservations, and user interactions.

*Note: Perplexity was used to create this README, understand Django concepts and debugging application issues.*

## Features

### Core Functionality
- **Movie Management**: Create and manage movie listings with details like title, description, release date, and duration
- **Seat Booking**: Reserve specific seats for movies with real-time availability tracking
- **User Bookings**: Track individual user reservations and booking history
- **Dual Interface**: Both REST API endpoints and web templates for flexible access

### API Endpoints
- **Movies API**: Full CRUD operations with custom actions for seat availability
- **Seats API**: Manage seat inventory with booking status tracking
- **Bookings API**: Create and manage reservations with user filtering
- **Custom Actions**: Specialized endpoints for available/unavailable seats per movie

### Web Interface
- **Movie List**: Browse available movies with booking links
- **Seat Selection**: Interactive seat booking interface for specific movies
- **Booking History**: View reservation history filtered by user

## Technology Stack

- **Framework**: Django 4.2.11
- **API**: Django REST Framework
- **Database**: SQLite (development)
- **Frontend**: Django Templates with Bootstrap styling
- **Authentication**: Django built-in user system

## Project Structure

```
movietheaterbooking/
├── manage.py                           # Django management script
├── movietheaterbooking/                # Main project directory
│   ├── settings.py                     # Django configuration
│   ├── urls.py                         # Root URL configuration
│   └── wsgi.py                         # WSGI configuration
└── bookings/                           # Main application
    ├── models.py                       # Database models (Movie, Seat, Booking)
    ├── views.py                        # API viewsets and template views
    ├── serializers.py                  # DRF serializers with validation
    ├── urls.py                         # App URL routing
    ├── admin.py                        # Django admin configuration
    ├── templates/bookings/             # HTML templates
    │   ├── base.html                   # Base template
    │   ├── movie_list.html             # Movie listing page
    │   ├── seat_booking.html           # Seat selection interface
    │   └── booking_history.html        # User booking history
    └── management/commands/            # Custom Django commands
        └── create_test_data.py         # Test data generation script
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/calebc1800/cs4300.git
   cd cs4300/homework2/movietheaterbooking
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create test data (optional)**
   ```bash
   python manage.py create_test_data
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```

## Usage

### Web Interface
- **Home Page**: `http://127.0.0.1:8000/` - Browse available movies
- **Seat Booking**: `http://127.0.0.1:8000/movie/<movie_id>/book/` - Book seats for a specific movie
- **Booking History**: `http://127.0.0.1:8000/history/` - View booking history by user

### REST API Endpoints

#### Movies
- `GET /api/movies/` - List all movies
- `POST /api/movies/` - Create new movie
- `GET /api/movies/<id>/` - Retrieve specific movie
- `PUT /api/movies/<id>/` - Update movie
- `DELETE /api/movies/<id>/` - Delete movie
- `GET /api/movies/<id>/available_seats/` - Get available seats for movie
- `GET /api/movies/<id>/unavailable_seats/` - Get booked seats for movie

#### Seats
- `GET /api/seats/` - List all seats
- `POST /api/seats/` - Create new seat
- `GET /api/seats/available/` - List available seats
- `GET /api/seats/unavailable/` - List booked seats
- `POST /api/seats/<id>/book/` - Book specific seat

#### Bookings
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create new booking
- `GET /api/bookings/?user_id=<id>` - Filter bookings by user
- `GET /api/bookings/my_bookings/?user_id=<id>` - Get user's bookings

## Database Models

### Movie
- `title` (CharField): Movie title
- `description` (TextField): Movie description
- `release_date` (DateField): Release date
- `duration` (DurationField): Movie duration

### Seat
- `movie` (ForeignKey): Associated movie
- `seat_number` (CharField): Seat identifier (e.g., "A01", "B15")
- `booking_status` (BooleanField): Availability status

### Booking
- `movie` (ForeignKey): Booked movie
- `seat` (ForeignKey): Reserved seat
- `user` (ForeignKey): User who made booking
- `booking_date` (DateTimeField): Booking timestamp

## Test Data

The application includes a management command to create sample data:

```bash
python manage.py create_test_data
```

This creates:
- Two sample movies ("The Amazing Spider-Man", "Inception")
- 40 seats per movie (A01-A20, B01-B20)
- Two test users (testuser01, testuser02)

## Key Features Implementation

### Seat Availability Tracking
- Real-time seat status updates when bookings are created
- Validation prevents double-booking of seats
- Separate endpoints for available/unavailable seat queries

### User-Filtered Bookings
- Query parameter support for filtering bookings by user
- Optimized database queries with select_related for performance
- Booking history interface with user selection dropdown

### API Validation
- Duration validation ensures positive movie lengths
- Seat number validation prevents empty values
- Booking validation checks seat availability before creation

### Custom Management Commands
- Automated test data generation
- Handles duplicate creation gracefully with get_or_create patterns

## Development Notes

### Recent Updates
- Fixed booking functionality and seat status tracking
- Implemented proper model relationships and cascading
- Added comprehensive API serializers with validation
- Created responsive web interface templates
- Optimized database queries for booking history

### Known Features
- Uses SQLite for development (easily configurable for production databases)
- Bootstrap styling for responsive web interface
- Django admin interface available for administrative tasks
- REST Framework browsable API for testing endpoints

## Contributing

This project was developed as part of CS4300 coursework. For educational purposes and assignment requirements.

## License

This project is created for educational purposes as part of university coursework.