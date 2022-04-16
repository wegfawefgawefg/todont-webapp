import '../assets/win95.css';

import React from 'react';

/*
at the top is a button for creating a new todont, 
it just involves a description

this page has a list of todonts that it gets from the server. 
Todont is a component that is used to display a single todont.

completed todonts are in a different list
which is rendered below the list of uncompleted todonts

it has a time created, a description, and a checkbox.
if you check the checkbox, it should tell the server to set that todont to done.
then reload the todonts.
*/

import ToDont from '../components/ToDont';

// center the page
const toDontsWindowStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    // move the window to the center of the screen
    position: 'absolute',
    top: '25%',
    left: '25%',
    // height: '20vh',
    width: '50%',
    backgroundColor: 'lightgrey',
    border: '1vw solid darkgrey',
};

// remove the dots from the list
const listStyle = {
    listStyle: 'none',
    padding: 0,
    margin: 0
};


export default function Index() {
    let todont_ex = {
        "id": "1",
        "description": "test",
        "created_at": 100,
        "done": false
    };

    // get time in hours, minutes, and seconds
    let currentTime = new Date(new Date().getTime()).toLocaleTimeString();

  return (
      <div>
        <div class="container">
            <div class="row mb-5">
            </div>
        </div>
        <div class="container">
            <div class="card mb-4">
                <div class="card-header">
                    <h4 class="my-0 font-weight-normal">ToDonts</h4>
                </div>
                <div class="card-body">
                    {/* <button>Create a new todont</button> */}
                    <ul style={listStyle}>
                        <li><ToDont todont={todont_ex}/></li>
                        <li><ToDont todont={todont_ex}/></li>
                        <li><ToDont todont={todont_ex}/></li>
                        <li><ToDont todont={todont_ex}/></li>
                    </ul>
                </div>
            </div>
        </div>
        <footer class="taskbar">
            <div class="row" >
                <div class="col-8">
                    <a href="/" class="btn start-button">Start</a>
                </div>
                <div class="col-4 time">{currentTime}</div>
            </div>
        </footer>
      </div>
    );
};