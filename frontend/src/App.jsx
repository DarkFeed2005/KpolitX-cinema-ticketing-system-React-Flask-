import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [form, setForm] = useState({ name: '', movie: '', seat: '' });
  const [ticket, setTicket] = useState(null);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setTicket(null);

    try {
      const res = await axios.post('http://localhost:5000/api/book', form);
      setTicket(res.data.ticket);
    } catch (err) {
      console.error('Booking failed:', err);
      setError('Booking failed. Please check your input or try again.');
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: '500px', margin: 'auto' }}>
      <h2>🎬 Book Your Cinema Ticket</h2>

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <input
          name="name"
          placeholder="Your Name"
          value={form.name}
          onChange={handleChange}
          required
        />
        <input
          name="movie"
          placeholder="Movie Title"
          value={form.movie}
          onChange={handleChange}
          required
        />
        <input
          name="seat"
          placeholder="Seat Number"
          value={form.seat}
          onChange={handleChange}
          required
        />
        <button type="submit">Book Ticket</button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {ticket && (
        <div style={{ marginTop: '2rem', textAlign: 'center' }}>
          <h3>✅ Booking Confirmed</h3>
          <p><strong>ID:</strong> {ticket.id}</p>
          <p><strong>Name:</strong> {ticket.name}</p>
          <p><strong>Movie:</strong> {ticket.movie}</p>
          <p><strong>Seat:</strong> {ticket.seat}</p>
          <img
            src={`data:image/png;base64,${ticket.qr}`}
            alt="Ticket QR"
            style={{ marginTop: '1rem', width: '200px', height: '200px' }}
          />
        </div>
      )}
    </div>
  );
}

export default App;