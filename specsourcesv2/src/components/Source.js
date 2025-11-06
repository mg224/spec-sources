export default function OutputItem({ id, name, email, deleteSource }) {
  return (
    <div className="output-item">
      <div className="output-text">{id}</div>
      <div className="output-text">{name}</div>
      <div className="output-email">{email}</div>
      <button 
        onClick={() => deleteSource(id)}
        className="delete-btn"
      >
        DELETE
      </button>
    </div>
  );
};
