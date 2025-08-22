import React, { useState } from 'react';
import axios from 'axios';
import SeatSelector from './SeatSelector';

const BookingForm = () => {
  const [form, setForm] = useState({ name: '', showId: '', seat: '' });
  const [seats, setSeats] = useState([]);

  const fetchSeats = async () => {
    const res = await axios.get(`/api/seats/available?show_id=${form.showId}`);
    setSeats(res.data);
  };

  const handleSubmit = async () => {
    await axios.post('/api/bookings/create', form);
    alert('Booking confirmed!');
  };

  return (
    <div>
      <h2>Book Your Ticket</h2>
      <input placeholder="Your Name" onChange={e => setForm({ ...form, name: e.target.value })} />
      <input placeholder="Show ID" onChange={e => setForm({ ...form, showId: e.target.value })} />
      <button onClick={fetchSeats}>Load Seats</button>
      <SeatSelector seats={seats} onSelect={seat => setForm({ ...form, seat })} />
      <button onClick={handleSubmit}>Confirm Booking</button>
    </div>
  );
};

export default BookingForm;