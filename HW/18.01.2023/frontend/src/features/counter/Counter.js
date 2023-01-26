import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { newTask, fetchTasksCreator } from './counterSlice'
import '../../App.css';


export function Counter() {
  const [title, setTitle] = React.useState(''); 
  let mass = useSelector((state) => state.counter.mass)
  const dispatch = useDispatch()
  console.log(typeof(mass))

  let fetchTasks = () => {
    fetch("http://127.0.0.1:8000/api/user/1/tasks")
    .then(res => res.json())
    .then(results => dispatch(fetchTasksCreator(results)))
  }
  let createTasks = function () {
    dispatch(newTask(title))
    setTitle('');

    let data = {
      "title": title,
    };
    
    fetch('http://127.0.0.1:8000/api/user/1/task/1/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(data)
    });
    // setTimeout(1000, fetchTasks())
  }
  

  let deleteTask = (del_id) => {
    fetch('http://127.0.0.1:8000/api/user/1/task/'+del_id+'/', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      }
    });
    console.log(del_id)
    setTimeout(1000, fetchTasks())
    
  }

  React.useEffect(() => {
    fetchTasks()
  }, [])

  
  return (
    <div className="tasks">
        <div className="header">
            <h4>TODO LIST</h4>
        </div>
        <div className="main">
            <div className="">
                <form>
                    <div className="input-group flex-nowrap">
                        <input type="text" onChange={(e) => setTitle(e.target.value)} value={title} className="form-control" placeholder="Введите название задачи" name="title" id="new_todo" />
                        <button type="button" className="btn btn-success" onClick={() => createTasks()}>Создать</button>
                    </div>
                </form>
            </div>
            {/* {mass} */}
            {mass.map(element => (
              
              <div className="task" id={element.id}>
                <form className="d-flex align-items-center justify-content-between form-37">
                    <div className="form-group w-100">
                        <input type="hidden" name="_method" value="DELETE"></input>
                        <input type="text" className="form-control input-41" value={element.title}></input>
                    </div>
                    <button type="button" className="btn btn-danger button-1" onClick={() => deleteTask(element.id)}>Удалить</button>
                  </form>
              </div>
            ))}
            
        </div>
        
    </div>
  )
}