
function submitfun(){


                
                var request = new XMLHttpRequest();
                var url = "http://127.0.0.1:8000/testsess/create/";
                request.open("GET", url, true);
                request.setRequestHeader("Content-Type", "application/json");

                // request.setRequestHeader('X-CSRF-Token', getCookie('csrftoken'));

                request.onreadystatechange = function () {
                    if (request.readyState === 4 && request.status === 200) {
                        var jsonData = JSON.parse(request.response);
                        console.log(jsonData);
                        if (jsonData != 'Invalid Credentials') {
                  

                    window.location.href="home.html";
                    
                    
                }
                else {
                    
                    alert(jsonData);
                }
                    }
                };
                var username =  document.getElementById("username").value;
                var password = document.getElementById("password").value;
                

                var data = JSON.stringify({"email": username, "password": password});
                console.log(data);

                request.send(data);

            };  


