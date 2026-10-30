import pandas as pd

agro_df = pd.read_csv("data/Agrofood_co2_emission.csv")
gdp_df = pd.read_csv("data/IMF_GDP.csv")

# Get intersection of country names
agro_countries = set(agro_df['Area'].unique())
gdp_countries = set(gdp_df['Country'].unique())
COUNTRIES = sorted(list(agro_countries.intersection(gdp_countries)))

# Countries known to lack valid overlapping data in scatter.py
exclude_countries = ["San Marino"]  # Add any others here if they pop up!
COUNTRIES = [c for c in COUNTRIES if c not in exclude_countries]
rule all:
    input:
        expand("results/{country}.png", country=COUNTRIES)

rule make_plots:
    input:
        script = "src/scatter.py",
        agro_data = "data/Agrofood_co2_emission.csv",
        gdp_data = "data/IMF_GDP.csv"
    output:
        "results/{country}.png"
    shell:
        """
        python {input.script} \
            --country "{wildcards.country}" \
            --out "{output}"
        """
