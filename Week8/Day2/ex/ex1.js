// #1 - 'a' will be 3.
// #1.1 - Error due to reassignment of a const variable.

// #2 - 'a' will be 5 in both calls to funcThree.
// #2.2 - Error due to reassignment of a const variable.

// #3 - 'a' will be "hello" in funcFive.
// #4 - 'a' will be "test" in funcSix.
// #4.2 - No error, but global 'a' remains 1.

// #5 - 'a' will be 5 inside the if block and 2 outside.
// #5.2 - No error, but global 'a' remains 2.