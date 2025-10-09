import { useState } from 'react';
import OutputItem from './OutputItem';

export default function Main() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const addItem = (e) => {
    e.preventDefault();
    if (!name.trim() || !email.trim()) {
      return;
    }

    const newItem = {
      id: items.length + 1,
      name: name,
      email: email
    };

    setItems((prev) => [...prev, newItem]);

    setName("");
    setEmail("");
    return;
  };

  const deleteItem = (id) => {
    setItems(items.filter((i) => i.id !== id));
  };

  return (
    <>
      <div>
        <div>
          <h1 class="title">Spectator's Sources</h1>
        </div>

        <form action="" className="form" onSubmit={addItem}>
          <div class="input-div">
            <label forName="name" className="input-label">
              Source Name:
              <input 
                type="text" 
                id="name" 
                name="name" 
                className="input-item" 
                onChange={(e) => setName(e.target.value)} 
                value={name} 
              />
            </label>
          </div>

          <div className="input-div">
            <label forName="email" className="input-label">
              Source Email: 
              <input 
                type="email" 
                id="email" 
                name="email" 
                className="input-item" 
                onChange={(e) => setEmail(e.target.value)} 
                value={email} 
              />
            </label>
          </div>

          <button type="submit" className="submit-btn">ADD</button>
        </form>
      </div>

      <div className="output-list">
        {items.length ? 
          items.map((i) => (
          <OutputItem 
            id={i.id}
            name={i.name}
            email={i.email}
            deleteItem={deleteItem}
          />
          ))
        :
          <p></p>
        }
      </div>
    </>
  );
};
