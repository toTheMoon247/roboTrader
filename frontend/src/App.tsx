import React, { useState } from 'react';
import Message from './Message';
import RunButton from './Components/RunButton';


function App() {
  const [backendStatus, setBackendStatus] = useState("Backend off");

  const handleBackendStatusUpdate = (status: string) => {
    setBackendStatus(status);
  };

  return (
    <div>
      <Message text={backendStatus} />
      <RunButton onUpdateStatus={handleBackendStatusUpdate} />
    </div>
  );
}

export default App;
