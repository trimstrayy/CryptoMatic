import React from 'react';

const OperationSelector = ({ onSelectOperation }) => {
  const handleSelect = (event) => {
    onSelectOperation(event.target.value);
  };

  return (
    <div>
      <h2>Select Operation</h2>
      <select onChange={handleSelect}>
        <option value="encrypt">Encrypt</option>
        <option value="decrypt">Decrypt</option>
      </select>
    </div>
  );
};

export default OperationSelector;
