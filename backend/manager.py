from flask import Blueprint, request, jsonify
from models import movies, shows, bookings, prices, generate_id, create_booking

manager_bp = Blueprint('manager', __name__)

@manager_bp.route('/api/movies/add', methods=['POST'])
def add_movie():
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing movie title'}), 400
    movie = {**data, 'id': generate_id('MOV')}
    movies.append(movie)
    return jsonify({'status': 'added', 'movie': movie})

@manager_bp.route('/api/shows/schedule', methods=['POST'])
def schedule_show():
    data = request.json
    required_fields = ['movieId', 'date', 'time', 'hall']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing show details'}), 400
    show = {**data, 'id': generate_id('SHOW')}
    shows.append(show)
    return jsonify({'status': 'scheduled', 'show': show})

@manager_bp.route('/api/prices/update', methods=['POST'])
def update_price():
    data = request.json
    if 'seatType' not in data or 'newPrice' not in data:
        return jsonify({'error': 'Missing pricing info'}), 400
    prices[data['seatType']] = int(data['newPrice'])
    return jsonify({'status': 'updated', 'prices': prices})

@manager_bp.route('/api/bookings/all', methods=['GET'])
def view_all_bookings():
    return jsonify({'bookings': bookings})

@manager_bp.route('/api/book', methods=['POST'])
def book_ticket():
    data = request.json
    required_fields = ['showId', 'seatType', 'user']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing booking info'}), 400
    try:
        booking = create_booking(data)
        bookings.append(booking)
        return jsonify({'status': 'booked', 'booking': booking})
    except Exception as e:
        return jsonify({'error': str(e)}), 500