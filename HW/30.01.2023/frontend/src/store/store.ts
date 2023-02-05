import {applyMiddleware, createStore} from "@reduxjs/toolkit";
import {composeWithDevTools} from "redux-devtools-extension";
import thunk from "redux-thunk";
import {reducer} from './ToDoReducer'

// @ts-ignore
export const store:any = createStore(reducer, composeWithDevTools(applyMiddleware(thunk)))














