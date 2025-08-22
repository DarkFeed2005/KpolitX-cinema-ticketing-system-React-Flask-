from flask import Blueprint, request, jsonify
from models import bookings, shows, prices, generate_id
from utils.qr import generate_qr

cashier_bp = Blueprint('cashier', __name__)

@cashier_bp.route('/api/bookings/create', methods=['POST'])
def create_booking():
    data = request.json
    ticket_id = generate_id('TKT')
    ticket_info = f"TicketID: {ticket_id}\nName: {data['name']}\nShow: {data['showId']}\nSeat: {data['seat']}"
    qr = generate_qr(ticket_info)

    booking = {
        'id': ticket_id,
        'name': data['name'],
        'showId': data['showId'],
        'seat': data['seat'],
        'price': prices.get('Regular', 500),
        'qr': qr
    }
    bookings.append(booking)
    return jsonify({'status': 'success', 'ticket': booking})

@cashier_bp.route('/api/seats/available', methods=['GET'])
def get_available_seats():
    show_id = request.args.get('show_id')
    booked_seats = [b['seat'] for b in bookings if b['showId'] == show_id]
    all_seats = [f"A{i}" for i in range(1, 21)]
    seat_map = [{'seat_number': s, 'status': 'booked' if s in booked_seats else 'available'} for s in all_seats]
    return jsonify(seat_map)