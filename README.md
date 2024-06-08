# US Jury Duty Simulation

I had to attend jury duty today and I found myself in a screening room with one hundred and sixty other candidates when my local government official described only fourteen candidates can be selected and some may be dismissed if they have valid legal examption. So, I was curious if it was possible to measure how my odds of being selected as a juror would change as the pool became smaller since there seemed to be an obvious relationship between the pool size and the likelihood of being selected. Unfortunately, I learned in the US juries are selected on a per case basis so I learned it's not really possible to estimate the direct probabilities of being chosen myself.

However, I had an idea for a proxy. It should be possible to enumerate the total number of juries an individual can be selected for and take the proportion against the total number of possible jury combinations.

$$
\text{Proportion of Possible Juries} = \frac{\text{Juries Selected to Attend}}{\text{Total Number of Possible Juries}}
$$
 
