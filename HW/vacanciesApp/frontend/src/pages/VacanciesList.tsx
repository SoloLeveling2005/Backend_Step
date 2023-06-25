import React, {useEffect, useState} from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import {Link} from "react-router-dom";


function VacanciesList(props: any) {

    const [vacancies, changeVacancies] = useState([{id:0,title:'', description:'', rate:0}]);


    useEffect(()=>{
        axios.get(`http://127.0.0.1:8000/api/vacancies/`, {
            headers: {
                // 'content-type': 'multipart/form-data',
                'Content-Type': 'application/json',

            },
        }).then(response=> {
            console.log(response)
            changeVacancies(response.data)
        }).catch(error=>{
            console.log(error)
        });
    }, []);

    return (
        <section className="container mt-3">
            <h2 className="mb-4">Топ вакансий <a href="/create" className="btn btn-primary">Добавить</a></h2>
            {vacancies.map((item, index)=>(
                <Link to={`/vacancy/${item.id}`} className="card mb-3">
                    <div className="card-header">
                        {item.title}
                    </div>
                    <div className="card-body">
                        <blockquote className="blockquote mb-0">
                            <p>{item.description}</p>
                            <footer className="blockquote-footer">Оклад: {item.rate}</footer>
                        </blockquote>
                    </div>
                </Link>
            ))}

        </section>
    );
};

export default VacanciesList;
