import React, {useEffect} from 'react';
import './../App.css';
import {useDispatch, useSelector} from "react-redux";
// import axios from "axios";
import {fetchDeleteTodos, fetchGetTodos, fetchPostTodos} from "../asyncAction/customers";
import {useCookies} from 'react-cookie';

function ToDo() {
    let [cookies, setCookie, removeCookie] = useCookies(['csrftoken']);

    const [newTodoText, setInputValue] = React.useState("");
    const [dataTodos, setDataTodos] = React.useState([]);
    const dispatch = useDispatch()
    // @ts-ignore
    const todos = useSelector(state => state.todos)


    const changeTextNewTodo = (event:any) => {
       setInputValue(event.target.value);
    };

    const newTodo = () => {
        if (!newTodoText) return
        dispatch({type:'newTodo', payload:`${newTodoText}`})
        // @ts-ignore
        dispatch(fetchPostTodos(newTodoText))
        setInputValue("");
        // @ts-ignore

    }

    const deleteTodo = (id_:string) => {
        dispatch({type:'deleteTodos', payload:id_})
        // @ts-ignore
        dispatch(fetchDeleteTodos(id_));
    }

    useEffect(() => {
        console.log("start")
        // @ts-ignore
        dispatch(fetchGetTodos())
        console.log('end')
    }, []);

    console.log(cookies)

    // @ts-ignore
    const {name} = cookies;
    return (
        <div className="App" >
            <form>

                <div className="mb-3">
                    <label htmlFor="exampleInputTitle" className="form-label">Введите название задачи</label>
                    <input type="text"
                           className="form-control"
                           id="exampleInputTitle"
                           aria-describedby="emailHelp"
                           onChange={changeTextNewTodo}
                           value={newTodoText}/>
                    {name}
                </div>
                <button type="button" className="btn btn-primary w-100" onClick={() => newTodo()}>Создать</button>
            </form>
            {todos.map((todo: any) =>
                <div key={todo.id} className={'card'}>
                    <span>{todo.title}</span>
                    {todo.id}
                    <button
                        type="button"
                        className="btn-close"
                        aria-label="Close"
                        onClick={() => deleteTodo(todo.id)}></button>
                </div>
            )}
        </div>

    );
}

export default ToDo;
