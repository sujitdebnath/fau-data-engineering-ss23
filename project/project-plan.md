# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This data science project aims to analyze **Berlin's cycling facilities and weather conditions** to determine if it's a suitable city for an enthusiastic cyclist to live in. The project will use two open data sources: [mobilithek](https://mobilithek.info/), which contains information on cycling facilities in Berlin, and [meteostat](https://meteostat.net/en/), which provides weather and climate data of Berlin. The analysis will focus on identifying patterns and trends in the cycling facilities in Berlin to assess the suitability for cycling in the city. Additionally, the analysis will examine the weather and climate data to determine if Berlin's weather and climate conditions are conducive for cycling.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis of cycling facilities and weather conditions in Berlin can have several significant impacts on the targeted audience, including:
1. **Enthusiast Cyclists:** The analysis can help enthusiastic cyclists make an informed decision about whether Berlin is a suitable city for their lifestyle by providing insights into the quality of cycling facilities and weather conditions in the city. It can help alleviate the pain of uncertainty about the cycling conditions in the city and make it easier for cyclists to plan their routes and activities.
2. **Berlin City Planners:** The analysis can also provide insights for city planners to improve the quality and safety of cycling facilities in Berlin. By identifying the most common types of cycling facilities, assessing their quality, and pinpointing areas of the city with the most and least cycling infrastructure, city planners can prioritize investments in areas that need improvement, potentially making cycling in the city more accessible and enjoyable for enthusiasts.
3. **Cycling Tourists:** The analysis can also benefit cycling tourists by providing insights into the quality of cycling facilities and weather conditions in Berlin. Tourists can use the insights to plan their cycling routes and activities, potentially attracting more tourism to the city.

Overall, the analysis can help alleviate the pains of uncertainty about the cycling conditions in Berlin for enthusiasts, provide insights for city planners to improve the quality and safety of cycling facilities in the city, and benefit cycling tourists planning to visit Berlin.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Mobilithek
* Metadata URL: [https://mobilithek.info/offers/-6901989592576801458](https://mobilithek.info/offers/-8141096470822855854)
* Data Type: CSV

This data source contains Berlin's cycling facilities which consist of cycle paths, cycle lanes, protective lanes, and special bus lanes, with and without shared use by cyclists.

### Datasource2: Meteostat
* Metadata URL: [https://dev.meteostat.net/bulk/monthly.html](https://dev.meteostat.net/bulk/monthly.html)
* Data Type: CSV

This data source will provide weather and climate data in Berlin, including average air temperature, daily minimum and maximum air temperature, monthly precipitation total, maximum snow depth, average wind direction and speed, peak wind gust, average sea-level air pressure, and monthly sunshine total.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data Collection, Preprocessing, and Storage [#1][i1]
2. Data Analysis and Visualization [#2][i2]
3. Automated Data Pipeline [#3][i3]
4. Automated Tests for the Project [#4][i4]
5. Continuous Integration Pipeline for the Project [#5][i5]
6. Deploy the Project Using GitHub Pages [#6][i6]

[i1]: https://github.com/sujitdebnath/fau-data-engineering-ss23/issues/1
[i2]: https://github.com/sujitdebnath/fau-data-engineering-ss23/issues/2
[i3]: https://github.com/sujitdebnath/fau-data-engineering-ss23/issues/3
[i4]: https://github.com/sujitdebnath/fau-data-engineering-ss23/issues/4
[i5]: https://github.com/sujitdebnath/fau-data-engineering-ss23/issues/5
[i6]: https://github.com/sujitdebnath/fau-data-engineering-ss23/issues/6
