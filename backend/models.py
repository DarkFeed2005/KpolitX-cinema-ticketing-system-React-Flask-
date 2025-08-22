import random
import string

movies = []
shows = []
bookings = []
prices = {
    'Regular': 500,
    'VIP': 1000
}

def generate_id(prefix):
    return f"{prefix}{''.join(random.choices(string.digits, k=5))}"

def create_booking(data):
    show_id = data['showId']
    seat_type = data['seatType']
    user = data['user']

    # Optional: validate show exists
    if not any(show['id'] == show_id for show in shows):
        raise ValueError("Invalid show ID")

    # Optional: validate seat type
    if seat_type not in prices:
        raise ValueError("Invalid seat type")

    booking = {
        'id': generate_id('BOOK'),
        'showId': show_id,
        'seatType': seat_type,
        'price': prices[seat_type],
        'user': user
    }
    return booking