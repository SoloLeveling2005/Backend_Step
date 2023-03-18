import React from 'react';
import './App.css';

function App() {
  return (
    <div className="tasks">
        <div className="header">
            <h4>TODO LIST</h4>
        </div>
        <div className="main">
            <div className="">
                <form action="{% url 'django_api:task' id=0 user_id=user_id %}" method="POST">
                    {/* {% csrf_token %} */}
                    <div className="input-group flex-nowrap">
                        <input type="text" className="form-control" placeholder="Введите название задачи" name="title" onChange=""></input>

                        <button type="submit" className="btn btn-success">Создать</button>
                    </div>
                </form>
            </div>
            
            {/* {% for i in todos %} */}
            
            <div className="task" id="{{i.id}}">
                <form action="{% url 'django_api:task' id=i.id user_id=i.user_id %}" method="POST" className="d-flex align-items-center justify-content-between wert">
                    {/* {% csrf_token %} */}
                    <div className="form-group w-100">
                        <input type="hidden" name="_method" defaultValue="DELETE"></input>
                        <input type="text" className="form-control qwer" onChange="123"></input>
                    </div>
                    <button type="submit" className="btn btn-danger delete" >Удалить</button>
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
  );
}

export default App;
