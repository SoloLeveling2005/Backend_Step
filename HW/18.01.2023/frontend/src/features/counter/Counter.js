import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { newTask } from './counterSlice'
import '../../App.css';


export function Counter() {
  // const count = useSelector((state) => state.counter.value)
  const mass = useSelector((state) => state.counter.mass)
  const dispatch = useDispatch()

  let createTasks = function () {
    let text_in_input = document.querySelector('#new_todo').value
    dispatch(newTask(text_in_input))
  }

  return (
    <div class="tasks">
        <div class="header">
            <h4>TODO LIST</h4>
        </div>
        <div class="main">
            <div class="">
                <form action="{% url 'django_api:task' id=0 user_id=user_id %}" method="POST">
                    {/* {% csrf_token %} */}
                    <div class="input-group flex-nowrap">
                        <input type="text" class="form-control" placeholder="Введите название задачи" name="title"></input>

                        <button type="submit" class="btn btn-success">Создать</button>
                    </div>
                </form>
            </div>
            
            {/* {% for i in todos %} */}
            
            <div class="task" id="{{i.id}}">
                <form action="{% url 'django_api:task' id=i.id user_id=i.user_id %}" method="POST" class="d-flex align-items-center justify-content-between form-37">
                    {/* {% csrf_token %} */}
                    <div class="form-group w-100">
                        <input type="hidden" name="_method" value="DELETE"></input>
                        <input type="text" class="form-control input-41" value="{{i.title}}"></input>
                    </div>
                    <button type="submit" class="btn btn-danger button-1">Удалить</button>
                  </form>
                {/* <!-- <form action="" method="UPDATE" class="w-100" content>

                            <div class="form-group">
                              <label>{{i.title}}</label>
                              <input type="hidden" class="form-control" placeholder="Введите текст задачи">
                            </div>
                            <button type="submit" class="btn btn-danger">Удалить</button>

                </form> --> */}
            </div>
            {/* {% endfor %} */}
        </div>
        
    </div>
  )
}