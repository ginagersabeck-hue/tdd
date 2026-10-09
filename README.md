# tdd

# Forest-Fire Emissions and GDP

## Introduction

For this project, I wanted to see if there was a relationship between a country's GDP and its forest-fire emissions. My hypothesis was that forest-fire emissions would increase as GDP increased because economic growth can lead to more industrial activity, land development, and other changes that affect the environment. I wanted to see if this pattern appeared in different countries or if the relationship varied.

I looked at Brazil, Canada, and Australia using forest-fire emissions data from the Agrofood CO2 Emission dataset and GDP data from the IMF GDP dataset. I analyzed each country separately.

## Methods

I used Python to read the two CSV files and match forest-fire emissions with GDP for the same country and year. I wrote functions to read the data, find the correct columns, and filter the rows for each country. I also made sure to skip years where emissions or GDP data were missing or where the year was not available in both datasets.

After matching the data, I created a scatter plot for each country using Matplotlib. GDP is on the x-axis, and forest-fire emissions are on the y-axis. I used `src/scatter.py` to generate the plots for Brazil, Canada, and Australia.

## Results

Overall, I did not find a clear relationship between GDP and forest-fire emissions across the three countries. My original hypothesis was that emissions would increase as GDP increased, but the plots did not show a consistent upward trend.

### Brazil

![Brazil forest-fire emissions versus GDP](results/brazil.png)

Brazil had a pretty sporadic pattern, and there was no obvious relationship between GDP and forest-fire emissions. Emissions varied across different GDP values, so GDP alone did not seem to explain the changes in forest-fire emissions.

### Canada

![Canada forest-fire emissions versus GDP](results/canada.png)

Canada also did not show a clear trend. The highest forest-fire emissions occurred in a year when GDP was relatively lower. This was different from what I expected, since I thought higher GDP would generally go along with higher emissions.

### Australia

![Australia forest-fire emissions versus GDP](results/australia.png)

Australia's results were a little more mixed. There seemed to be a slight downward trend in part of the plot, but the two highest forest-fire emission values also occurred at the highest GDP values. Those two points fit my original hypothesis, but the overall pattern was not consistently positive.

### What I found overall

Based on these plots, my hypothesis was not consistently supported. Brazil showed a sporadic pattern, Canada had no clear trend, and Australia had a mix of patterns. This suggests that the relationship between GDP and forest-fire emissions may be more complicated than I originally expected.

## Reproducing the Analysis

Download the datasets into the `data/` directory:

```bash
mkdir -p data
curl -L "https://docs.google.com/uc?export=download&id=1AsXP_OGs1O_TDeXiZjk3fYV1SrG4vwXF" -o data/Agrofood_co2_emission.csv
curl -L "https://docs.google.com/uc?export=download&id=19YEPysdnK7VCXuAe9Og9pwYkNT5CbQzr" -o data/IMF_GDP.csv
```

Generate the plots from the repository's root directory:

```bash
mkdir -p results
python src/scatter.py --country Brazil --out results/brazil.png
python src/scatter.py --country Canada --out results/canada.png
python src/scatter.py --country Australia --out results/australia.png
```

Run the tests:

```bash
python test/unit/test_fire_gdp.py
bash test/func/test_fire_gdp.sh
```


