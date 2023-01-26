import { createSlice } from '@reduxjs/toolkit'

export const counterSlice = createSlice({
  name: 'counter',
  initialState: {
    mass: []
      
  },
  reducers: {
    newTask: (state, actions) => {
      console.log(actions.payload)
      console.log(typeof(state.mass))
      state.mass.push({
        "id":state.mass.length,
        "title": actions.payload,
        "description": "description"
      })
    },
    fetchTasksCreator: (state, action) => {
      console.log(...action.payload)
      state.mass = [...action.payload]
    },
    cleanTasks: (state) => {
      state.mass = []
    }
  },
})

// Action creators are generated for each case reducer function
export const { newTask, fetchTasksCreator } = counterSlice.actions

export default counterSlice.reducer