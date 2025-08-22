@app.route('/api/movies/add', methods=['POST'])
def add_movie():
    # Accept title, genre, duration, etc.
    pass

@app.route('/api/shows/schedule', methods=['POST'])
def schedule_show():
    # Accept movie_id, date, time, hall
    pass

@app.route('/api/prices/update', methods=['POST'])
def update_price():
    # Accept seat_type, new_price
    pass

@app.route('/api/bookings/all', methods=['GET'])
def view_all_bookings():
    # Return all bookings for admin
    pass