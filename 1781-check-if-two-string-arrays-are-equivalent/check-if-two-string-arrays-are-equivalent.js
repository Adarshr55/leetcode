/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    let s1=""
    let s2=""
    for( str of word1){
        s1+=str
    }
    for(str of word2){
        s2+=str
    }
    return s1===s2
};