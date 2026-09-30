---
layout: post
title: Temperature change in Larnaca, Cyprus
tags: [climate, python, data science]
---

<!-- Working title. Build and review this post one section at a time. -->

## Where the observations come from

<iframe src="{{ '/img/cyprus/larnaca-map.html' | relative_url }}" title="Interactive map of the Larnaca temperature station in Cyprus" width="100%" height="690" style="border:0;" loading="lazy"></iframe>

The daily temperatures come from NOAA's Larnaca station on the coast of Cyprus. Click the marker for station details, or zoom in to explore its surroundings.

[Station metadata](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt) · [Analysis notebook](https://github.com/rileythejones/01-climate-fall-template/blob/main/06-cyprus-temperature.ipynb)


## How temperatures have changed

<iframe src="{{ '/img/cyprus/temperature-trend.html' | relative_url }}" title="Larnaca annual temperatures and linear warming trend, 1978–2024" width="100%" height="690" style="border:0;" loading="lazy"></iframe>

Temperatures vary from year to year. Across the full record, the fitted trend rises by about **2.6°C between 1978 and 2024**.

[Download the chart]({{ '/img/cyprus/temperature-trend.png' | relative_url }}) · [Annual data]({{ '/data/cyprus/larnaca-annual.csv' | relative_url }})
