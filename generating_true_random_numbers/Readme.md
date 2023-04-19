1 - If we are going to allow input from a user to choose a range for generating our number, we will need to figure out how many bits are required to represent a given base 10 integer so we know how many random bits to generate. The equation we need to do this is 

$$
b_{spec} = |\log_{2}(n)| + 1
$$

This function returns the number of bits required to represent a given base 10
