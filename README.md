# US Jury Duty Simulation

## Summary
  I had to attend jury duty today and I found myself in a screening room with one hundred and sixty other candidates when my local government official described only fourteen candidates can be selected and some may be dismissed if they have valid legal examption. So, I was curious if it was possible to measure how my odds of being selected as a juror would change as the pool became smaller since there seemed to be an obvious relationship between the pool size and the likelihood of being selected. Unfortunately, I learned in the US juries are selected on a per case basis, and the event only happens once, so I learned it's not really possible to estimate the direct probabilities of being chosen myself for a jury.

  However, I had an idea for a proxy measurement. It should be possible to enumerate the total number of juries an individual can be selected for and take the proportion against the total number of possible jury combinations.

$$
\text{Proportion of Possible Juries} = \frac{\text{Juries Selected to Attend}}{\text{Total Number of Possible Juries}}
$$

  This measures that, out of all possible juries, the proportion of possible jury combinations where I am selected. What I've found was that as the candidate pool becomes smaller that the proportion of possible juries to be selected for grows larger. This seems to reconcile my intuition and provide an anchor for the magnitude of how likely selection becomes as the candidate pool becomes smaller.

## Outcome
[!alt_text](https://github.com/amason445/jury_duty_problem/blob/main/output.png)
