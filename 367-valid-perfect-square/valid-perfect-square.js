/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    if(num<0)return false
    for(i=1;i*i<=num;i++){
        if(i*i===num){
            return true
        }
    }
    return false
   

    
};