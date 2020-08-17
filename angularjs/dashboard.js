var app= angular.module("DashboardView",[])
                    .controller("ProductController",function($scope,$http){
                    	$scope.email=sessionStorage.getItem("email");
                    	 // $scope.allstudent=function()
                      //    {
                            $http.get('http://127.0.0.1:8000/products/all/')                 			

			
            			         .then(
      					                function (response){
        				                $scope.products = response.data;
        				                console.log($scope.products);
        				                                   }
            			              )
	                     $scope.getproduct=function(productid)
	                                                        {
	                                                        sessionStorage.setItem('productid',productid);
	                                                        window.location.href="order.html";
	                                                        }
                    })
                    .controller("OrderController",function($scope,$http){
                    	productid=sessionStorage.getItem("productid");
                    	$scope.email=sessionStorage.getItem("email");
                    	// getproductinfo
                                                
                                                $http({
                                                        method: 'POST',
                                                        url: 'http://127.0.0.1:8000/products/all/viewproduct/',
                                                        data: {
                                                                'productid':productid
                                             
                                                                }

                                                            })
                                              .then(function(response) {
                                                $scope.productinfo = response.data;
                                                console.log($scope.productinfo);

                                                }

                                            )

                          $scope.submitphoneno=function()
					                        {let phone_no=$scope.phoneno;
					                        	$http({
					                                                method: 'POST',
					                                                url:'http://127.0.0.1:8000/phoneverification/sendsms/',
					                                                data: {
					                                                      'phone_no': phone_no,
					                                                     
					                                           
					                                                    }

					                              })
					                        .then(function(response) {
					                           
					                            $scope.messagesendotp = response.data;
					                        },function(response)
					                        {
					                        	$scope.message = 'Failed server error';

					                        });
					                      }
						  $scope.submitotp=function()
						                        {let otp=$scope.otp;
						                          let phone_no=$scope.phoneno;
						                          $http({
						                                                method: 'POST',
						                                                url:'http://127.0.0.1:8000/phoneverification/verifysms/',
						                                                data: {
						                                                      'phone_no': phone_no,
						                                                      'otp': otp
						                                           
						                                                    }

						                              })
						                        .then(function(response) {
						                           
						                            $scope.messageotp = response.data;
						                        },function(response)
						                        {
						                          $scope.messageotp = 'Invalid Server error';

						                        });
						                      }


							  $scope.submitifsc=function()
							  {let ifsc=$scope.ifsc;
							  	$http.get("https://ifsc.razorpay.com/"+ifsc,false)
							  .then(function(response) {
							     
							      $scope.messageifsc = 'Verified';
							  },function(response)
							  {
							  	$scope.messageifsc = 'Invalid';

							  });
							}
			                    
			                      		





                                          })
                    	


                   