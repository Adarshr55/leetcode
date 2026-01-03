/**
 * @param {number} n
 * @return {number}
 */
var numOfWays = function(n) {
    let mod=1000000007
    let a=6,b=6
    for(i=2;i<=n;i++){
        let newA=(2*a+2*b)%mod
        let newB=(2*a+3*b)%mod
        a=newA
        b=newB
    }
    return (a+b)%mod
};