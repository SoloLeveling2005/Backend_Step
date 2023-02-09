import {CreateFetchTodo, DeleteTodo} from "../store/ToDoReducer";
import axios from 'axios';
import Cookies from 'js-cookie';

export const fetchGetTodos = () => {
    return function (dispatch: any) {
        fetch('http://127.0.0.1:8000/apii/api/')
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
        let cookie_data = {csrf_token: Cookies.get('csrftoken')}
        const requestOptions = {
            method: 'POST',
            headers: {
                'X-CSRFToken': cookie_data.csrf_token,
                // 'content-type': 'multipart/form-data',
                'Content-Type': 'application/json',

            },
            body: JSON.stringify({
              title: title,
              // comment: 'test comment',
            }),
        };
        console.log(cookie_data)
        // @ts-ignore
        fetch('http://127.0.0.1:8000/apii/api/', requestOptions)
            .then(data => {
                // @ts-ignore
                const response = data.json()
                console.log(response)
                response.then((value) => {
                    dispatch(CreateFetchTodo(value))
                })

            })
            .then(() => console.log("create"))
    }
}

export const fetchDeleteTodos = (id:string) => {
    return function (dispatch: any) {
        let cookie_data = {csrf_token: Cookies.get('csrftoken')}
        const requestOptions = {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': cookie_data.csrf_token,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              id: id,
            }),
        };
        // @ts-ignore
        fetch('http://127.0.0.1:8000/apii/api/', requestOptions)
            .then(data => {
                const response = data.json()
                console.log(response)
                response.then((value) => {
                    dispatch(CreateFetchTodo(value))
                })
            })
            .then(() => console.log("delete"))
            .then(() => dispatch(fetchGetTodos()))
    }
}