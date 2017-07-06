var userServices = angular.module('userServices', ['ngResource']);

userServices.factory('UserLocatiuonService', [$resource, function($resource){
    return $resource('api\\/', {
        query: {method:'GET', params:{}, isArray:true}
    });

}]);