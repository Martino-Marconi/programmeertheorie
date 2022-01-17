
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
from shapely.geometry import point, linestring
import csv
import random



def make_dataframe(data):

    data_items = data.items()
    data_list = list(data_items)
    df = pd.DataFrame(data_list, columns=["train", "stations"]).explode("stations")

    return df
    
def load_coordinates():
    stations = []
    x_coords = []
    y_coords = []
    with open("data/StationsNationaal.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            stations.append(row[0])
            x_coords.append(float(row[2]))
            y_coords.append(float(row[1]))

    coords_df = pd.DataFrame(list(zip(stations, x_coords, y_coords)), columns=["stations", "x", "y"])

    return coords_df


def map_plot(dataframe):

    route_data = dataframe
    tmp_data = route_data

    df_geo = gpd.GeoDataFrame(tmp_data, geometry = gpd.points_from_xy(route_data.x, route_data.y))

    # get built in dataset from geopandas

    world_data = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    # print(world_data.head(10))

    # plot world map
    axis = world_data[world_data.name == "Netherlands"].plot(color = 'lightblue', edgecolor='black')

    df_geo.plot(ax=axis, color="black")

    for i in range(1, 8):

        r = random.random()
        g = random.random()
        b = random.random()
        color = (r, g, b)

        tmp_df = route_data[route_data["train"] == f"train_{i}"]
        plt.plot(tmp_df["x"], tmp_df["y"], label=f"train_{i}", color=color)
       
    plt.legend()
    plt.savefig("plots/NLplot.png")
