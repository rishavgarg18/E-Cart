var app= angular.module("LoginView",[''])
                    .controller("studentLoginController",function($scope,$http){
                    $scope.error="";    
                    $scope.submit=function(){
                        let email = $scope.email;
                        let Password = $scope.password;
                        // let url =  window.backend__url+"patient_login/login/"
                        $http.get("https://706c7cea8a9d.ngrok.io/testsess/create/")
  .then(function(response) {
    $scope.myWelcome = response.data;})}})