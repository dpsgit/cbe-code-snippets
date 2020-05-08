# cbe-code-snippets
Code snippets useful for research work at Communities for a Better Environment (CBE).

~~ pums_code_snippets_R.Rmd ~~
This code is in a R Markdown file.
Relevant dataset files (psam_p06.csv, psam_h06.csv) are in same folder as code.
Code is structured in terms of answering three "Questions":

1. What is the geographic distribution of workers (i.e. their PUMA field) in the Petroleum Refining sector (i.e. have a NAICS code of 32411) who work in Contra Costa County (i.e. their Place of Work PUMA is “01300”)? 

2. What is the age, gender, race (for the workers), household income, household size (for their households),  breakdown of workers in the Petroleum Refining sector (i.e. have a NAICS code of 32411) in California? 

3. What are the top 5 most spoken languages (using the LANP variable) in each Census PUMA not in the five most commonly spoken languages statewide?

Code should return data frames or vectors that answer these three questions (though a data dictionary may be needed to translate variable codes (i.e. language codes to corresponding languages))
