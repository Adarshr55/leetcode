/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let s=0,p=1,arr=[]
    let num=n.toString()
    for(d of num){
        arr.push(Number(d))
    }
    for(e of arr){
        s+=e
        p*=e
    }
    return p-s
};