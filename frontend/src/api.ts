async function startApp() {
    await fetch('/start');
  }
  
  async function stopApp() {
    await fetch('/stop');
  }
  
  export { startApp, stopApp };
  