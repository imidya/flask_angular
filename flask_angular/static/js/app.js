'use strict';

var FlaskAngular = angular.module('FlaskAngular', []);

FlaskAngular.config(['$routeProvider', '$locationProvider',
	function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/partial.html',
			controller: PartialController
		})

		$locationProvider.html5Mode(true);
	}]);