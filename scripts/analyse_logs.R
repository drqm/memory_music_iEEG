setwd('C:/Users/au571303/Documents/projects/memory_music_iEEG')
library(ggplot2)
library(lme4)

files <- list.files('logs', pattern = 'pilot')

# load all pilot files:
d <- data.frame()
for (f in files){
  cdata <- read.table(paste0('logs/',f),sep = ',', header = TRUE)
  if (nrow(d) < 1){
    d <- cdata
  }else{
    d <- rbind(d,cdata)
  }
}
## compute accuracy:

d$acc <- as.numeric(d$type == d$response)
d$type <- as.character(d$type)
#accuracy summary:
prop.table(table(d$subject,d$acc),1)

ggplot(d,aes(type,rt, color = subject)) +
  geom_jitter(width = 0.05) +
  geom_boxplot(alpha = 0.3,
             color = 'black', width = 0.2) +
  geom_violin(color = 'black',
              alpha = 0.2,trim = FALSE)