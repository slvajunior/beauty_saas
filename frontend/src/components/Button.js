// src/components/Button.js
import React from 'react';

function Button({ label, onClick }) {
  return (
    <button onClick={onClick} className="btn">
      {label}
    </button>
  );
}

export default Button;
