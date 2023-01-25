import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { newTask } from './counterSlice'

export function Counter() {
  // const count = useSelector((state) => state.counter.value)
  const mass = useSelector((state) => state.counter.mass)
  const dispatch = useDispatch()

  return (
    <div>
      <div>
        <input type="" name="" value="" id='new_todo'></input>
        <button aria-label="Decrement value" onClick={() => dispatch(newTask())}> Добавить задачу </button>
        {/* <span>{count}</span> */}
        <span>{mass}</span>
        {/* <button aria-label="Increment value" onClick={() => dispatch(increment())}> Increment </button> */}
      </div>
    </div>
  )
}