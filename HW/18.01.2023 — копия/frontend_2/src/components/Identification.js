// import logo from './logo.svg';
import '../App.css';


function Identification() {
  return (
    <div>
        <header>
            <h2>Todo</h2>
        </header>
        <div class="body">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal_reg">
                <h4>Регистрация</h4>
            </button>
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal_auth">
                <h4>Авторизация</h4>
            </button>
            {/* <!-- Modal --> */}
            <div class="modal fade" id="exampleModal_reg" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel_reg">Регистрация</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form action="{% url 'authentication:index' %}" method="POST">
                    {/* {% csrf_token %} */}
                    <div class="modal-body">

                        <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Username</label>
                        <input type="text" name="username" autocomplete="off" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"></input>
                        <div id="emailHelp" class="form-text">We'll never share your Username with anyone else.</div>
                        </div>
                        <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" name="password" autocomplete="off"  class="form-control" id="exampleInputPassword1"></input>
                        </div>
            {/* <!--          <div class="mb-3 form-check">--> */}
            {/* <!--            <input type="checkbox" class="form-check-input" id="exampleCheck1">--> */}
            {/* <!--            <label class="form-check-label" for="exampleCheck1">Check me out</label>--> */}
            {/* <!--          </div>--> */}

                    </div>
                    <div class="modal-footer">
                    <input type="hidden" name="reg" value="reg"></input>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
                    </div>
                </form>
                </div>
            </div>
            </div>
            <div class="modal fade" id="exampleModal_auth" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel_auth">Авторизация</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form action="{% url 'authentication:index' %}" method="POST">
                    {/* {% csrf_token %} */}
                    <div class="modal-body">

                        <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Username</label>
                        <input type="text" name="username" autocomplete="off" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"></input>
            {/* <!--            <div id="emailHelp" class="form-text">We'll never share your Username with anyone else.</div>--> */}
                        </div>
                        <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" name="password" autocomplete="off" class="form-control" id="exampleInputPassword1"></input>
                        </div>
                    </div>
                    <div class="modal-footer">
                    <input type="hidden" name="auth" value="auth"></input>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-primary">Авторизоваться</button>
                    </div>
                </form>
                </div>
            </div>
            </div> 
        </div>
        
    </div>
  );
}
export default Identification;