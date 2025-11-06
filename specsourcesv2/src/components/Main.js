import { useEffect, useState } from 'react';
import OutputItem from './Source';
import axios from 'axios';

export default function Main() {
  const [sources, setSources] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    axios.get(`${process.env.REACT_APP_API_URL}/sources`)
      .then((response) => {
        // console.log(response);
        setSources(response.data);
      })
      .catch((error) => {
        console.error(error);
      });

  }, [sources]);

  const addSource = (e) => {
    e.preventDefault();
    if (!name.trim() || !email.trim()) {
      return;
    }

    const newSource = {
      name: name,
      email: email
    };

    axios.post(`${process.env.REACT_APP_API_URL}/sources`, newSource);

    // setSources((prev) => [...prev, newSource]);

    setName("");
    setEmail("");
    return;
  };

  const deleteSource = (id) => {
    axios.delete(`${process.env.REACT_APP_API_URL}/sources/${id}`);
    // setSources(sources.filter((i) => i.id !== id));
  };

  return (
    <>
      <div>
        <div>
          <h1 className="title">Spectator's Sources</h1>
        </div>

        <form action="" className="form" onSubmit={addSource}>
          <div className="input-div">
            <label htmlFor="name" className="input-label">
              Source Name:
              <input 
                type="text" 
                id="name" 
                forName="name" 
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
        {sources.length ? 
          sources.map((i) => (
            <OutputItem 
              key={i.id}
              id={i.id}
              name={i.name}
              email={i.email}
              deleteSource={deleteSource}
            />
          ))
          :
          <p></p>
        }
      </div>
    </>
  );
};
