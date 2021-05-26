#Introduction

A colony of Aucks (super-intelligent alien bioengineers) has landed on Earth and has created
new species of farm animals! The Aucks are performing their experiments on Earth, and plan on
transporting the mutant animals back to their home planet of Aurock.
In this problem set, youwill implement algorithms to figure out how the aliens should shuttle 
their experimental animals back across space.

The aliens have succeeded in breeding cows that jump over the moon! Now they want to take home 
their mutant cows. The aliens want to take all chosen cows back, but their spaceship has a weight 
limit  and they want to minimize the number of trips they have to take across the universe. Somehow,
the  aliens have developed breeding technology to make cows with only integer weights. The data for 
the  cows to be transported is stored in ps1_cow_data.txt.

1. Greedy Cow Transport

One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. 
This is an example of a greedy algorithm. So if there’s only 2 tons of free space on your spaceship,
with one cow that’s 3 tons and another that’s 1 ton, the 1 ton cow will still get put onto the spaceship.

2. Brute Force Cow Transport

Another way to transport the cows is to look at every possible combination of trips and pick the best one. 
This is an example of a brute force algorithm.

3. Comparing the Cow Transport Algorithms

Compare both alorigthms. Compare the results as well as computation time.
