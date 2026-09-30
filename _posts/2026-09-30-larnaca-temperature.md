---
layout: post
title: Temperature change in Larnaca, Cyprus
tags: [climate, python, data science]
css:
  - "/css/cyprus-post.css"
js:
  - "/js/cyprus-post.js"
---

I wanted a good temperature dataset for a project I could build on, eventually incorporating changing energy prices in a dynamic geopolitical situation. Cyprus interested me because of its demand for air conditioning and dependence on imported energy. In 2024, net imports supplied [88% of its energy needs](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/wdn-20260318-1), while cooling accounted for [16% of household energy use](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260708-1), which is the highest share in the EU. I started with NOAA’s nearly complete daily temperature record for Larnaca from 1978 through 2024 to examine how temperatures have changed.

## Where the observations come from

<iframe class="cyprus-visual" src="{{ '/img/cyprus/larnaca-map.html' | relative_url }}" title="Interactive map of the Larnaca temperature station in Cyprus" width="100%" height="690" style="border:0;" loading="lazy"></iframe>

The daily temperatures come from NOAA's Larnaca station on the coast of Cyprus. Click the marker for station details, or zoom in to explore its surroundings.

I used 1978 through 2024 because the 1977 record has large gaps and the saved dataset ends partway through 2025. Only 17 of 17,167 days were missing during the selected period. I kept all 47 years and calculated each annual average from the available daily readings.

[NOAA daily data](https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/CY000176090.dly) · [Data definitions](https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt) · [Station metadata](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt) · [Analysis notebook](https://github.com/rileythejones/01-climate-fall-template/blob/main/06-cyprus-temperature.ipynb)


## How temperatures have changed

<iframe class="cyprus-visual" src="{{ '/img/cyprus/temperature-trend.html' | relative_url }}" title="Larnaca annual temperatures and linear warming trend, 1978–2024" width="100%" height="690" style="border:0;" loading="lazy"></iframe>

I estimated the warming trend using [ordinary least squares (OLS) regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html), with year predicting annual mean temperature. OLS fits a straight line by minimizing the sum of squared differences between observed and predicted temperatures. The estimated warming rate is **0.57°C per decade**, equal to about **2.6°C between 1978 and 2024**.

[Download the chart]({{ '/img/cyprus/temperature-trend.png' | relative_url }}) · [Annual data]({{ '/data/cyprus/larnaca-annual.csv' | relative_url }})

| Data used | Years included | OLS warming estimate |
|---|---:|---:|
| All years, 1978–2024 | 47 | 0.57°C per decade |
| Years with no missing days, 1978–2023 | 41 | 0.55°C per decade |

Excluding the six years with missing days changed the warming estimate from 0.57°C to 0.55°C per decade. I kept all 47 years in the main analysis because dropping nearly complete years removed useful data with little effect on the estimated trend.

This result only describes one station in Larnaca. Comparing records from nearby stations such as [Nicosia (Athalassa), Akrotiri, and Paphos](https://www.mesonet.agron.iastate.edu/sites/networks.php?network=CY__ASOS&station=LCLK), and checking for changes in station location, equipment, or surrounding development, would help determine how well it represents warming across Cyprus.

I want to build on this analysis by combining daily temperatures with electricity prices and household energy use. That would help show how changes in demand for air conditioning and changes in energy prices combine to affect household costs.
