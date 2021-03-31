function setAction(form) {
	//calling test api
  /*
      var entry={
       x_value:x,
       y_value:y,
       z_value:z
      };
      fetch(`http://192.168.10.102:5000/test`,{
        method:"POST",
        credentials: "include",
        body:JSON.stringify(entry),
        cache:"no-cache",
        headers: new Headers({
          "content-type": "application/json"
        })
      })
      .then(function(response){
        if(response.status!==200){
          console.log(`Looks like there was a problem. Status code: ${response.status}`);
          return ;
        }
        response.json().then(function (data){
          console.log(data);
        });
        })
        .catch(function(error){
          console.log("Fetch error: "+error);
        });
      }
      */
        
        
    form.action = "http://10.11.57.125:5000/test";
    return true;
    
    
    }
	
    function validateForm(form) {
	if(document.form.x_value.value===""){
	    alert("Please enter x value");
            return false;	
	}
	 else if(document.form.y_value.value===""){
	    alert("Please enter y value");
            return false;
	 }
		//validating user inputs
		var choose=document.getElementById("drop");
		choose=choose.options[choose.selectedIndex].value;
        var x = parseFloat(document.form.x_value.value);
        var y = parseFloat(document.form.y_value.value);
        var z = parseInt(choose);
        if(x<0  || x>20){
          alert("Enter x valuein between 0mm-20mm");
          return false;
        }
        if(y<0 || y>15){
          alert("Enter y valuein between 0mm-15mm");
          return false;
        }
        if(z==4 || z==10 || z==40 || z==100 ){
	//calling setAction function
          
          setAction(form);
        }
        else{
          alert("Please select an option");
        return false;
        }
      }
      
