import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { newTask } from './counterSlice'

export function Counter() {
  // const count = useSelector((state) => state.counter.value)
  const mass = useSelector((state) => state.counter.mass)
  const dispatch = useDispatch()
  let createTasks = function () {
    let text_in_input = document.querySelector('#new_todo').value
    // mass.push(text_in_input)

    dispatch(newTask(text_in_input))
  }
  console.log(mass)

  return (
    <div>
      <div>
        <input type="" name="" id='new_todo'></input>
        <button aria-label="Decrement value" onClick={() => createTasks()}> Добавить задачу </button>
        {/* <span>{count}</span> */}
        <span>{mass}</span>
        {/* <button aria-label="Increment value" onClick={() => dispatch(increment())}> Increment </button> */}
      </div>
    </div>
  )
}