from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import qrcode
import io
import base64

app = Flask(__name__)
CORS(app)

# Health check route
@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'Backend is running'})

# Simple test route
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Flask backend!'})

# Booking route with QR generation
@app.route('/api/book', methods=['POST'])
def book_ticket():
    data = request.get_json()
    name = data.get('name')
    movie = data.get('movie')
    seat = data.get('seat')

    if not all([name, movie, seat]):
        return jsonify({'error': 'Missing booking details'}), 400

    # Generate unique ticket ID
    ticket_id = str(uuid.uuid4())[:8]

    # Compose ticket info
    ticket_info = f"TicketID: {ticket_id}\nName: {name}\nMovie: {movie}\nSeat: {seat}"

    # Generate QR code
    qr = qrcode.make(ticket_info)
    buf = io.BytesIO()
    qr.save(buf, format='PNG')
    qr_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Return ticket data and QR
    return jsonify({
        'status': 'success',
        'ticket': {
            'id': ticket_id,
            'name': name,
            'movie': movie,
            'seat': seat,
            'qr': qr_base64
        }
    })

if __name__ == '__main__':
    app.run(debug=True)