import React, {useEffect} from 'react';
import './../App.css';
import {useDispatch, useSelector} from "react-redux";
// import axios from "axios";
import {fetchDeleteTodos, fetchGetTodos, fetchPostTodos} from "../asyncAction/customers";
import {useCookies} from 'react-cookie';

function ToDo() {
    let [cookies, setCookie, removeCookie] = useCookies(['csrftoken']);

    const [title_, changeTitle_] = React.useState("");
    const [description_, changeDescription_] = React.useState("");

    const dispatch = useDispatch()

    // @ts-ignore
    const todos = useSelector(state => state.todos)


    const changeTitleNewTodo = (event:any) => {
       changeTitle_(event.target.value);
    };
    const changeDescriptionNewTodo = (event:any) => {
       changeDescription_(event.target.value);
    };

    const newTodo = () => {
        if (!title_) return
        dispatch({type:'newTodo', payload:{'title':title_,'description':description_}})
        // @ts-ignore
        dispatch(fetchPostTodos({'title':title_,'description':description_}))
        changeTitle_("");
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

    return (
        <div className="App" >
            <form>
                <div className="mb-3">
                    <label htmlFor="exampleInputTitle" className="form-label">Введите название задачи</label>
                    <input type="text"
                           className={"form-control form-new-title"}
                           id="exampleInputTitle"
                           aria-describedby="emailHelp"
                           onChange={changeTitleNewTodo}
                           value={title_}/>
                    <input type="text"
                           className="form-control"
                           id="exampleInputTitle"
                           aria-describedby="emailHelp"
                           onChange={changeDescriptionNewTodo}
                           value={description_}/>
                    {title_}
                    {description_}
                </div>
                <button type="button" className="btn btn-primary w-100" onClick={() => newTodo()}>Создать</button>
            </form>
            {todos.map((todo: any) =>
                <div key={todo.id} className={'card'}>
                    <span>{todo.title}</span>
                    <span>{todo.description}</span>
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
