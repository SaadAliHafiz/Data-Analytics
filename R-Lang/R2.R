library(readxl)
employee_data <- read_excel("Employee.xls", 
                            sheet = "Employee data", col_types = c("numeric", 
                                                                   "text", "date", "numeric", "numeric", 
                                                                   "numeric", "numeric", "numeric"))
View(employee_data)
str(employee_data)

head(employee_data)
tail(employee_data)
plot(employee_data)
#Same variable function
boxplot(employee_data$ID,employee_data$Salary)
#different variable function
boxplot(employee_data$Salary ~ employee_data$Gender)

