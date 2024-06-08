'''
This script runs a simulation for US Jury duty. 
It compares the total number of a 14 man jury to the total number of juries an individual could be on given different candidate pool sizes.
The simulation leverages enumeration techniques to count the total combinations of people that compose a single jury.
The lower bound of the simulation is assumed to be one more than the size of the jury.
'''
import math as mth
import matplotlib.pyplot as plt

class simulation:

    def __init__(self, candidate_pool_size, jury_size):
        self.candidate_pool_size = candidate_pool_size
        self.jury_size = jury_size

    def proportion_function(self, candidate_pool_size, jury_size):
        total_juries = mth.comb(candidate_pool_size, jury_size)
        total_juries_incl_you = mth.comb(candidate_pool_size - 1, jury_size - 1)
        return total_juries_incl_you / total_juries
    
    def get_tuples(self):
        outcome_list = []
        for i in range(self.candidate_pool_size, self.jury_size, -1):
            output_tuple = tuple([i, self.proportion_function(i, self.jury_size)])
            outcome_list.append(output_tuple)
        return outcome_list
    

if __name__  == "__main__":
    
    #set simulation parameters
    candidate_pool_size = 200
    jury_size = 14
    
    simulation_results = simulation(candidate_pool_size, jury_size).get_tuples()

    x, y = zip(*simulation_results)

    plt.plot(x,y)

    plt.title("Proportion of Jury Selection to Total Juries")
    plt.xlabel("Number of Candidates")
    plt.ylabel("Proportion of Selected Juries (%)")

    plt.grid(True)

    plt.savefig('output.png')