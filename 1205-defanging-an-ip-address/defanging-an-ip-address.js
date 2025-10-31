/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address){
    let str=""
    for(ltr of address){
        if(ltr=="."){
            ltr="[.]"
        }
            str+=ltr
        

    }
    return str
}
