# CWHAP-analysis

# Survey Instruments

## Pre-test Measures

### Personality (courtesy of Dr. Olivia Newton)

The Ten Item Personality Inventory (TIPI) developed by Gosling and colleagues (2003) was used in the study. The TIPI is used to measure the Big Five personality dimensions: Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Openness to Experiences.

*Scoring*

Responses are provided on a 7-point Likert-type scale ranging from strongly disagree to strongly agree. A subset of the items need to be reverse scored: 2, 4, 6, 8, and 10. Mean ratings of the two items for each personality scale are used to calculate scores (see table below).

Recode as follows:
* 7 = 1
* 6 = 2
* 5 = 3
* 4 = 4
* 3 = 5
* 2 = 6
* 1 = 7


| Label  | Item  | Scale |
| :------------- | :------------- | :------------- |
| TIPI_1 | Extraverted, enthusiastic | Extraversion |
| TIPI_2* | Critical, quarrelsome | Agreeableness |
| TIPI_3 | Dependable, self-disciplined | Conscientiousness |
| TIPI_4* | Anxious, easily upset | Emotional Stability |
| TIPI_5 | Open to new experiences, complex | Openness to Experiences |
| TIPI_6* | Reserved, quiet | Extraversion |
| TIPI_7 | Sympathetic, warm | Agreeableness |
| TIPI_8* | Disorganized, careless | Conscientiousness |
| TIPI_9 | Calm, emotionally stable | Emotional Stability |
| TIPI_10* |  Conventional, uncreative | Openness to Experiences |

Asterisk denotes reverse-scored item.


Additional information is available at this [link](https://gosling.psy.utexas.edu/scales-weve-developed/ten-item-personality-measure-tipi/).

*Analysis*

Group personality composition can be assessed as a predictor of group effectiveness. 

* Prior research suggests there is negative relationship between the variance of personality scores within a group and group effectiveness such that heterogeneous groups are less effective and homogeneous groups are more effective (Halfhill et al., 2005). 
  * Mechanism: heterogeneity is associated with conflict.
  * Operationalizing heterogeneity: (1) variance of individual scores, (2) range of individual scores, or (3) proportion of team members that posses a trait 
* Minimum and maximum scores can also potentially have predictive utility under the assumption that one individual can significantly affect group outcome. It is suggested that, for problem solving groups, the max score can be used in analysis.
* For collaborative work, it is expected that relationship-oriented traits will be important: agreeableness and emotional stability (Halfhill et al., 2005). 


### Video Game Experience

The Video Game Experience Measure from Williams (2024) contains 26 questions that examine 5 factors of video game experience. The scoring for the measure is complex and detailed in the tables below. Video game experience will be used as a control variable since participant's with more gaming experience will be more likely to orient themselves and adjust to controls faster than less experienced participants. The task is video game based, and therefore previous gaming experience would be a confounding variable that could explain performance.

| Question  | Response Options  | Scale | Scoring |
| :------------- | :------------- | :------------- | :------------ |
| Q1.1 | 0 to 20 years' experience | 0 - 20 | response x 5 |
| Q1.2 | 0 to 20 years' experience | 0 - 20 | response x 5 |
| Q1.3 | 0 to 20 years' experience | 0 - 20 | response x 5 |
| Q2 | 0 to 100 Age | 0 - 100 | Retained as is (where 100 = n/a) |
| Q3.1 | 1 to 7 | 7-point | response x ~14.29 |
| Q3.2 | 1 to 7 | 7-point | response x ~14.29 |
| Q3.3 | 1 to 7 | 7-point | response x ~14.29 |
| Q3.4 | 1 to 7 | 7-point | response x ~14.29 |
| Q3.5 | 1 to 7 | 7-point | response x ~14.29 |
| Q4 | Control System Preference | 5 options | Retained as is |
| Q5 | Hours per week | Numeric entry | Retained as is |
| Q6 | 1 to 4 proficiency level | 4-point | response x 25 |
| Q7* | 1 to 5 experience level | 5-point | response x 20 |
| Q8.1 | 0 to 100 motivation | 0 - 100 | Retained as is |
| Q8.2 | 0 to 100 motivation | 0 - 100 | Retained as is |
| Q8.3 | 0 to 100 motivation | 0 - 100 | Retained as is |
| Q9.1 | 0 to 100 motivation | 0 - 100 | Retained as is |
| Q9.2 | 0 to 100 level of skill mastery | 0 - 100 | Retained as is |
| Q9.3 | 0 to 100 level of skill mastery | 0 - 100 | Retained as is |
| Q9.4 | 0 to 100 level of skill mastery | 0 - 100 | Retained as is |
| Q9.5 | 0 to 100 level of skill mastery | 0 - 100 | Retained as is |
| Q9.6 | 0 to 100 level of skill mastery | 0 - 100 | Retained as is |
| Q9.7 | 0 to 100 level of skill mastery | 0 - 100 | Retained as is |
| Q9.8 | 0 to 100 level of skill mastery | 0 - 100 | Retained as is |
| Q10 | -100 to 100 confidence | -100 - 100 | (response + 100) / 2|
| Q11 | 1 to 6 | 6-point | response x ~16.67 |

| VGEM Factor | VGEM Items | Formula for Factor Average Score |
| :---------  | :--------- | :------------------------------- |
| Game-Skill Confidence | Q9.1, Q9.2, Q9.3, Q9.4, Q9.5, Q9.6, Q9.7, Q9.8, Q10 | (Q9.1 + Q9.2 + Q9.3 + Q9.4 + Q9.5 + Q9.6 + Q9.7 + Q9.8 + Q10) / 9 |
| Gaming Lifespan | Q1.1, Q1.2, Q1.3 | (Q1.1 + Q1.2 + Q1.3) / 3 |
| Gaming Intensity | Q3.5, Q8.1, Q9.2, Q9.3, Q11 | (Q3.5 + Q8.1 + Q9.2 + Q9.3 + Q11) / 5 |
| Gaming Frequency | Q3.2, Q3.3 | (Q3.2 + Q3.3) / 2 |
| Gamer Self-efficacy | Q3.2, Q6, Q7 | (Q3.2 + Q6 + Q7) / 3 |

*Q7 scoring is marked incorrectly from the instrument. The question is on a 6-point scale not a 5-point, so for analysis, Q7 was scored as a 6-point scale response.*


### Virtual Reality Usage

A single 5-point Likert scale response is used to measure VR usage from none at all to a great deal.

### Teammate Familiarity

A single 5-point Likert scale response is used to measure teammate familiarity by asking "To what extent are you familiar with your teammate?".

## Post-test Measures

### Team Processes (courtesy of Dr. Olivia Newton)

A measure of team process was used in the study. Specifically, the 10-item short-form version of Mathieu et al. (2020)'s team process measure was administered to participants. The measure contains three subscales representing second-order team process constructs: Transition Processes, Action Processes, and Interpersonal Processes. 

*Scoring*

Responses are provided on a 5-point Likert-type scale: 1 = Not at all; 2 = Very little; 3 = To some extent; 4 = To a great extent; 5 = To a very great extent. The group mean of each subscale is used to calculate the extent to which the team engaged in effective team processes over some period in time.


Transition Processes 
| Label  | Item  | Facet |
| :------------- | :------------- | :------------- |
| mission_analysis_1 | Identify the key challenges that we expect to face? | Mission Analysis |
| goal_specification_1 | Ensure that everyone on our team clearly understands our goals? | Goal Specification |
| strategy_formulation_1 | Develop an overall strategy to guide our team activities? | Strategy Formulation and Planning |


Action Processes 
| Label  | Item  | Facet |
| :------------- | :------------- | :------------- |
| monitoring_progress_1 | Regularly monitor how well we are meeting our team goals? | Monitoring Progress Toward Goals |
| systems_monitoring_1 | Monitor important aspects of our work environment? | Systems Monitoring |
| team_monitoring_1 | Assist each other when help is needed? | Team Monitoring and Backup |
| coordination_1 | Coordinate our activities with one another? | Coordination |

Interpersonal Processes
| Label  | Item  | Facet |
| :------------- | :------------- | :------------- |
| conflict_management_1| Deal with personal conflicts in fair and equitable ways? | Conflict Management |
| motivating_1 | Encourage each other to perform our very best? | Motivating and Confidence Building |
| affect_management_1 | Keep a good emotional balance in the team? | Affect Management |

### Performance Evaluations

One 11-point bipolar question measures the evaluation of the teammate's performance and one 11-point bipolar question measures the personal evaluation of performance. The scales are both 0 to 10 with 0 being "Awful" and 10 being "Excellent".

### Mental Workload

The NASA Task Load Index or NASA-TLX (Hart, 2006) measures perceived mental workload. Workload will be used as one of the response variable to analyze how modality impacts team performance. The NASA-TLX consists of 6 7-point scale responses. This instrument is presented as the raw TLX and therefore each question can be taken individually.

| Label/Facet | Question |
| :---------- | :------- |
| mental_demand | How mentally demanding was the task? |
| physical_demand | How physically demanding was the task? |
| temporal_demand | How hurried or rushed was the pace of the task? |
| performance | How successful were you in accomplishing what you were asked to do? |
| effort | How hard did you have to work to accomplish your level of performance? |
| frustration | How insecure, discouraged, irritated, stressed, and annoyed were you? |

### Perceived Usability

System Usability Scale (SUS) (Brooke, 1995) is administered to provide a secondary measure to how modality predicts performance. This measure will also provide feedback on the task itself which we can use to further refine the task if repeated for a full study. Each question is a 5-point Likert scale response ranging from strongly disagree to strongly agree.

| Label | Question |
| :---- | :------- |
| usability_1 | I think that I would like to use this system frequently |
| usability_2 | I found the system was unnecessarily complex |
| usability_3 | I thought the system was easy to use |
| usability_4 | I think that I would need the support of a technical person to be able to use this system |
| usability_5 | I found the various functions in this system were well integrated |
| usability_6 | I thought there was too much inconsistency in this system |
| usability_7 | I would imagine that most people would learn to use this system very quickly |
| usability_8 | I found the system was very cumbersome to use |
| usability_9 | I felt very confident using this system |
| usability_10 | I needed to learn a lot of things before I could get going with this system |


SUS is scored using the following formula.

$$ SUS = 2.5 ( 20 + \sum (SUS01, SUS03, SUS05, SUS07, SUS09) - \sum (SUS02, SUS04, SUS06, SUS08, SUS10) ) $$


## References

Brooke, J. (1995). SUS: A quick and dirty usability scale. Usability Eval. Ind., 189.

Gosling, S. D., Rentfrow, P. J., & Swann, W. B., Jr. (2003). A very brief measure of the big five personality domains. Journal of Research in Personality, 37, 504-528.

Halfhill, T., Sundstrom, E., Lahner, J., Calderone, W., & Nielsen, T. M. (2005). Group personality composition and group effectiveness: An integrative review of empirical research. Small Group Research, 36(1), 83–105.

Hart, S. G. (2006). Nasa-Task Load Index (NASA-TLX); 20 Years Later. Proceedings of the Human Factors and Ergonomics Society Annual Meeting, 50(9), 904–908. https://doi.org/10.1177/154193120605000909

Mathieu, J. E., Luciano, M. M., D’Innocenzo, L., Klock, E. A., & LePine, J. A. (2020). The development and construct validity of a team processes survey measure. Organizational Research Methods, 23(3), 399–431.

Williams, J. L. (2024). Informing a comprehensive player profile model through the development of a Video game experience measure to support theory of mind in artificial social intelligence. (graduate thesis and dissertation). University of Central Florida, Orlando, FL, United States. Available at: https://stars.library.ucf.edu/etd2023/275