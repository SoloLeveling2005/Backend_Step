import React from 'react';
// import logo from './logo.svg';
// import { Counter } from './features/counter/Counter';
import './../App.css';
import {useDispatch, useSelector} from "react-redux";

function ToDo() {

    const [newTodoText, setInputValue] = React.useState("");

    const changeTextNewTodo = (event:any) => {
       setInputValue(event.target.value);
    };

    const dispatch = useDispatch()
    // @ts-ignore
    const todos = useSelector(state => state.todos)
    // @ts-ignore
    const ids = useSelector(state => state.id_)

    const newTodo = () => {
        if (!newTodoText) return
        dispatch({type:'newTodo', payload:`${newTodoText}`})
        setInputValue("");
    }
    const deleteTodo = (id_:string) => {
        dispatch({type:'deleteTodos', payload:id_})
        // setInputValue("");
    }

    let res = todos.map(function(todo:any) {
          return <div key={todo.id} className={'card'}>
              <span>{todo.title}</span>
              <button
                  type="button"
                  className="btn-close"
                  aria-label="Close"
                  onClick={() => deleteTodo(todo.id)}></button>
          </div>;
       });

  return (
    <div className="App">
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
        {/*{listItems}*/}
        {res}

    </div>

  );
}

export default ToDo;
