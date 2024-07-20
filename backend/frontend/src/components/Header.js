import {useState} from 'react';
import './Header.css'
function Header(){

    const [trackName,setName]=useState('Around the World');
    const [clicked,setClicked]=useState(false);
    const [enteredText, setEnteredText] = useState('Search for a Song!'); 
    return(
        <div className='header'>
            <div className='title'>hum</div>
            <div className='align'>
            <input
            className='search'
                type="text"
                style={{color: clicked? 'white':'dimgrey'}}
                value={enteredText}
                //onClick={cleared?()=>{}:()=>{
                //    setEnteredText('');
                //    cleared=true;
                //}}
                onClick={()=>{
                    if(!clicked){
                        setEnteredText('');
                        setClicked(true);
                    }
                }}
                //above clears when clicked
                onChange={(e) => {
                    setEnteredText(e.target.value);
                    console.log(e.target.value);
                    //{*Next LINE CAN TRIGGER MANY RE-RENDERS*}
                    setName(e.target.value);
                }}
            />
            <button
                className='searchBtn'
                onClick={()=>{
                    //spotifyapi endpoint
                    fetch('http://127.0.0.1:8000/spotifyApp/', {
                        method: 'POST',
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify(trackName)
                    }).then((response)=>{
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                          }
                          return response.json(); // Parse the JSON data
                        }).then((data) => {
                          console.log('Success:', data); // Handle the JSON data
                        })
                        .catch((error) => {
                          console.error('Error:', error); // Handle any errors
                        });
                }}
            >Search</button>
            </div>
        </div>
    );
}
export default Header;