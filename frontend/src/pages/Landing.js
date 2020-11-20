import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../assets/images/header.png'

function Landing() {
    return (
        <>
            <div className="container-fluid">
                <main className="landing row d-flex align-items-center">
                    <div className="col-6 title">
                        <svg width="4em" height="4em" viewBox="0 0 16 16" class="bi bi-cash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M15 4H1v8h14V4zM1 3a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1H1z" />
                            <path d="M13 4a2 2 0 0 0 2 2V4h-2zM3 4a2 2 0 0 1-2 2V4h2zm10 8a2 2 0 0 1 2-2v2h-2zM3 12a2 2 0 0 0-2-2v2h2zm7-4a2 2 0 1 1-4 0 2 2 0 0 1 4 0z" />
                        </svg>
                        <h1>Ganhar um dinheiro extra na internet nunca ficou mais fácil!</h1>
                        <p>Você no Magalu: uma plataforma criada para conectar vendedores com o Magazine Luiza de forma digital e prática.</p>
                        <button className="btn btn-dark my-2 my-sm-0" type="submit">
                            <Link to="/login">
                                Começar Agora
                            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z" />
                                </svg>
                            </Link>
                        </button>
                    </div>
                    <div className="col-6">
                        <img src={Header} alt="Header" />
                    </div>
                </main>
            </div>
        </>
    );
}

export default Landing;