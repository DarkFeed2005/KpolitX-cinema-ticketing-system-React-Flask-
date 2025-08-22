@app.route('/api/bookings/create', methods=['POST'])
def create_booking():
    # Accept name, movie_id, seat, etc.
    pass

@app.route('/api/seats/available', methods=['GET'])
def get_available_seats():
    # Return seat map for selected show
    pass