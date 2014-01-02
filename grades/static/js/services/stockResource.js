/**
 * Created with IntelliJ IDEA.
 * User: yinchengjie2
 * Date: 9/8/13
 * Time: 10:47 AM
 * To change this template use File | Settings | File Templates.
 */
stockAppModule.factory('stockResource', [$resource, function stockResource ($resource){
    var baseUrl = "http://query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.quotes where symbol=:symbol"
    var suffix = "&env=http://datatables.org/alltables.env&format=json";

    return $resource(baseUrl + ":suffix",
        {symbol: @symbol, suffix: suffix},
        {search : {method : 'GET', isArray:false}});                                                                                                                      return $resource()
}]);