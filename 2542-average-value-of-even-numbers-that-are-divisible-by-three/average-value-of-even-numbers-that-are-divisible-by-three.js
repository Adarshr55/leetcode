/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    let max=0
    let count=0
    for(key of nums){
        if(key%3==0 &&key%2==0){
            max+=key
            count++
        }

    }
    if (count!==0){
       max=max/count
    }else{
        return 0
    }

    return Math.floor(max)

    
}