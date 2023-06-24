import React, {useEffect, useState} from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';


function VacanciesList(props: any) {

    const [vacancies, changeVacancies] = useState([]);


    useEffect(()=>{
        // Получение CSRF-токена из cookie
        const csrftoken = Cookies.get('csrftoken');

        // Отправка запроса с CSRF-токеном
        axios.defaults.headers.common['X-CSRFToken'] = csrftoken;
        let cookie_data = {csrf_token: Cookies.get('csrftoken')}
        axios.get(`http://127.0.0.1:8000/api/vacancies`, {
            headers: {
                'X-CSRFToken': cookie_data.csrf_token,
                // 'content-type': 'multipart/form-data',
                'Content-Type': 'application/json',

            },
        }).then(response=> {
            console.log(response)
        }).catch(error=>{
            console.log(error)
        });
    });

    return (
        <section className="container mt-3">
            <h2 className="mb-4">Топ вакансий</h2>
            {vacancies.map((item, index)=>(
                <div className="card">
                    <div className="card-header">
                        Quote
                    </div>
                    <div className="card-body">
                        <blockquote className="blockquote mb-0">
                            <p>A well-known quote, contained in a blockquote element.</p>
                            <footer className="blockquote-footer">Someone famous in <cite title="Source Title">Source
                                Title</cite></footer>
                        </blockquote>
                    </div>
                </div>
            ))}

        </section>
    );
};

export default VacanciesList;
