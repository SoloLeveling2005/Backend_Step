const newTodo = "newTodo"
const deleteTodos = "deleteTodos"
const fetchTodo = "fetchTodo"


// action = {type:"", payload:""}
const defaultState = {
    todos: [],
}

export const reducer = (state = defaultState, action:any) => {
    switch (action.type) {
        case newTodo:
            let now = new Date().getTime();
            // @ts-ignore
            state.todos.push({id: now, title: action.payload})

            // @ts-ignore
            return {...state, todos: state.todos}
        case fetchTodo:
            state.todos = []
            for (let todo of action.payload)  {
                // @ts-ignore
                state.todos.push(todo)
            }
            console.log(state.todos)
            state.todos = [...state.todos]
            // @ts-ignore
            return {...state}
        case deleteTodos:
            const todos_ = [...state.todos]
            // @ts-ignore
            todos_.splice(state.todos.findIndex(v => v.id === action.payload), 1);
            state.todos = todos_
            return {...state}
        default:
            return state
    }
}


export const CreateFetchTodo = (payload: any) => ({type: fetchTodo, payload})
export const CreateTodo = (payload: any) => ({type: newTodo, payload})
export const DeleteTodo = (payload: any) => ({type: deleteTodos, payload})
