/*
this is a todont component

it has a time created, a description, and a checkbox.
if you check the checkbox, it should tell the server to set that todont to done.
then reload the todonts.
*/
import '../assets/win95.css';

import React from 'react'

// everything should be grey like windows 95

const toDontStyle = {
    display: 'flex',
    flexDirection: 'row',
    // add more space between the elements
    justifyContent: 'space-between',
    alignItems: 'center',
    margin: '20px',
    padding: '10px',
    border: '0px solid black',
    backgroundColor: '#e0e0e0'
};

const descriptionStyle = {
    fontSize: '20px',
    // add left and right margins
    marginLeft: '100px',
    marginRight: '100px',
    padding: '10px',
    backgroundColor: '#e0e0e0'
};


const ToDont = ({ todont, onCheck }) => {
    let dateFromUTSInt = new Date(todont.created_at).toLocaleString();
    console.log(dateFromUTSInt);

    return (
        <div className="todont" 
            // style={toDontStyle}
            >
            {/* <div className="todont-created-at">{dateFromUTSInt}</div> */}
            {/* put the description on the next line */}
            {/* <div className="todont-description" style={descriptionStyle}>{todont.description}</div> */}
            {/* <input type="checkbox" checked={todont.done} onChange={() => onCheck(todont.id)} /> */}
            <form>
                <div class="form-group row">
                    <div class="col-sm-4">{dateFromUTSInt}</div>
                    <div class="col-sm-6">{todont.description}</div>
                    <div class="col-sm-2">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="gridCheck1">
                            </input>
                            <label class="form-check-label" for="gridCheck1">
                                Done
                            </label>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    )
};

export default ToDont;