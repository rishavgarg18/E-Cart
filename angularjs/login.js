var app= angular.module("LoginView",[])
                    .controller("LoginController",function($scope,$http){
                    $scope.error="";    
                                    $scope.submit=function(){
                                        let email = $scope.email;
                                        let Password = $scope.password;
                                        // let url =  window.backend__url+"patient_login/login/"
                                        $http({
                                                method: 'POST',
                                                url: 'http://127.0.0.1:8000/login/',
                                                data: {
                                                        'email': email,
                                                        'password': Password,
                                     
                                                        }

                                                    })
                                      .then(function(response) {
                                        $scope.myWelcome = response.data;
                                        if (response.data=="OK"){
                                                    console.log("CHAL RH HA");
                                                    window.location.href="dashboard.html";
                                                    sessionStorage.setItem("email", email);

                                                }
                                        })}})
                      .controller("SignUpController",function($scope,$http){
                                            $scope.error="";    
                                            $scope.submit=function(){
                                                let email = $scope.email;
                                                let Password = $scope.password;
                                                // let url =  window.backend__url+"patient_login/login/"
                                                $http({
                                                        method: 'POST',
                                                        url: 'http://127.0.0.1:8000/login/new/',
                                                        data: {
                                                                'email': email,
                                                                'password': Password,
                                             
                                                                }

                                                            })
                                              .then(function(response) {
                                                $scope.myWelcome = response.data;

                                                }

                                            )}


                                          })