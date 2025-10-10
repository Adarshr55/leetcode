/**
 * @param {number} celsius
 * @return {number[]}
 */
var convertTemperature = function(celsius) {
    let x=celsius
   let arr=[]
   let kelvin =x+273.15
   let fah=x*1.80 +32.00
   arr.push(kelvin,fah)
   return arr
};