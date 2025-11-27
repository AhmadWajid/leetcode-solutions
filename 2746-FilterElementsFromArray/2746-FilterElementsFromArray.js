// Last updated: 11/26/2025, 8:55:20 PM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let result = []
    for(i=0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
             result.push(arr[i])
        }
    }
            return result
};