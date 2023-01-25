import { createSlice } from '@reduxjs/toolkit'

export const counterSlice = createSlice({
  name: 'counter',
  initialState: {
    mass: ["1"]
  },
  reducers: {
    newTask: (state) => {
      state.mass.push("1")
    },
  },
})

// Action creators are generated for each case reducer function
export const { newTask } = counterSlice.actions

export default counterSlice.reducer