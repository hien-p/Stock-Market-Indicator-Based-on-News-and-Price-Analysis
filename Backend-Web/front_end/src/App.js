import { useState } from "react";

function MyButton({ onClick }){
  return(
    <button onClick={onClick}>
      Click me
    </button>
  )
}

function App(){
  const [count, setCount] = useState(0);
  const handleCount = () => setCount(count + 1)

  return(
    <div>
      <h1>Counters that update together</h1>
      <p>{count}</p>
      <MyButton count={count} onClick={handleCount} />
      <MyButton count={count} onClick={handleCount} />
    </div>
  )
}

export default App;
