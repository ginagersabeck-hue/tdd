import argparse
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from fire_gdp import get_fire_gdp_year_data


def main():
    parser = argparse.ArgumentParser(
        description="Plot forest-fire emissions against GDP for a country."
    )
    parser.add_argument(
        "--out",
        default="fire_gdp.png",
        help="Output image filename"
    )
    parser.add_argument(
        "--country",
        default="Brazil",
        help="Country to analyze (default: Brazil)"
    )
    parser.add_argument(
        "--co2",
        default="data/Agrofood_co2_emission.csv",
        help="Path to the CO2 emissions CSV"
    )
    parser.add_argument(
        "--gdp",
        default="data/IMF_GDP.csv",
        help="Path to the GDP CSV"
    )

    args = parser.parse_args()

    data = get_fire_gdp_year_data(
        args.co2,
        args.gdp,
        args.country
    )

    if not data:
        raise ValueError(
            f"No matching fire and GDP data found for {args.country}"
        )

    years = [row[0] for row in data]
    fires = [row[1] for row in data]
    gdp = [row[2] for row in data]

    fig, ax = plt.subplots()
    ax.scatter(gdp, fires)

    ax.set_xlabel("GDP (millions of local currency)")
    ax.set_ylabel("Forest-fire emissions")
    ax.set_title(
        f"Forest-fire emissions vs GDP: {args.country}"
    )

    fig.tight_layout()
    fig.savefig(args.out, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
