import React from 'react';  
import './App.css';

class App extends React.Component{

  constructor(props){
    super(props);
      this.state={
        todoList:[],
        activeItem:{
          id:null,
          title:'',
          completed:false,
        },
        editing:false,
      };
      this.fetchTasks = this.fetchTasks.bind(this)
  };

  componentWillMount(){
    this.fetchTasks()
  }
  
  fetchTasks(){
    console.log('Fetching...')
    fetch('http://127.0.0.1:8000/api/task-list/')
    .then(response => response.json())
    .then(data=>
      this.setState({
        todoList:data
      })
      ) 
  }

  render(){
    var tasks = this.state.todoList
    return(
      <div className = "container">

        <div id="task-container">
          <div id="form-wrapper">
            <div id="form">
              <div className='flex-wrapper'>
                <div style={{flex:6}}>
                  <input className='form-control' id='title' type="text" name="title" placeholder='Add Task title here..'></input>
                </div>
                <div style={{flex:1}}>
                  <input id="submit" className='bt btn-warning' type="submit" name='Add'></input>

                </div>
              </div>
            </div>
          </div>

          <div id="list-wrapper">
            {tasks.map(function(task,index){
              return(
                <div key={index} className='task-wrapper flex-wrapper'>
                  <span>{task.title}</span>
                </div>
              )
            })}
          </div>

        </div>
        
      </div>
    )
  }
}

export default App;
