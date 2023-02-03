import {createStore} from "@reduxjs/toolkit";

// action = {type:"", payload:""}
const defaultState = {
    todos: [
        {
            id:0,
            title:"Первый"
        },
    ],
    id_:1
}
const reducer = (state = defaultState, action:any) => {
    switch (action.type) {
        case "newTodo":
            state.todos.push({id: state.id_, title: action.payload})
            state.id_ += 1
            // @ts-ignore
            return {...state, todos: state.todos}
        case "getTodos":
            return {...state}
        case "deleteTodos":
            const todos_ = [...state.todos]
            todos_.splice(state.todos.findIndex(v => v.id === action.payload), 1);
            state.todos = todos_
            return {...state}
        default:
            return state
    }
}


// @ts-ignore
export const store:any = createStore(reducer)

