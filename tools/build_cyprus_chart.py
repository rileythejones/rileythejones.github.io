"""Build the portfolio chart from the notebook's exported annual data.

Run with base Python 3.11.6: python tools/build_cyprus_chart.py
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, FixedTicker, NumeralTickFormatter
from bokeh.embed import components
from bokeh.resources import INLINE

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"img/cyprus"
annual=pd.read_csv(ROOT/"data/cyprus/larnaca-annual.csv")
summary=json.loads((ROOT/"data/cyprus/trend-summary.json").read_text())
assert annual.year.tolist()==list(range(1978,2025))
assert annual.valid_days.sum()==17150 and annual.missing_days.sum()==17
model=LinearRegression().fit(annual[["year"]],annual.temp_c)
slope=float(model.coef_[0]*10)
assert np.isclose(slope,summary["slope_c_per_decade"],rtol=0,atol=1e-7)
fit=model.predict(annual[["year"]])
BLUE="#246482"
AMBER="#b96818"
INK="#20353e"
TITLE=f"Larnaca’s warming trend: {slope:.2f}°C per decade"
SUBTITLE="Annual mean temperature · 1978–2024 · All 47 years"
source=ColumnDataSource(annual)
chart=figure(height=430,sizing_mode="stretch_width",min_width=260,
             x_range=(1977,2025),y_range=(18,22.2),tools="",toolbar_location=None,
             x_axis_label="Year",y_axis_label="Annual mean temperature (°C)",
             min_border_left=55,min_border_right=16,min_border_top=12,min_border_bottom=42)
chart.line(annual.year,fit,color=AMBER,line_width=2.7,line_dash="dashed")
chart.line("year","temp_c",source=source,line_color=BLUE,line_width=1.5)
points=chart.scatter("year","temp_c",source=source,size=5.5,fill_color=BLUE,line_color="white",line_width=0.8)
chart.add_tools(HoverTool(renderers=[points],mode="vline",tooltips=[
    ("Year","@year{0}"),("Annual average","@temp_c{0.00} °C"),
    ("Days recorded","@valid_days{0} / @expected_days{0}")]))
chart.xaxis.ticker=FixedTicker(ticks=[1980,1990,2000,2010,2020])
chart.yaxis.ticker=FixedTicker(ticks=[18,18.5,19,19.5,20,20.5,21,21.5,22])
chart.yaxis.formatter=NumeralTickFormatter(format="0.0")
chart.xgrid.grid_line_color=None
chart.ygrid.grid_line_color="#e7edef"
chart.outline_line_color=None
chart.axis.axis_line_color="#b7c6cc"
chart.axis.major_tick_line_color=None
chart.axis.minor_tick_line_color=None
chart.axis.major_label_text_color="#526b75"
chart.axis.major_label_text_font="Helvetica"
chart.axis.major_label_text_font_size="11px"
chart.axis.axis_label_text_font="Helvetica"
chart.axis.axis_label_text_font_style="normal"
chart.axis.axis_label_text_font_size="12px"
chart.axis.axis_label_text_color=INK
chart.axis.axis_label_standoff=10
js,div=components(chart)
template='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
__RESOURCES__
<style>
*{box-sizing:border-box}body{margin:0;background:#fff;color:#20353e;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.chart-card{max-width:1100px;margin:auto;padding:20px 24px 12px}h1{font-size:27px;line-height:1.25;font-weight:650;margin:0 0 8px;letter-spacing:-.015em}.subtitle{font-size:13px;color:#617780;margin:0}.legend{display:flex;flex-wrap:wrap;gap:8px 24px;padding:20px 0 6px;font-size:12px;color:#45606c}.legend span{display:inline-flex;gap:8px;align-items:center}.swatch{width:26px;border-top:2px solid #246482;height:0}.swatch.trend{border-top:3px dashed #b96818}.chart-plot{width:100%}.chart-footer{border-top:1px solid #e5ecef;padding-top:11px;margin-top:5px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:6px 18px;font-size:12px;line-height:1.6;color:#61747d}.chart-footer p{margin:0}.chart-footer a{color:#315e71;text-underline-offset:2px}a:focus-visible{outline:3px solid #f5b849;outline-offset:3px}.fallback{width:100%;height:auto}
@media(max-width:600px){.chart-card{padding:17px 10px 10px}h1{font-size:22px}.legend{padding-top:15px;gap:7px 16px}.chart-footer{font-size:11px}}
</style></head><body><main class="chart-card">
<h1>__TITLE__</h1><p class="subtitle">__SUBTITLE__</p>
<div class="legend" aria-label="Chart legend"><span><i class="swatch" aria-hidden="true"></i>Annual average</span><span><i class="swatch trend" aria-hidden="true"></i>Linear trend · +__SLOPE__°C per decade</span></div>
<div class="chart-plot" role="region" aria-label="Annual temperatures at Larnaca from 1978 through 2024, with a rising fitted trend. Hover over a year to see its temperature.">__PLOT__</div>
<noscript><img class="fallback" src="temperature-trend.png" alt="Annual temperatures at Larnaca, 1978–2024, with a fitted warming trend of 0.57 degrees Celsius per decade."></noscript>
<footer class="chart-footer"><p>NOAA CY000176090 · Mean of available daily readings</p><p>Hover over a year · <a href="../../data/cyprus/larnaca-annual.csv" download>Data</a> · <a href="temperature-trend.png" download>PNG</a></p></footer>
</main>__SCRIPT__</body></html>
'''
html=(template.replace("__TITLE__",TITLE).replace("__SUBTITLE__",SUBTITLE)
      .replace("__SLOPE__",f"{slope:.2f}").replace("__RESOURCES__",INLINE.render())
      .replace("__PLOT__",div).replace("__SCRIPT__",js))
(OUT/"temperature-trend.html").write_text(html)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"axes.spines.top":False,"axes.spines.right":False,"axes.labelcolor":INK,"text.color":INK,"axes.edgecolor":"#b7c6cc","xtick.color":"#526b75","ytick.color":"#526b75"})
fig,ax=plt.subplots(figsize=(10.5,5.8))
fig.subplots_adjust(left=.085,right=.98,bottom=.17,top=.74)
fig.text(.085,.93,TITLE,fontsize=19,fontweight="bold",ha="left")
fig.text(.085,.875,SUBTITLE,fontsize=11,color="#617780",ha="left")
trend,=ax.plot(annual.year,fit,color=AMBER,lw=2.5,ls="--",label=f"Linear trend · +{slope:.2f}°C per decade")
observed,=ax.plot(annual.year,annual.temp_c,color=BLUE,lw=1.3,marker="o",ms=4.2,mec="white",mew=.5,label="Annual average")
fig.legend(handles=[observed,trend],loc="upper left",bbox_to_anchor=(.078,.845),frameon=False,ncol=2,fontsize=10)
ax.set(xlabel="Year",ylabel="Annual mean temperature (°C)",xlim=(1977,2025),ylim=(18,22.2))
ax.set_xticks([1980,1990,2000,2010,2020])
ax.set_yticks(np.arange(18,22.1,.5))
ax.set_axisbelow(True)
ax.grid(axis="y",color="#e7edef",lw=.8)
ax.tick_params(axis="both",which="both",length=0,pad=7)
fig.text(.085,.045,"NOAA CY000176090 · Mean of available daily readings · All 47 annual observations",fontsize=9,color="#617780")
fig.savefig(OUT/"temperature-trend.png",dpi=200,facecolor="white")
plt.close(fig)
print(f"Built chart: {len(annual)} years; {slope:.12f} °C/decade; all notebook results matched.")
