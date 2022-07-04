# Types of plots

#Strip chart
#Histogram
#Scatterplot/plot
#qqnorm plot
#Barplot
#Mosaic plot
#Boxplot
#Practice

library(readxl)
employee_data <- read_excel("Employee.xls", col_types = c("numeric", 
                                                     "text", "date", "numeric", "numeric", 
                                                     "numeric", "numeric", "numeric"))
View(employee_data)

#STRIP CHART
#for one variable
stripchart(employee_data$Salary)
# for two variables
stripchart(employee_data$ID ~ employee_data$Salary)
#it is use for to check the distribution of the data


#HISTOGRAM

hist(employee_data$Salary)
hist(employee_data$Minority)

#Plot/Scatter Plot

plot(employee_data$ID ~ employee_data$Salary)

#QQnorm Plot

qqnorm(employee_data$Salary)

#BARPLOT

barplot(employee_data$Salary)

#MOSAIC PLOT

mosaicplot(~employee_data$Gender+employee_data$Salary)

#BoxPlot

boxplot(employee_data$Salary ~ employee_data$Gender)
