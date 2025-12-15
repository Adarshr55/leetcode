/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function(n, m) {
    let sumn=0
    let summ=0
    for(i=0;i<=n;i++){
        if(i %m !==0){
          sumn+=i
        }else {
            summ+=i
        }
            
        }
       return sumn-summ
    }
