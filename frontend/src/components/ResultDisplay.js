import React from 'react';

const ResultDisplay = ({ result }) => {
  return (
    <div>
      <h2>Result</h2>
      <pre>{result}</pre>
    </div>
  );
};

export default ResultDisplay;
