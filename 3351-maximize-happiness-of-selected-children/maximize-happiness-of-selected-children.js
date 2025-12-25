/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function(happiness, k) {
    let happy=happiness.sort((a,b)=>b-a)
    let sum=0
    for(i=0;i<k;i++){
        sum+=Math.max(happiness[i]-i,0)
    }
    return sum
};