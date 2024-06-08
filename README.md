# US Jury Duty Simulation

## Summary
  I had to attend jury duty today and I found myself in a screening room with one hundred and sixty other candidates. My local government official described that only fourteen candidates can be selected for any jury and some may be dismissed prior to selection only if they have a valid legal examption. So, I was curious if it was possible to measure how my odds of being selected as a juror would change as the candidate pool became smaller. Since there seemed to be an obvious relationship between the pool size and the likelihood of being selected, I was interested in taking a probability. Unfortunately, I learned in the US juries are selected on a per case basis, and since this event only happens once, I realized it's not possible to estimate the direct probability of being chosen for a jury in a meaningful way.

  However, I had an idea for a proxy measurement. It's possible to enumerate the total number of juries an individual can be selected for and take the proportion of this against the total number of possible jury combinations.

$$
\text{Proportion of Possible Juries} = \frac{\text{Juries Selected to Attend}}{\text{Total Number of Possible Juries}}
$$

  This measures, out of all of the possible juries, the proportion of possible jury combinations where I can selected. What I've found was that as the jury candidate pool becomes smaller that the proportion of possible juries to be selected for grows larger. This reconciles my intuition and provide an anchor for the magnitude of how likely selection becomes as the candidate pool becomes smaller but falls short in assuming selection between candidates is equally likely.

## Outcome
![alt_text](https://github.com/amason445/jury_duty_problem/blob/main/output.png)

## References
- [Combinatorics - Joy Morris](https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Combinatorics_(Morris))
- [Discrete Uniform Distribution](https://en.wikipedia.org/wiki/Discrete_uniform_distribution)
