// Last updated: 11/26/2025, 8:55:15 PM
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(arg) {
            if (val === arg) {
                return true
            } else {
                throw new Error('Not Equal')
            }
        },
        notToBe: function(arg) {
            if (val !== arg) {
                return true
            } else {
                throw new Error("Equal");
            }
        }
    };
};


/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */