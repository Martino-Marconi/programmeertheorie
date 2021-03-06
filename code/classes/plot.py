import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import csv
import random


def make_dataframe(data):
    """
    Add train names and their stops to a dataframe.
    """
    data_items = data.items()
    data_list = list(data_items)
    df = pd.DataFrame(data_list, columns=["train", "stations"]).explode("stations")

    return df


def load_coordinates():
    """
    Get the coordinates of all stations and add them to a dataframe.
    """
    stations = []
    x_coords = []
    y_coords = []

    with open("input/StationsNationaal.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            stations.append(row[0])
            x_coords.append(float(row[2]))
            y_coords.append(float(row[1]))

    coords_df = pd.DataFrame(list(zip(stations, x_coords, y_coords)), columns=["stations", "x", "y"])

    return coords_df


def map_plot(dataframe):
    """
    Plots all train lines onto a map of the netherlands.
    """
    route_data = dataframe
    tmp_data = route_data

    df_geo = gpd.GeoDataFrame(tmp_data, geometry=gpd.points_from_xy(route_data.x, route_data.y))

    # get a dataset from cbsodata and adjust the coordinates
    url = 'https://geodata.nationaalgeoregister.nl/cbsgebiedsindelingen/wfs?request=GetFeature&service=WFS&version=2.0.0&typeName=cbs_gemeente_2017_gegeneraliseerd&outputFormat=json'
    nederland = gpd.read_file(url)
    nederland = nederland.to_crs("EPSG:4326")

    # plot map of the Netherlands
    axis = nederland.plot(color='lightblue', edgecolor='black')
    df_geo.plot(ax=axis, color="black")

    for i in range(1, 20):
        # pick random colors for each line
        r = random.random()
        g = random.random()
        b = random.random()
        color = (r, g, b)

        tmp_df = route_data[route_data["train"] == f"train_{i}"]
        plt.plot(tmp_df["x"], tmp_df["y"], label=f"train_{i}", color=color)

    plt.legend()
    plt.savefig("output/NLplot.png")
