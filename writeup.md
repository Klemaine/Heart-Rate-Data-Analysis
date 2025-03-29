## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[The reason there may be missing values or values that state "NO DATA" could be a result of the heart rate monitor not functioning properly and therefore not outputting any data. For example, during sleep, there may be a point during the night that the subject may move into a postion that causes the heart rate monitor to be unable to read any data. By filtering out the missing values or "NO DATA" we may not be made aware that there is in fact an issue with the heart rate monitor and will therefore not try to find a solution to ensure that the monitor is working at 100% capacity given any circumstance.]

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

[Based on my findings, it appears to me that sleep occured during Phase 3. The average heart rate BPM is the lowest during this phase.]

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

[Bsed on the data that I've collected, exercise occurs during Phase Phase 1. I can determine this because the average and maximum heart rate BPM during Phase 2 are among the highest out of all the phases.]

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

[We notice that during Phase 2 the heart rate BPM is lower than Phase 1 but the standard deviation is higher. I believe that the standard deviation is higher becuase throughout normal awake activity, the heart rate BPM will vary more based on different level of activity during normal everyday tasks.]
