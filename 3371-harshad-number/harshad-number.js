/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function(x) {
    let sum=0
    let str=x.toString()
    for(s of str){
        sum+=Number(s)
    }
    if(x%sum==0){
        return sum
    }else{
        return -1
    }

    }
