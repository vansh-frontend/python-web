from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
      <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
*::selection{
    background-color: gray;
    color: #fff;
}
html{
    scroll-behavior: smooth;
}
/* scroll color change blue */
::-webkit-scrollbar{
    width: 7px;
    }
    ::-webkit-scrollbar-track{
        background-color:cornflowerblue;
        border-radius: 15px;
    
    }
    ::-webkit-scrollbar-thumb{
        background-color: #74797e;
        border-radius: 15px;
    }


/* font stye change */





body {
    font-family: 'Poppins', sans-serif;
    background-color:rgba(0,0,0,0.9);
    color:#fff;
    transition: background-color 0.5s;
    scroll-behavior: smooth;
    /* background-size: cover; */
}

/* Header css  */
header {
    background: linear-gradient(to right, #333, #1e1e1e);
    transition: background-color 0.5s;
    position: sticky;
    top: 0;
    z-index: 1000;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 80px;
    transition: height 0.5s, background-color 0.5s;
    z-index: 1000;
}


nav .left {
    font-size: 1.7rem;
    color: #fff;
    transition: color 0.5s;
}

nav ul {
    display: flex;
}

nav ul li {
    list-style: none;
    margin-right: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #fff;
    font-size: 1.2rem;
    transition: color 0.5s
}

nav ul li a:hover {
    color:#9933ff;
}
nav ul:hover  > :not(:hover)
{
    opacity: 0.2;   
}
    
/* Main tag css*/
main {
    padding: 50px;
}

/* Sections1 css*/
.firstsection {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 100px 0;
}
.purple{
    color:#aa6be4;
}
.firstsection .leftsection {
    width: 50%;
    font-size: 2rem;
    transition: transform 0.5s, opacity 0.5s;
}

.firstsection .leftsection p {
    transition: opacity 0.5s;
}

.firstsection .rightsection img {
    width: 100%;
    max-width:300px;
    height: auto;
    transition: transform 0.5s, opacity 0.5s;
}


.secondsection, .thirdsection, .fourthsection, .fifthsection {
    max-width: 800px;
    margin: auto;
    padding: 50px 0;
    transition: opacity 0.5s;
}

.secondsection hr, .thirdsection hr, .fourthsection hr, .fifthsection hr {
    border: 0;
    background: #9933ff;
    height: 2px;
    margin: 20px 0 40px;
    transition: background 0.5s;
}

.secondsection h1, .thirdsection h1, .fourthsection h1, .fifthsection h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    transition: color 0.5s;
}

.secondsection h1, .thirdsection h1,.fourthsection h1, .fifthsection h1, .text-gray{
    color: gray;
    transition: color 0.5s;
}

#about p{
    font-size: 20px;
    font-weight: 200;
    
}
.thirdsection ul, .fifthsection p {
    font-size: 1.3rem;
    transition: font-size 0.5s;
}

.fourthsection .project {
    margin-bottom: 40px;
    transition: transform 0.5s, opacity 0.5s;
}

.fourthsection .project h3 {
    font-size: 1.8rem;
    margin-bottom: 10px;
    transition: color 0.5s;
    color:#ccc;
}
.fourthsection .project p {
    font-size: 1.2rem;
    color: #ccc;
    transition: color 0.5s;
}
#services >  ul li{
    list-style: circle;
}
#projects > h1{
    color:#74797e;
    font-size: 31px;
}
#projects .project h3{
    color:#545252;
    font-size: 30px;
   font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 900;
    margin: 20px -20px;
   
  
}
#projects .project p{
    color:#fff;
    font-weight: 400;
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    margin: 0 -20px;
  
}



/* Typed.js */
#element {
    color: #aa6be4;
    font-size:30px;
    transition: color 0.5s;
}
.left{
    position: relative;
    color: transparent;
    margin: 20px 10px;

    
}

.left::before {
    content: 'Vansh\'s Portfolio';
    position: absolute;
    top: 0;
    left: 0;
    overflow: hidden;
    white-space: nowrap;
    color:#9933ff;
    animation: fillAnimation 3s linear infinite ;
}

@keyframes fillAnimation {
    0% {
        width: 0%;
    }
    100% {
        width: 100%;
    }
}
.sidebar{
    position: fixed;
    top:0;
    right: 0;
    height: 100vh;
    width: 250px;
    z-index: 1000;
    background-color:rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    box-shadow: -10px 0 10px rgba(0,0,0,0.1);
    display: none;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    justify-content: flex-start;
   border-radius: 15px;
   border:none;
   right: 90px;
   outline: 2px solid black;
   outline-offset:1px;
    filter:drop-shadow(2px 3px 2px black);
  
   }


 .btn button{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 700;
    justify-content: center;
    align-items: center;
    background-color:#9933ff;
    /* margin:20px 100px; */

 }


 .btn button:hover{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 100;
    background-color:#aa6be4;
   }

   .btnnn button:active{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 200;
    background-color:#aa6be4;
    transform: scale(0.87);
    outline: 2px solid #333;
    outline-offset: 2px;
   }
   

   

   .btnn button{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 700;
    justify-content: center;
    align-items: center;
    background-color:#9933ff;
    margin:20px 100px;
    display: none;
   }

   .btnn button:hover{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 100;
    background-color:#aa6be4;
   }
   .btnnn button:active{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 200;
    background-color:#aa6be4;
    transform: scale(0.87);
    outline: 2px solid #333;
    outline-offset: 2px;
   }
   

   svg{
    background-color: #ccc;
   }

 

   .sidebar li{
    width: 100%;
  
   }
   .sidebar a{
    width: 100%;
    font-size: 15px;
   }
 
  
   .menu{
    display: none;
   }

    input[type=text]{
    border: none;
    border-radius: 4px;
    width: 80%;
    height: 30px;
    background-color:rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    box-shadow: -10px 0 10px rgba(0,0,0,0.1);
    outline: 2px solid #ccc;
    outline-offset:2px;
    color: #fff;
    margin: 7px 5px;
    font-size: 15px;

   }
   ::placeholder{
    color:#ccc;
    font-size: 13px;
    font-weight: 100;
   }

   input:hover{
    outline: 1px solid steelblue;

   }

   input[type=submit]{
    width: 80px;
    height: 30px;
    border:none;
    border-radius: 5px;
    background-color:rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    box-shadow: -10px 0 10px rgba(0,0,0,0.1);
    color: #fff;
    outline:1px solid #fff;
    margin:0px 10px;


   }

    input[type=submit]:active{
    width: 80px;
    height: 30px;
    border:none;
    border-radius: 5px;
    background-image: linear-gradient(to right,#1e1e1e,#444);
    backdrop-filter: blur(10px);
    box-shadow: -10px 0 10px rgba(0,0,0,0.1);
    color: #fff;
    outline:1px solid #fff;
    margin: 2px 3px;
    transform: scale(0.80);

   }

   /* about css  */
.about {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 12px;
    background: linear-gradient(to right, #333, #1e1e1e);
    border-top: 1px solid #444; 
}

.bottom {
    color: #007bff;
    font-size: 20px;
    display: flex;
    margin: 20px 0;
}

.bottom h1 a {
    text-decoration: none;
    color: #fff;
    font-size: 22px;
}

.bottom > h1 a:hover {
    opacity: 0.8;
}


.inputs {
    margin: 20px;
    font-size: 28px;
    text-transform: capitalize;
    color:#007bff;
    text-align: center;
    font-size: 40px;
}

.bottom img {
    margin-right: 10px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    transition: transform 0.3s ease;
}

.bottom img:hover {
    transform: scale(1.1);
}


.inputs input[type=email] {
    width: 950px;
    height: 70px;
    border-radius: 20px;
    padding: 10px;
    border: none;
    background-color: #333;
    color: #fff;
    box-shadow: 3px 5px rgba(0,0,0,0.1);
    font-size: 15px;
}
form{
    margin: 20px 20px;
    flex-direction: column;
}
.about label{
    color:#ccc;
    font-size: 28px;
   
}
.about textarea{
    height: 90px;
    color: #fff;
    border-radius: 20px;
    padding: 10px;
    border: none;
    background-color: #333;
    color: #fff;
    font-size: 15px;

}
.about textarea:hover{
    height: 90px;
    color: #fff;
    border-radius: 20px;
    padding: 10px;
    border: none;
    background-color: #333;
    color: #fff;
    outline: 1px solid #007bff;

}
button[type=submit] {
    width: 150px;
    height:40px;
    border:none;
    border-radius: 5px;
    background-color:rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    /* box-shadow: 3px 5px #444; */
    color: #fff;
    outline:1px solid #fff;
    margin:20px 0;
    outline-offset: 2px;
    font-size: 15px;
    font-weight: 500;
}
button[type=submit]:hover{
    outline: 1px solid #007bff;
}

button[type=submit]:active{
    background: linear-gradient(to right, #0056b3, #007bff);
    /* background-color: #333; */
    transform: scale(0.89);
    outline: 1px solid #007bff;
}
.bottom a:nth-child(5){
    background-color:whitesmoke;
    height: 30px;
    width: 30px;
    border: none;
    border-radius: 6px;
}

form{
    display: flex;
    flex-direction: column;
    justify-self: center;
    align-items: center;
    text-align: center;
}
.about label{
    color:#ccc;
}
.about textarea{
    height: 150px;
    width: 950px; 
    color: #fff;
    border-radius: 20px;
    padding: 10px;
    border: none;
    background-color:#333;

    box-shadow: 3px 5px rgba(0,0,0,0.1);
    color: #fff;
}
.about textarea:hover{
    height: 150px;
    width: 950px; 
    color: #fff;
    border-radius: 20px;
    padding: 10px;
    border: none;
    background-color: #333;
    color: #fff;
}
.project  ul li{
    list-style: circle;
    font-size: 19px;
    
}



/* Responsiveness start here*/

    
@media (max-width: 768px) 
{

    html{
        scroll-behavior: smooth;
    }
    body{
        font-family: 'Poppins', sans-serif;
        /* background-color:rgba(0,0,0,0.9); */
        color:#fff;
        transition: background-color 0.5s;
        scroll-behavior: smooth;
    }
    .left{
        margin-top: 10px;
        height: 3vh;
        text-align: center; /* Center the "Vansh's Portfolio" text */
    }
    nav {
        flex-direction: column;
        height: auto;
        z-index: 1000;
        align-items: center; /* Center the navigation items */
    }
    nav ul {
        margin-top: 20px;
    }
    nav ul li {
        margin: 10px 0;
    }
    nav ul li a{
        font-size: 15px;
        margin: 20px 8px;
    }
    main {
        padding: 20px;
    }
    .firstsection {
        flex-direction: column;
        text-align: center;
        margin: 40px 0;
    }
    .firstsection .leftsection {
        width: 100%;
    }
    .firstsection .rightsection img {
        margin-top: 50px;
    }
   
    #element {
        color: #aa6be4;
        font-size: 20px;
        transition: color 0.5s;
        text-transform: capitalize;
    }
    .thirdsection{
        margin: 15px;
    }

   
    .sidebar{
        width: 100%;
        align-self: flex-end; /* Align sidebar to flex-end */
    }

    .menu{
        display: block;
    }

    .li li {
        display: none;
    }


    .menu{
    /* background-color: red; */
    margin-left: 310px;
}




#services >  ul li{
    list-style: circle;
}
#projects > h1{
    color:#74797e;
}
#projects .project h3{
    color:#545252;
    font-size: 22px;
   font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: 900;
    margin: 10px -10px; 
}
#projects .project p{
    color:#fff;
    font-weight: 400;
    margin: 10px -10px;
    font-size: 18px;
  
}
.project  ul li{
    list-style: circle;
    font-size: 15px;
    
}




.left {
    position: relative;
    color: transparent;
    
}
.btn{
    justify-content: center;
    display: flex;
    align-items: center;
}
.btn button{
   font-weight: 800;
}
.about {
    padding: 10px;
    flex-direction: column;
    display: flex;
    justify-content:flex-start;
    text-align: center;
    align-items: center;
}



.bottom{
    font-size: 24px;
    margin:20px 0;
    
}
.bottom h1 a {
    font-size: 20px;
    font-weight: 300;
    
    
 
}
.about button{
    margin: 20px 0;
}


.about textarea{
    height: 90px;
    width: 300px; 
    color: #fff;
    border-radius: 20px;
    padding: 10px;
    border: none;
    background-color: #333;
    color: #fff;
}
.about textarea:hover{
    height: 90px;
    width: 300px; 
    color: #fff;
    border-radius: 20px;
    padding: 10px;
    border: none;
    background-color: #333;
    color: #fff;
}

.inputs input[type=email]{
    width: 300px;
    height: 70px;
    border-radius: 20px;
    padding: 10px;
    border: none;
    background-color: #333;
    color: #fff;
    box-shadow: 3px 5px rgba(0,0,0,0.1);
}
.inputs input[type=email]::placeholder{
    color:#ccc;
    font-size: 13px;
    font-weight: 100;
}

.btnn button{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 700;
    justify-content: center;
    align-items: center;
    background-color:#9933ff;
    display: flex;
   }

   .btnn button:hover{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 100;
    background-color:#aa6be4;
   }
   .btnnn button:active{
    border: none;
    width: 110px;
    height: 40px;
    border-radius: 4px;
    text-align: center;
    font-size: 14px;
    font-weight: 200;
    background-color:#aa6be4;
    transform: scale(0.87);
    outline: 2px solid #333;
    outline-offset: 2px;
   }
   .btn{
    display: none;
   }
  

}


 @media(min-width:400px){

  .sidebar{
    width: 100%;
    
  }
  
  }




      </style>
    </head>
  <body>
  <header>
    <nav>
      <div class="left">Vansh's Portfolio</div>
      <div class="right">
        <ul class="sidebar">
          <li onclick="hide()"><a href="#"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/></svg></a></li>
          <li><a href="#home" onclick="hideSidebar()">Home</a></li>
          <li><a href="#about" onclick="hideSidebar()">About</a></li>
          <li><a href="#services" onclick="hideSidebar()">Services</a></li>
          <li><a href="#projects" onclick="hideSidebar()">Projects</a></li>
          <li><a href="#contact" onclick="hideSidebar()">Contact</a></li>
          <li><input type="text" name="search" id="search" placeholder="   search here"></li> 
         <li><input type="submit" value="search"></input></li>
        </ul>
  
        <ul class="li">
          <b class="menu" onclick="show()"><a href="#"><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z"/></svg></a>
          </b>
          <li><a href="#home" onclick="hideSidebar()">Home</a></li>
          <li><a href="#about" onclick="hideSidebar()">About</a></li>
          <li><a href="#services" onclick="hideSidebar()">Services</a></li>
          <li><a href="#projects" onclick="hideSidebar()">Projects</a></li>
          <li><a href="#contact" onclick="hideSidebar()">Contact</a></li>
          
        </ul>
      </div>
    </nav>
  </header>
 
  <main>

    <!-- Section 1: Home -->
    <section id="home" class="firstsection">
      <div class="leftsection">
        <p>Hi, My name is <span class="purple">Vansh Dhalor</span></p>
        <p>I am a <span id="element"></span></p>
        
        <div class="btn">
          <button>Resume </button>
        
        </div>
      </div>
      
      <div class="rightsection">
        <img src="images/logo1-removebg-preview.png" alt="logo">

        <div class="btnn">
          <button>Resume </button>
        
        </div>

      </div>
    </section>
    <hr>
    <!-- Section 2: About -->
    <section id="about" class="secondsection">
      <span class="text-gray"></span> 
      <h1>About <svg xmlns="http://www.w3.org/2000/svg" height="34" viewBox="0 -960 960 960" width="34"><path d="M480-484.065q-69.587 0-118.859-49.272-49.272-49.272-49.272-118.859 0-69.587 49.272-118.739T480-820.087q69.587 0 118.859 49.152 49.272 49.152 49.272 118.739t-49.272 118.859Q549.587-484.065 480-484.065ZM151.869-147.804v-120.609q0-36.224 18.743-66.589 18.742-30.365 49.801-46.346 62.717-31.239 127.664-46.978T480-444.065q67.435 0 132.391 15.619 64.957 15.62 127.196 46.859 31.059 15.947 49.801 46.245 18.743 30.299 18.743 66.916v120.622H151.869Zm91.001-91h474.26v-28.413q0-10.768-5.5-19.578-5.5-8.81-14.5-13.705-52.565-26.043-106.847-39.304Q536-353.065 480-353.065q-55.522 0-110.283 13.261-54.76 13.261-106.847 39.304-9 4.895-14.5 13.705t-5.5 19.578v28.413Zm237.122-336.262q31.812 0 54.475-22.654 22.663-22.655 22.663-54.467 0-31.813-22.654-54.357-22.655-22.543-54.468-22.543-31.812 0-54.475 22.587-22.663 22.586-22.663 54.304 0 31.816 22.654 54.473 22.655 22.657 54.468 22.657Zm.008-77.13Zm0 413.392Z" /></svg> </h1>
      <p>I am currently in my BCA 2nd year and have experience in HTML, CSS, JavaScript, PHP, and SQL.</p>
    </section>
    <hr>
    <!-- Section 3: Services -->
    <section id="services" class="thirdsection">
      <span class="text-gray">My Services</span>
      <h1>Services Offered
        <svg xmlns="http://www.w3.org/2000/svg" height="34" viewBox="0 -960 960 960" width="34"><path d="M316.413-232.348 68.521-480l247.892-247.891 64.891 64.652-184 184 183 183-63.891 63.891Zm327.174.239-64.891-64.652 184-184-183-183 63.891-63.891L891.479-480 643.587-232.109Z"/></svg>
      </h1>
      <ul>
        <li>Web Development</li>
        <li>Frontend Design</li>
        <li>Database Management (sql)</li>
        <li>WebDesigner(html,css,Figma)</li>
      </ul>
    </section>  
    <hr>
    <!-- Section 4: Projects -->
    <section id="projects" class="fourthsection">
        <span class="text-gray">My Projects</span>
        <h1>Recent Projects</h1>


        <div class="project">
          <h3>Simple Portfolio <img src="images/5072860.png" alt="" height="60px"></h3>
          
          <p>About me and My skills and experience what i Learned till now</p>
      </div>
        
        <div class="project">
            <h3>Headphone & SmartWatch Website <img src="images/logoindex.png" alt="" height="50px"></h3>
            <p>A website showcasing different types of headphones with details and prices.</p>
        </div>

        <div class="project">
          <h3>Netflix Clone <img src="images/faviconn.ico" alt="" height="30px"></h3>
          <p>A Netflix Clone by (html,css).</p>
      </div>
        
    
        <div class="project">
            <h3>Coding Site</h3>
            <img src="images/Screenshot 2024-03-02 150115 (1).jpg" alt="" height="70px">

           
            <p>A platform where users can get different type of codes in <b>(C/C++/HTML,CSS,JS/PHP/SQL).</b></p>
        </div>
    
        <div class="project">
            <h3>Astrology Website</h3>
            <img src="images/images-removebg-preview.png" height="70px">
            <p>An astrology website providing your lagna chart and your birth chart reading.</p>
        </div>

        <div class="project">
          <h3>Small Html,Css Projects <img src="images/html.png" alt="" height="40px"> <img src="images/css-3 (1).png" alt="" height="40px"></h3>
        
            <ul>
              <li>digital clock</li>
              <li>get user location</li>
              <li>side nav</li>
              <li>reponsive nav</li>
              <li>check user-status</li>
              <li>button animation's</li>
              <li>age calculator</li>
              <li>login form</li>
              <li>webcam access</li>
              <li>text to speech and speech to text</li>
            </ul>
        

         
      </div>

      <div class="project">
        <h3>Sql Question's</h3><img src="images/sql-server.png" alt="" height="70px">
        <p>Solved 20+ sql Question on real life based problem.</p>  
      </div>

    </section>
    <hr>
    <!-- Section 5: Contact -->
    <section id="contact" class="fifthsection">
      <span class="text-gray">Contact Me</span>
      <h1>Contact Information</h1>
      <p>You can reach me at 9xxxxx
        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"><path d="M798-120q-125 0-247-54.5T329-329Q229-429 174.5-551T120-798q0-18 12-30t30-12h162q14 0 25 9.5t13 22.5l26 140q2 16-1 27t-11 19l-97 98q20 37 47.5 71.5T387-386q31 31 65 57.5t72 48.5l94-94q9-9 23.5-13.5T670-390l138 28q14 4 23 14.5t9 23.5v162q0 18-12 30t-30 12ZM241-600l66-66-17-94h-89q5 41 14 81t26 79Zm358 358q39 17 79.5 27t81.5 13v-88l-94-19-67 67ZM241-600Zm358 358Z"/></svg>
      </p>
      
    <ul class="bottom">
      <h1><a href="https://www.instagram.com/_vansh_.19/?igsh==" target="_blank"></a></h1>

      <a href=""><img src="/images/faviconinsta.png" alt="" height="30px"></a>

      <a href="#"><img src="images/faviconwha.png" alt="" height="30px"></a>

      
      <a href="#"><img src="images/favicon (1).ico" alt="" height="30px"></a>


      <a href="https://github.com/vansh-frontend"><img src="images/favicon.ico" alt="" height="30px"></a>

   </ul>
    </section>
    
  </main>
  <div class="about">
     <div class="inputs" id="about">FeedBack
  

       
  <form action="https://api.web3forms.com/submit" method="POST">
  
    <input type="hidden" name="access_key" value="6aa99d94-6385-47ea-af98-84a0e261f23d">
            <label for="text">suggestion</label>
          <textarea name="Any suggestion" id="" cols="30" rows="10" placeholder=" Any FeedBack or suggestion..."></textarea>
         
          <label for="email">Email</label>
          <input type="email" id="email" placeholder="your email address">

          <button type="submit" value="send" onclick="send()">Send</button>
         
        </form>
    </div>

    
    </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
