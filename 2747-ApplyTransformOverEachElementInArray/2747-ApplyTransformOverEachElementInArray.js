// Last updated: 11/26/2025, 8:55:19 PM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let result  = []
    for(let i = 0; i < arr.length; i++){
        result.push(fn(arr[i], i))
    }
    return result
};