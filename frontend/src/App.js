import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import OperationSelector from './components/OperationSelector';
import ResultDisplay from './components/ResultDisplay';
import './App.css';

const App = () => {
  const [file, setFile] = useState(null);
  const [textInput, setTextInput] = useState('');
  const [operation, setOperation] = useState('encrypt');
  const [result, setResult] = useState('');

  const handleFileUpload = (uploadedFile) => {
    setFile(uploadedFile);
  };

  const handleOperationSelect = (selectedOperation) => {
    setOperation(selectedOperation);
  };

  const handleTextChange = (event) => {
    setTextInput(event.target.value);
  };

  const handleProcess = async () => {
    const formData = new FormData();

    if (file) {
      formData.append('file', file);
    }

    if (textInput) {
      formData.append('text', textInput);
    }

    formData.append('operation', operation);

    try {
      const response = await fetch('http://localhost:5000/process', {
        method: 'POST',
        body: formData,
      });

      const data = await response.text();
      setResult(data);
    } catch (error) {
      console.error('Error processing input:', error);
      setResult('An error occurred while processing the input.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>CryptoMatic</h1>
        <FileUpload onFileUpload={handleFileUpload} />
        <div>
          <h2>Input Text</h2>
          <textarea
            value={textInput}
            onChange={handleTextChange}
            placeholder="Enter text to encrypt or decrypt"
          />
        </div>
        <OperationSelector onSelectOperation={handleOperationSelect} />
        <button onClick={handleProcess}>Process</button>
        <ResultDisplay result={result} />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
