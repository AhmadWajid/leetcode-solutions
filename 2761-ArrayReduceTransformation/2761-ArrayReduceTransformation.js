// Last updated: 11/26/2025, 8:55:19 PM
/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var first = init
    for(i=0; i< nums.length; i++) {
        first = fn(first, nums[i])
    }
    return first
    
};