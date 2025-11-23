export default function OutputItem({ id, name, email, editSource, deleteSource }) {
  return (
    <div className="output-item">
      <div className="output-text">{id}</div>
      <div className="output-text">{name}</div>
      <div className="output-email">{email}</div>
      <div className="output-item-buttons">
        {/* <button 
        onClick={() => editSource(id)}
        className="edit-btn"
        >
          EDIT
        </button> */}
        <button 
          onClick={() => deleteSource(id)}
          className="delete-btn"
        >
          DELETE
        </button>
      </div>
    </div>
  );
};
