interface Props {
    text: string;
  }
  
  function Message({ text }: Props) {
    return <h1>{text}</h1>;
  }
  
  export default Message;
  