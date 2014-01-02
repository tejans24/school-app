stockAppModule.factory('stock', function stock($http, $rootScope) {
    var prefix = 'http://query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.quotes where symbol="';
    var suffix = '"&env=http://datatables.org/alltables.env&format=json&callback=JSON_CALLBACK';
    var query = "";
    var stocks = [];

    var get = function (symbol) {
        query = prefix + symbol + suffix;

        $http.jsonp(query).success(function (data) {
            stocks.push(data.query.results.quote);
        });

        return stocks;
    };

    var getUpdatedInfo = function (symbol) {
        query = prefix + symbol + suffix;
    }

    return {
        getStockData: get
    };
});