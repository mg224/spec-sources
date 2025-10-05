import React from 'react'
import OutputItem from './OutputItem'

export default function Form() {
  return (
    <>
      <div>
        <form action="" class="form">
          <div class="input-div">
          <label for="name">Source Name: </label>
          <input type="text" id="name" name="name" class="input-item" />
          </div>

          <div class="input-div">
          <label for="email">Source Email: </label>
          <input type="email" id="email" name="email" class="input-item" />
          </div>

          <button type="submit" class="submit-btn">ADD</button>
        </form>
      </div>

      <div class="output-list">
        <OutputItem 
          id={1}
          name={"Presbo"}
          email={"presbo@columbia.edu"}
        />

        <OutputItem 
          id={2}
          name={"John Jay Mouse"}
          email={"mouse@columbia.edu"}
        />

        <OutputItem 
          id={3}
          name={"Water Bottle Man"}
          email={"flipper@columbia.edu"}
        />
      </div>
    </>
  )
}
