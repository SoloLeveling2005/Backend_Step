import {CreateFetchTodo} from "../store/ToDoReducer";

export const fetchGetTodos = () => {
    return function (dispatch: any) {
        fetch('http://127.0.0.1:8000/api/')
            .then(response => response.json())
            .then(json => {
                dispatch(CreateFetchTodo(json))
                console.log(json)
            })
            .then(() => console.log("get"))
    }
}

export const fetchPostTodos = (title:string) => {
    return function (dispatch: any) {
        const requestOptions = {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              title: title,
              // comment: 'test comment',
            }),
        };
        fetch('http://127.0.0.1:8000/api/', requestOptions)
            .then(() => {
                // dispatch(CreateFetchTodo(title))
                console.log(title)
            })
            .then(() => console.log("post"))
    }
}

export const fetchDeleteTodos = (id:string) => {
    return function (dispatch: any) {
        const requestOptions = {
            method: 'DELETE',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              id: id,
              // comment: 'test comment',
            }),
        };
        fetch('http://127.0.0.1:8000/api/', requestOptions)
            .then(() => {
                // dispatch(CreateFetchTodo(title))
                console.log(id)
            })
            .then(() => console.log("delete"))
    }
}