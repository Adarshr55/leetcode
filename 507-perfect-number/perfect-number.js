/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function(num) {
 if(num<0)return false
let sum=0
for(i=1;i<num;i++){
    if(num%i==0){
        sum+=i
    }
}
    if(num===sum){
        return true
    }else
    return false
    
};