//definimos los paquetes o modulo a utilizar en angular
var app=angular.module("app",["ngResource"]);
//definimos el controlador
app.controller("controlador",function($scope,datos_alumno,datos_materia){
	$scope.mensaje="";
	$scope.lista_alumno=datos_alumno.get();
	$scope.lista_materia=datos_materia.get();
	$scope.BuscarAlumno=function(){
		var ced=$scope.cedula;
		for (var i = 0; i < $scope.lista_alumno.length; i++) {
			if(angular.equals(ced, $scope.lista_alumno[i].cedula)){
				window.location.href="matricularse.html";
			}
			else{
				$scope.mensaje="NO Existe el alumno";
			}
		}
	}
});
//definir el factory que retorne datos de un webservice
app.factory('datos_alumno',['$resource',function($resource){
	return $resource('http://127.0.0.1:8000/api/alumno/', {}, {get:{method:'GET',params:{},isArray:true}});
}])

app.factory('datos_materia',['$resource',function($resource){
	return $resource('http://127.0.0.1:8000/api/materia/', {}, {get:{method:'GET',params:{},isArray:true}});
}])