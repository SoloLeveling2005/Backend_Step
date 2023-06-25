import React, {useEffect, useState} from 'react';
import axios from "axios";
import {useParams} from "react-router";
import {Link} from "react-router-dom";
interface MatchParams {
  dynamicParam: string;
}

function Vacancy(props: any) {
    let { id } = useParams();
    const vacancyId = id;
    const [vacancy, changeVacancy] = useState({id:0, title:'', description:'', rate:0});


    useEffect(()=>{
        axios.get(`http://127.0.0.1:8000/api/vacancy/${vacancyId}/`, {}).then((response)=>{
            console.log(response)
            changeVacancy(response.data)
        }).catch((error)=>{
            console.log(error)
        });
    }, []);

    return (
        <section>
            <div className="py-2 text-white bg-dark">
                <div className="container d-flex justify-content-between align-items-center">
                    <h2>{vacancy.title}</h2>
                    <Link to="/" className="btn text-white">На главную</Link>
                </div>
            </div>
            <div className="container mt-3">
                <h4>Описание: {vacancy.description}</h4>
                <h4>Оклад: {vacancy.rate}</h4>
            </div>
        </section>

    );
};

export default Vacancy;
