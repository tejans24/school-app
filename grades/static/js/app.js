/*var stockAppModule = angular.module('ngStock', []);

stockAppModule.config(function($locationProvider, $routeProvider) {
  	$routeProvider.
    when('/', {
        templateUrl: 'static/partials/tableView.html',
        controller: 'TableViewController'
    }).otherwise({redirectTo: '/'});
});*/


var PARTIALS_URL = 'static/partials/';

/*
* calcRatesApp
*
* 
*/
var calcRatesApp = angular.module('calcRatesApp', []);

calcRatesApp.config(function($routeProvider){
	$routeProvider.when('/',{
		templateUrl: 'static/partials/home.html',
		controller: 'HomeController'
	});

	$routeProvider.when('/homeloan_calculator',{
		templateUrl: PARTIALS_URL + 'home-loan.html',
		controller: 'HomeLoanController'
	});
});