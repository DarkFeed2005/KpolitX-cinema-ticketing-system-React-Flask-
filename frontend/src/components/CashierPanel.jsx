import React, { useState, useEffect } from 'react';
import axios from 'axios';
import SeatSelector from './SeatSelector';

const CashierPanel = () => {
  const [booking, setBooking] = useState({ name: '', showId: '', seat: '' });
  const [availableSeats, setAvailableSeats] = useState([]);

  useEffect(() => {
    if (booking.showId) {
      axios.get(`/api/seats/available?show_id=${booking.showId}`)
        .then(res => setAvailableSeats(res.data));
    }
  }, [booking.showId]);

  const handleBooking = async () => {
    await axios.post('/api/bookings/create', booking);
    alert('Booking successful!');
  };

  return (
    <div>
      <h2>Cashier Panel</h2>
      <input placeholder="Customer Name" onChange={e => setBooking({ ...booking, name: e.target.value })} />
      <input placeholder="Show ID" onChange={e => setBooking({ ...booking, showId: e.target.value })} />
      <SeatSelector seats={availableSeats} onSelect={seat => setBooking({ ...booking, seat })} />
      <button onClick={handleBooking}>Book Ticket</button>
    </div>
  );
};

export default CashierPanel;