stockAppModule.directive('ngEnter', function(){
	return function(scope, element, attrs) {
		element.on('keydown keypress', function(event){
			event.preventDefault();
			if(event.which === 13) {
				
			}
		});
	};
});