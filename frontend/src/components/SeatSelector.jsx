import React from 'react';

const SeatSelector = ({ seats, onSelect }) => {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(10, 1fr)', gap: '5px' }}>
      {seats.map(seat => (
        <button
          key={seat.seat_number}
          disabled={seat.status === 'booked'}
          onClick={() => onSelect(seat.seat_number)}
          style={{
            backgroundColor: seat.status === 'booked' ? '#ccc' : '#4caf50',
            color: 'white',
            padding: '10px',
            borderRadius: '4px'
          }}
        >
          {seat.seat_number}
        </button>
      ))}
    </div>
  );
};

export default SeatSelector;