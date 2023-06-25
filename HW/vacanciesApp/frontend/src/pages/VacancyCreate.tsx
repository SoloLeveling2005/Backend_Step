import React, {useEffect, useState} from 'react';
import axios from "axios";
import {Link, redirect, useNavigate} from "react-router-dom";

function Vacancy(props: any) {
    const navigate = useNavigate();

    const [inputTitle, setInputTitle] = useState('');
    const handleInputTitle = (event: any) => {
        setInputTitle(event.target.value);
    };

    const [inputDescription, setInputDescription] = useState('');
    const handleInputDescription = (event: any) => {
        setInputDescription(event.target.value);
    };

    const [inputRate, setInputRate] = useState('');
    const handleInputRate = (event: any) => {
        setInputRate(event.target.value);
    };

    function create() {
        console.log(inputTitle,inputDescription,inputRate)
        axios.post('http://127.0.0.1:8000/api/create/', {
            title:inputTitle,
            description:inputDescription,
            rate:inputRate,
            headers: {
                // 'content-type': 'multipart/form-data',
                'Accept':'application/json',
                'Content-Type': 'application/json',
            },
        }).then(response=>{
            navigate("/");
        }).catch(error=>{
            console.log(error)
        })
    }


    return (
        <section>
            <div className="py-2 text-white bg-dark">
                <div className="container d-flex justify-content-between align-items-center">
                    <h2></h2>
                    <Link to="/" className="btn text-white">На главную</Link>
                </div>
            </div>
            <div className="container py-3">
                <input type="text" className="form-control my-1" placeholder="Название" onChange={handleInputTitle}/>
                <input type="text" className="form-control my-1" placeholder="Описание" onChange={handleInputDescription}/>
                <input type="text" className="form-control my-1" placeholder="Зарплата" onChange={handleInputRate}/>
                <button className="btn btn-success w-100" onClick={create}>Создать</button>
            </div>
        </section>

    );
};

export default Vacancy;
