/*
 * Controller class for stock table view
 */
stockAppModule.controller('TableViewController', function TableViewController($timeout, $rootScope, $scope, $http, stock){
	var scope = $scope;

	scope.stocks = [];
	//scope.sort = {column: "URL", descending: false};

	scope.tableHeaderOptions = [
			{name: "Symbol", value : "symbol"},
			{name: "Last Trade Price", value : "last_trade_price"},
			{name: "Change %", value: "change_in_percent"},
			{name: "Change", value: "change"},
			{name: "Daily Volume", value: "daily_volume"},
			{name: "Bid", value: "bid"},
			{name: "Ask", value: "ask"},
	];
	
	scope.sortTable = function(column) {
		var sort = scope.sort;
		if(column == sort.column) {
			sort.descending = !sort.descending;
		} else {
			sort.column = column;
			sort.descending = false;
		}
	};
	
	scope.addStock = function() {
		scope.stocks = stock.getStockData(scope.symbol);
		scope.symbol = "";
	};
    
    $timeout(function somework(){
        $timeout(somework, 1000);
    }, 1000);

    function updateStocks() {
        for(stock in scope.stocks) {
        	
        }
    }


    scope.editLoan = function(index) {
		console.log(index);
		console.log(scope.loans[index]);
	};
	
	
});