# Analyses for The Canaveral, We Have a Problem Experiment
# Conducted for HCC 8500 spring '25 with Dr. Nathan McNeese


# Import libraries
library(dplyr)
library(ggplot2)
library(lubridate) 
library(gghighlight)
library(RColorBrewer)
library(gridExtra)
library(tidyr)
library(stringr)
library(R.utils)
library(MetBrewer)
library(car)


# Prepare and clean data -------------------------------------------------------
# Import data files
preData <- read.csv("../HCC8500-pre_04-03.csv")
postData <- read.csv("../HCC8500-post_04-03.csv")
experimentData <- read.csv("../Experiment_Log.csv")
movementData <- read.csv("../Single_Metric.csv")

# Remove unnecessary rows and columns
# first two rows are subheadings/labels and can be removed
preData <- preData[- (1:2), ] %>%
  select(-StartDate, -EndDate, -Status, -IPAddress, -Progress, -Duration..in.seconds., -Finished, -RecordedDate, -ResponseId, -RecipientLastName, -RecipientFirstName, -RecipientEmail, -ExternalReference, -LocationLatitude, -LocationLongitude, -DistributionChannel, -UserLanguage)
head(preData)

postData <- postData[- (1:2), ] %>%
  select(-StartDate, -EndDate, -Status, -IPAddress, -Progress, -Duration..in.seconds., -Finished, -RecordedDate, -ResponseId, -RecipientLastName, -RecipientFirstName, -RecipientEmail, -ExternalReference, -LocationLatitude, -LocationLongitude, -DistributionChannel, -UserLanguage)


# fix input errors
preData$pid <- toupper(preData$pid)

# Prepare experiment data to add to survey dataframes
experimentData_long <- experimentData %>%
  tidyr::pivot_longer(cols = c(VR.PID, PC.PID), 
                      names_to = "PID_Type", 
                      values_to = "pid") %>%
  select(Session.ID, pid, PID_Type, Number_of_tasks, Solar_Flares_Avoided)

# Join dataframes
cwhapData <- preData %>%
  left_join(postData, by = "pid") %>%
  left_join(experimentData_long, by = "pid") %>%
  left_join(movementData, by = "Session.ID")


# Create a vector for the column numbers we want make numeric
col_nums <- c(c(2:14), c(16:20), c(23:72), c(78:83))

# Apply as.numeric() to those columns then print out data type to check
cwhapData[col_nums] <- sapply(cwhapData[col_nums], as.numeric)
sapply(cwhapData, class)

# Remove vector we no longer need
rm(col_nums)


# Score Measures ---------------------------------------------------------------


# Calculate TIPI scores (Gosling et al., 2003)
cwhapData <- cwhapData %>%
  mutate(extraversion = (tipi_1 + (8 - tipi_6)) / 2) %>%
  mutate(agreeableness = (tipi_2 + (8 - tipi_7)) / 2) %>%
  mutate(conscientiousness = (tipi_3 + (8 - tipi_8)) / 2) %>%
  mutate(emotionalStability = (tipi_4 + (8 - tipi_9)) / 2) %>%
  mutate(openness = (tipi_5 + (8 - tipi_10)) / 2)

# Remove used columns
cwhapData <- cwhapData %>%
  select(-starts_with(c("tipi")))



# Calculate scores for VGEM (Williams, 2024)
# Prepare the initial data that needs to be re-scaled
cwhapData <- cwhapData %>%
  mutate(Q1._1 = Q1._1 * 5 ) %>%
  mutate(Q1._2 = Q1._2 * 5 ) %>%
  mutate(Q1._3 = Q1._3 * 5 ) %>%
  mutate(Q3_1 = Q3_1 * (100/7) ) %>%
  mutate(Q3_2 = Q3_2 * (100/7) ) %>%
  mutate(Q3_3 = Q3_3 * (100/7) ) %>%
  mutate(Q3_4 = Q3_4 * (100/7) ) %>%
  mutate(Q3_5 = Q3_5 * (100/7) ) %>%
  mutate(Q6 = Q6 * 25 ) %>%
  mutate(Q7 = Q7 * (100/6) ) %>%
  mutate(Q10_1 = ( Q10_1 + 100 ) / 2 ) %>%
  mutate(Q11 = Q11 * (100/6) )

cwhapData <- cwhapData %>%
  mutate(skillConfidence = (Q9_1 + Q9_2 + Q9_3 + Q9_4 + Q9_5 + Q9_6 + Q9_7 + Q9_8 + Q10_1) / 9) %>%
  mutate(gameLifespan = (Q1._1 + Q1._2 + Q1._3) / 3 ) %>%
  mutate(gameIntensity = (Q3_5 + Q8_1 + Q9_2 + Q9_3 + Q11) / 5 ) %>%
  mutate(gameFrequency = (Q3_2 + Q3_3) / 2) %>%
  mutate(gameSelfEfficacy = (Q3_2 + Q6 + Q7) / 3)


# Remove used columns
# Q2, Q4, and Q5 are not used in scoring and can be used as independent data points
cwhapData <- cwhapData %>%
  select(-starts_with(c("Q1.","Q3","Q6","Q7","Q8","Q9","Q10","Q11")))

# Renaming Q2, Q4, and Q5 to better describe the measure
cwhapData <- cwhapData %>%
  rename(onset_age = Q2_1, preferred_device = Q4, hrs_per_week = Q5)




# Calculate scores for team processes measures (Mathieu et al., 2020)
cwhapData <- cwhapData %>%
  mutate(teamprocess_mean = select(., starts_with(c("transition", "action", "interpersonal"))) %>% rowMeans(),
         transition_process_mean = select(., starts_with(c("transition"))) %>% rowMeans(),
         action_process_mean = select(., starts_with(c("action"))) %>% rowMeans(),
         interpersonal_process_mean = select(., starts_with(c("interpersonal"))) %>% rowMeans())

# Remove used columns
cwhapData <- cwhapData %>%
  select(-c("transition_proc_1","transition_proc_2","transition_proc_3")) %>%
  select(-c("action_proc_1","action_proc_2","action_proc_3","action_proc_4")) %>%
  select(-c("interpersonal_proc_1","interpersonal_proc_2","interpersonal_proc_3"))


# Calculate scores for SUS (Brooke, 1995)
cwhapData <- cwhapData %>%
  mutate(sus = 2.5 * (20 + (select(., usability, usability.2, usability.4, usability.6, usability.8 ) %>% rowSums()) - (select(., usability.1, usability.3, usability.5, usability.7, usability.9) %>% rowSums()) ))

# Remove used columns
cwhapData <- cwhapData %>%
  select(-starts_with(c("usability")))



# Conduct analyses -------------------------------------------------------------
#
# Set directory to save plots
setwd("../Plots")


# Median Split Movement as a Predictor -----------------------------------------

# median splits, high = 1 low = 0
movement_stats <- cwhapData %>%
  filter(PID_Type == "VR.PID") %>% # the data is duplicated in the VR and PC rows so selecting one will stop doubling the values
  mutate(total_vr_movement = Left_Hand_Magnitude + Right_Hand_Magnitude + Head_Magnitude) %>%
  mutate(total_movement = total_vr_movement + Mouse_Magnitude) %>%
  mutate(category_left = 
           case_when(
             Left_Hand_Magnitude > median(Left_Hand_Magnitude) ~ "High",
             Left_Hand_Magnitude < median(Left_Hand_Magnitude) ~ "Low",
           )
  ) %>%
  mutate(category_right = 
           case_when(
             Right_Hand_Magnitude > median(Right_Hand_Magnitude) ~ "High",
             Right_Hand_Magnitude < median(Right_Hand_Magnitude) ~ "Low",
           )
  ) %>%
  mutate(category_head = 
           case_when(
             Head_Magnitude > median(Head_Magnitude) ~ "High",
             Head_Magnitude < median(Head_Magnitude) ~ "Low",
           )
  ) %>%
  mutate(category_mouse = 
            case_when(
              Mouse_Magnitude > median(Mouse_Magnitude) ~ "High",
              Mouse_Magnitude < median(Mouse_Magnitude) ~ "Low",
            )
  ) %>%
  mutate(category_vr_total = 
           case_when(
             total_vr_movement > median(total_vr_movement) ~ "High",
             total_vr_movement < median(total_vr_movement) ~ "Low",
           )
  ) %>%
  mutate(category_total = 
           case_when(
             total_movement > median(total_movement) ~ "High",
             total_movement < median(total_movement) ~ "Low",
           )
  )

# Plot distribution
png(filename = "task_performance_distribution.png",
    width = 2100, height = 2400,
    units = "px", res = 330)

barplot(table(movement_stats$Number_of_tasks), main="Distribution of Team Performance", 
        xlab="Number of Tasks Completed", ylab = "Count")

dev.off()

# Plot relationship between predictor and outcome
png(filename = "left_hand_success_relationship.png",
    width = 2100, height = 2400,
    units = "px", res = 330)

ggplot(movement_stats, aes(x=Left_Hand_Magnitude, y=Number_of_tasks)) +
  geom_point(size=3) +
  geom_smooth(method="loess", se=FALSE, color="#F9D14AFF") +
  labs(title="Relationship between Left Hand Magnitude and Task Performance",
       x="Left Hand Magnitude", y="Number of Tasks Completed") +
  theme_minimal() 

dev.off()


# Box plot
png(filename = "left_hand_median_split.png",
    width = 2100, height = 2400,
    units = "px", res = 330)
boxplot(Number_of_tasks ~ category_left, data = movement_stats, 
        xlab = "Movement Group", ylab = "Number of Tasks Completed", main = "Left Hand Movement",
        ylim = c(0, 4),
        col = c("#7C4B73FF", "#E78429FF"))
dev.off()

png(filename = "right_hand_median_split.png",
    width = 2100, height = 2400,
    units = "px", res = 330)
boxplot(Number_of_tasks ~ category_right, data = movement_stats, 
        xlab = "Movement Group", ylab = "Number of Tasks Completed", main="Right Hand Movement",
        ylim = c(0, 4),
        col = c("#7C4B73FF", "#E78429FF"))
dev.off()

png(filename = "head_median_split.png",
    width = 2100, height = 2400,
    units = "px", res = 330)
boxplot(Number_of_tasks ~ category_head, data = movement_stats, 
        xlab = "Movement Group", ylab = "Number of Tasks Completed", main="Head Movement",
        ylim = c(0, 4),
        col = c("#7C4B73FF", "#E78429FF"))
dev.off()

png(filename = "vr_median_split.png",
    width = 2100, height = 2400,
    units = "px", res = 330)
boxplot(Number_of_tasks ~ category_vr_total, data = movement_stats, 
        xlab = "Movement Group", ylab = "Number of Tasks Completed", main="VR Total Movement",
        ylim = c(0, 4),
        col = c("#7C4B73FF", "#E78429FF"))
dev.off()

png(filename = "total_median_split.png",
    width = 2100, height = 2400,
    units = "px", res = 330)
boxplot(Number_of_tasks ~ category_total, data = movement_stats, 
        xlab = "Movement Group", ylab = "Number of Tasks Completed", main="Total Movement of Both Team Members",
        ylim = c(0, 4),
        col = c("#7C4B73FF", "#E78429FF"))
dev.off()

png(filename = "mouse_median_split.png",
    width = 2100, height = 2400,
    units = "px", res = 330)
boxplot(Number_of_tasks ~ category_mouse, data = movement_stats, 
        xlab = "Movement Group", ylab = "Number of Tasks Completed", main="Mouse Movement",
        ylim = c(0, 4),
        col = c("#7C4B73FF", "#E78429FF"))
dev.off()

# None of the median split analyses were significant
# Compute the analysis of variance
res.aov <- aov(Number_of_tasks ~ Left_Hand_Magnitude, data = movement_stats)
# Summary of the analysis
print(summary(res.aov))

# Check that we meet the assumptions
plot(res.aov, 1)
plot(res.aov, 2)
# There are outliers, but due to the small sample size, we have decided not to remove them

# Test for homogeneity of variances, non-significant means that the assumption is met
print(leveneTest(Number_of_tasks ~ category_total, data = movement_stats))


# Spearman's correlation due to the small sample size
cor_test <- cor.test(movement_stats$Left_Hand_Magnitude, movement_stats$Number_of_tasks, method="spearman")
print(cor_test)

# Looking at left hand magnitude by itself was a predictor with a positive correlation with movement


