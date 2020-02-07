import React from 'react'

const baseUrl = "http://0.0.0.0:8000/compile_django/"

class BaseTemplate extends React.Component {
    constructor() {
    super()
      this.state = {
        data: null,
      };
    }
  
    componentDidMount() {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", baseUrl, true);
        xhr.setRequestHeader('Content-type', 'application/json')
        xhr.onload = () => {
            var template = xhr.response;
            console.log(template);
            this.setState({ template });
        }

        xhr.send(JSON.stringify( this.props ));
    }
  
    render() {
      if (this.state.template) {
        return  <div dangerouslySetInnerHTML={{__html:this.state.template}} />;
      }
      else {
        return <div>Loading...</div>
      }
    }
  }

  export default BaseTemplate;