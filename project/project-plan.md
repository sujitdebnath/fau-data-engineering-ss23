# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This data science project aims to analyze **the weather and climate conditions of Köln and its bicycle traffic** generated from several automatic counting stations throughout the city to determine if Köln is a suitable city for an enthusiastic cyclist to live in. The project will use two open data sources: [mobilithek](https://mobilithek.info/), which contains information on bicycle traffic in Köln, and [meteostat](https://meteostat.net/en/), which provides weather and climate data of Köln. The analysis will focus on identifying patterns and trends in bicycle traffic in Köln throughout the years to assess the suitability for cycling in the city. Additionally, the analysis will examine the weather and climate data to determine if Köln's weather and climate conditions are conducive for cycling.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis of weather and climate conditions, along with bicycle traffic in Köln, can have several significant impacts on the targeted audience, including:
1. **Enthusiast Cyclists:** The analysis can help enthusiastic cyclists make an informed decision about whether Köln is a suitable city for their lifestyle by providing insights into bicycle traffic depending on weather conditions in the city. It can help alleviate the pain of uncertainty about the cycling conditions in the city and make it easier for cyclists to plan their routes and activities.
2. **Cycling Tourists:** The analysis can also benefit cycling tourists by providing insights into bicycle traffic depending on weather conditions in Köln. Tourists can use the insights to plan their cycling routes and activities, potentially attracting more tourism to the city.
3. **Köln City Planners:** The analysis can also provide insights for city planners to improve the quality and safety of cycling facilities in Köln. By identifying the pinpointing areas of the city with the most and least cycling infrastructure, city planners can prioritize investments in areas that need improvement, potentially making cycling in the city more accessible and enjoyable for enthusiasts.

Overall, the analysis can help alleviate the pains of uncertainty about the cycling conditions in Köln for enthusiasts, provide insights for city planners to improve the quality and safety of cycling facilities in the city, and benefit cycling tourists planning to visit Köln.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Bicycle Traffic Data of Köln
* Metadata URL: [https://mobilithek.info/offers/-2236641647976866002](https://mobilithek.info/offers/-2236641647976866002)
* Sample Data URL: [https://offenedaten-koeln.de/sites/default/files/Fahrrad_Zaehlstellen_Koeln_2016.csv](https://offenedaten-koeln.de/sites/default/files/Fahrrad_Zaehlstellen_Koeln_2016.csv)
* Data Type: CSV

This data source contains Köln's bicycle traffic generated from several [automatic counting stations](http://www.eco-public.com/ParcPublic/?id=677) throughout the city from 2009.

### Datasource2: Meteostat
* Metadata URL: [https://dev.meteostat.net/bulk/monthly.html](https://dev.meteostat.net/bulk/monthly.html)
* Sample Data URL: [https://bulk.meteostat.net/v2/monthly/{station}.csv.gz](https://bulk.meteostat.net/v2/monthly/{station}.csv.gz), Station-id of Köln = '10513', 'D2968'
* Data Type: CSV

This data source will provide weather and climate data in Köln, including average air temperature, daily minimum and maximum air temperature, monthly precipitation total, maximum snow depth, average wind direction and speed, peak wind gust, average sea-level air pressure, and monthly sunshine total.

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
