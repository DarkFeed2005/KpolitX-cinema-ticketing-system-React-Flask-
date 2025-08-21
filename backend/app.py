from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample route to test connection
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello from Flask backend!'})

# Example: Book a ticket
@app.route('/api/book', methods=['POST'])
def book_ticket():
    data = request.get_json()
    name = data.get('name')
    movie = data.get('movie')
    seat = data.get('seat')

    # Simulate booking logic
    if not all([name, movie, seat]):
        return jsonify({'error': 'Missing booking details'}), 400

    # In real app: Save to DB, generate QR, etc.
    return jsonify({
        'status': 'success',
        'ticket': {
            'name': name,
            'movie': movie,
            'seat': seat,
            'confirmation': 'ABC123'
        }
    })

# Optional: Health check or homepage
@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'Backend is running'})

if __name__ == '__main__':
    app.run(debug=True)