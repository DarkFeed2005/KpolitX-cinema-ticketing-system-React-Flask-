import React, { useState } from 'react';
import axios from 'axios';

const ManagerPanel = () => {
  const [movie, setMovie] = useState({ title: '', genre: '', duration: '' });
  const [show, setShow] = useState({ movieId: '', date: '', time: '', hall: '' });
  const [price, setPrice] = useState({ seatType: '', newPrice: '' });

  const handleAddMovie = async () => {
    await axios.post('/api/movies/add', movie);
    alert('Movie added!');
  };

  const handleScheduleShow = async () => {
    await axios.post('/api/shows/schedule', show);
    alert('Show scheduled!');
  };

  const handleUpdatePrice = async () => {
    await axios.post('/api/prices/update', price);
    alert('Price updated!');
  };

  return (
    <div>
      <h2>Manager Panel</h2>

      <section>
        <h3>Add Movie</h3>
        <input placeholder="Title" onChange={e => setMovie({ ...movie, title: e.target.value })} />
        <input placeholder="Genre" onChange={e => setMovie({ ...movie, genre: e.target.value })} />
        <input placeholder="Duration" onChange={e => setMovie({ ...movie, duration: e.target.value })} />
        <button onClick={handleAddMovie}>Add Movie</button>
      </section>

      <section>
        <h3>Schedule Show</h3>
        <input placeholder="Movie ID" onChange={e => setShow({ ...show, movieId: e.target.value })} />
        <input type="date" onChange={e => setShow({ ...show, date: e.target.value })} />
        <input type="time" onChange={e => setShow({ ...show, time: e.target.value })} />
        <input placeholder="Hall" onChange={e => setShow({ ...show, hall: e.target.value })} />
        <button onClick={handleScheduleShow}>Schedule</button>
      </section>

      <section>
        <h3>Alter Ticket Prices</h3>
        <input placeholder="Seat Type" onChange={e => setPrice({ ...price, seatType: e.target.value })} />
        <input placeholder="New Price" onChange={e => setPrice({ ...price, newPrice: e.target.value })} />
        <button onClick={handleUpdatePrice}>Update Price</button>
      </section>
    </div>
  );
};

export default ManagerPanel;