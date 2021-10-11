var app = angular.module('BudgApp', []);
app.controller('BudgControl', function($scope) {
  $scope.total=0;
  $scope.myTransactions=[];
  $scope.addTransaction = function(){
    if($scope.trRad){
      if($scope.trRad=="deb"){
        $scope.myTransactions.push({"date":$scope.trDate,"desc":$scope.trDescription,"deb":$scope.trAmount, "cred":0});
        $scope.total=$scope.total+$scope.trAmount;
      }else if($scope.trRad=="cred"){
        $scope.myTransactions.push({"date":$scope.trDate,"desc":$scope.trDescription,"deb":0,"cred":$scope.trAmount});
        $scope.total=$scope.total-$scope.trAmount;
      }
    }
  };
  $scope.changeTrType = function(index){
    var trEdit = $scope.myTransactions[index];
    if(trEdit["deb"]==0){
      $scope.total=$scope.total+2*trEdit["cred"];
      trEdit["deb"]=trEdit["cred"];
      trEdit["cred"]=0;
    }else{
      $scope.total=$scope.total-2*trEdit["deb"];
      trEdit["cred"]=trEdit["deb"];
      trEdit["deb"]=0;
    }
    // for(var i=0;i<$scope.myTransactions.length;i++){
    // 	alert(index+"\n"+$scope.myTransactions[i]["date"]+"\n"+$scope.myTransactions[i]["desc"]);
    // }
  };
  $scope.deleteItem = function(index){
    if($scope.myTransactions[index]["deb"]==0){
      $scope.total=$scope.total+$scope.myTransactions[index]["cred"]
      $scope.myTransactions[index]["cred"]=0;
    }else{
      $scope.total=$scope.total-$scope.myTransactions[index]["deb"]
      $scope.myTransactions[index]["deb"]=0
    }
    $scope.myTransactions.splice(index,1);
  };
  app.filter("noPrintZero", function(){
    return function(number){
      alert(number);
      if(number==0||number=="0"){
        return "";
      }else{
        return number;
      }
    }
  });
});
