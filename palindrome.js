/*Given the string, check if it is a palindrome. I simply split the string in an array of chars, I reverse the array and join the chars again to build a string. If the first string and the reversed one are equals then it is a palindrome one.
* @author  Francesco Fresta
 * @version 1.0, 15th April 2018
*/

function checkPalindrome(inputString) {
    return (inputString == inputString.split('').reverse().join(''));
}