import React from 'react'

export default function OutputItem({ id, name, email }) {
  return (
    <div class="output-item">
      <div class="output-text">{id}</div>
      <div class="output-text">{name}</div>
      <div class="output-email">{email}</div>
      <button class="delete-btn">DELETE</button>
    </div>
  )
}
