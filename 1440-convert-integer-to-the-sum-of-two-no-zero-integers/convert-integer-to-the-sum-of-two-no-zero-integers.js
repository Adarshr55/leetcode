/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function(n) {
    let arr=[]
     let a=1
     let b=n-1
     while(a.toString().split("").includes("0")||b.toString().split("").includes("0")){
        a++
        b--
     }
     arr.push(a,b)
     return arr
}