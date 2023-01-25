import { createSlice } from '@reduxjs/toolkit'

export const counterSlice = createSlice({
  name: 'counter',
  initialState: {
    mass: ["1","2"]
  },
  reducers: {
    newTask: (state, actions) => {
      console.log(actions.payload)
      state.mass.push(actions.payload)
    },
  },
})

// Action creators are generated for each case reducer function
export const { newTask } = counterSlice.actions

export default counterSlice.reducer