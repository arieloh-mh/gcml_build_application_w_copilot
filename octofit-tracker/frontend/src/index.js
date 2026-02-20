import React from 'react';
import ReactDOM from 'react-dom/client';

import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';

// Definir la variable de entorno para el endpoint
if (!process.env.REACT_APP_CODESPACE_URL) {
  const host = window.location.hostname;
  const codespaceName = host.replace('-8000.app.github.dev', '');
  process.env.REACT_APP_CODESPACE_URL = `https://${codespaceName}-8000.app.github.dev`;
}
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
