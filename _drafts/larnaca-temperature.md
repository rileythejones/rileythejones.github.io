---
layout: post
title: Temperature change in Larnaca, Cyprus
tags: [climate, python, data science]
---

<!-- Working title. Build and review this post one section at a time. -->

I wanted a good temperature dataset for a project I could build on, eventually incorporating changing energy prices in a dynamic geopolitical situation. Cyprus interested me because of its demand for air conditioning and dependence on imported energy. In 2024, net imports supplied [88% of its energy needs](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/wdn-20260318-1), while cooling accounted for [16% of household energy use](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260708-1), which is the highest share in the EU. I started with NOAA’s nearly complete daily temperature record for Larnaca from 1978 through 2024 to examine how temperatures have changed.

## Where the observations come from

<iframe src="{{ '/img/cyprus/larnaca-map.html' | relative_url }}" title="Interactive map of the Larnaca temperature station in Cyprus" width="100%" height="690" style="border:0;" loading="lazy"></iframe>

The daily temperatures come from NOAA's Larnaca station on the coast of Cyprus. Click the marker for station details, or zoom in to explore its surroundings.

I used 1978 through 2024 because the 1977 record has large gaps and the saved dataset ends partway through 2025. Only 17 of 17,167 days were missing during the selected period. I kept all 47 years and calculated each annual average from the available daily readings.

[Station metadata](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt) · [Analysis notebook](https://github.com/rileythejones/01-climate-fall-template/blob/main/06-cyprus-temperature.ipynb)


## How temperatures have changed

<iframe src="{{ '/img/cyprus/temperature-trend.html' | relative_url }}" title="Larnaca annual temperatures and linear warming trend, 1978–2024" width="100%" height="690" style="border:0;" loading="lazy"></iframe>

Temperatures vary from year to year. Across the full record, the fitted trend rises by about **2.6°C between 1978 and 2024**.

[Download the chart]({{ '/img/cyprus/temperature-trend.png' | relative_url }}) · [Annual data]({{ '/data/cyprus/larnaca-annual.csv' | relative_url }})
