import React, {useEffect} from 'react';
import './../App.css';
import {useDispatch, useSelector} from "react-redux";
// import axios from "axios";
import {fetchGetTodos, fetchPostTodos, fetchDeleteTodos} from "../asyncAction/customers";


function ToDo() {
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
    }

    const deleteTodo = (id_:string) => {
        dispatch({type:'deleteTodos', payload:id_})
        // @ts-ignore
        dispatch(fetchDeleteTodos(id_))
    }

    useEffect(() => {
        console.log("start")
        // @ts-ignore
        dispatch(fetchGetTodos())
        console.log('end')
    }, [dataTodos]);

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
                </div>
                <button type="button" className="btn btn-primary w-100" onClick={() => newTodo()}>Добавить</button>
            </form>
            {todos.map((todo: any) => 
                <div key={todo.id} className={'card'}>
                    <span>{todo.title}</span>
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
