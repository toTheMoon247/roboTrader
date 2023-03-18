import { Button } from "react-bootstrap";
import { useState } from "react";
import { startApp, stopApp } from "../mockApi";

function RunButton(props: { onUpdateStatus: (status: string) => void }) {
    const [status, setStatus] = useState("idle");
  
    const handleClick = async () => {
      if (status === "idle") {
        setStatus("running");
        await startApp();
        props.onUpdateStatus("Backend on");
      } else {
        setStatus("idle");
        await stopApp();
        props.onUpdateStatus("Backend off");
      }
    };
  
    const buttonText = status === "idle" ? "Run" : "Stop";
  
    return (
      <Button variant="primary" onClick={handleClick}>
        {buttonText}
      </Button>
    );
  }  

export default RunButton;
