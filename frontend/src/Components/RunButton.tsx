import { Button } from "react-bootstrap";
import { useState } from "react";

function RunButton() {
  const [status, setStatus] = useState<"idle" | "running" | "stopped">("idle");

  function handleClick() {
    if (status === "idle") {
      setStatus("running");
    } else {
      setStatus("idle");
    }
    console.log("clicked");
  }
  

  return (
    <Button variant="primary" onClick={handleClick}>
      {status === "idle" ? "Run" : "Stop"}
    </Button>
  );
}

export default RunButton;
