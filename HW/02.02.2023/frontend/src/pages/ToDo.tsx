import React, {useEffect} from 'react';
import './../App.css';
import {useDispatch, useSelector} from "react-redux";
// import axios from "axios";
import {fetchDeleteTodos, fetchGetTodos, fetchPostTodos, fetchUpdateTodos} from "../asyncAction/customers";
import {useCookies} from 'react-cookie';
import {Link} from "react-router-dom";

function ToDo() {
    let [cookies, setCookie, removeCookie] = useCookies(['csrftoken']);

    const [title_, changeTitle_] = React.useState("");
    const [description_, changeDescription_] = React.useState("");

    const [editingTitle_, changeEditingTitle_] = React.useState("");
    const [editingDescription_, changeEditingDescription_] = React.useState("");
    const [editingId_, changeEditingId_] = React.useState("");
    const [checkBlock_, changeCheckBlock_] = React.useState(false);


    const dispatch = useDispatch()

    // @ts-ignore
    const posts = useSelector(state => state.todos)

    // control function
    const changeTitleNewTodo = (event:any) => {
       changeTitle_(event.target.value);
    };
    const changeDescriptionNewTodo = (event:any) => {
       changeDescription_(event.target.value);
    };
    // const changeEditingId = (event:any) => {
    //     changeEditingId_(event.target.id)
    //     console.log(event.target.id)
    // }
    const changeEditingTitle = (event:any) => {
        changeEditingTitle_(event.target.value)
    }
    const changeEditingDescription = (event:any) => {
        changeEditingDescription_(event.target.value)
    }


    // event function
    const applyChange = () => {
        // console.log(editingTitle_)
        // console.log(editingDescription_)
        // console.log(editingId_)
        // @ts-ignore
        dispatch(fetchUpdateTodos([editingId_,editingTitle_,editingDescription_]))
        changeEditingTitle_('')
        changeEditingDescription_('')
        changeCheckBlock_(false)
    }

    const changePost = (e:any, id_:string) => {
        if (e.target.id === "del-post") return
        // console.log(id_)
        for (let i of posts) {
            if (i['id'] === id_) {
                changeEditingTitle_(i['title'] )
                changeEditingDescription_(i['description'] )
                break
            }
        }
        changeCheckBlock_(true)
        changeEditingId_(id_)
    }

    const blockChanges = (e:any) => {
        // console.log(e.target)
        if (e.target.id === "block-changes-bottom") changeCheckBlock_(false)
    }


    // making function
    const newTodo = () => {
        if (!title_) return
        dispatch({type:'newTodo', payload:[title_,description_]})
        // @ts-ignore
        dispatch(fetchPostTodos([title_,description_]))
        changeTitle_("");
        changeDescription_("");
        // @ts-ignore
    }

    const deleteTodo = (id_:string) => {
        dispatch({type:'deleteTodos', payload:id_})
        // @ts-ignore
        dispatch(fetchDeleteTodos(id_));
    }

    useEffect(() => {
        // console.log("start")
        // @ts-ignore
        dispatch(fetchGetTodos())
        // console.log('end')
    }, []);

    return (
        <div className="App" >
            <header className="header d-flex justify-content-center py-3">
                <ul className="nav nav-pills">
                    <Link to={`/`}><a href="#" className="nav-link " aria-current="page">Home</a></Link>
                    <li className="nav-item"><a href="#" className="nav-link active">ToDo</a></li>
                </ul>
            </header>
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
                </div>
                <button type="button" className="btn btn-primary w-100" onClick={() => newTodo()}>Создать</button>
            </form>
            {posts.map((todo: any) =>
                <div key={todo.id} id={todo.id} className={'card'}  onClick={(e) => changePost(e, todo.id)}>
                    <span className={'info-post'}>{todo.title}</span>
                    <span className={'info-post'}>{todo.description}</span>
                    <button
                        type="button"
                        className="btn-close"
                        aria-label="Close"
                        id='del-post'
                        onClick={() => deleteTodo(todo.id)}
                    ></button>
                </div>

            )}
            {checkBlock_
                ? <div className="block-changes" id='block-changes-bottom' onMouseDown={(e) => blockChanges(e)}>
                    <div className="in" id='block-changes-top'>
                        <input type="text" value={editingTitle_} onChange={changeEditingTitle}/>
                        <input type="text" value={editingDescription_} onChange={changeEditingDescription}/>
                        <button className="btn btn-success" onClick={applyChange}>Сохранить изменения</button>
                    </div>
                </div>
                :
                ""
            }
        </div>

    );
}

export default ToDo;
