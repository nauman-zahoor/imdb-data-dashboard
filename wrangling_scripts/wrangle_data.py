import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # read_data_file and process 
    data = pd.read_csv('./data/imdb_data.csv')
    cols = ['primaryTitle','startYear','runtimeMinutes','genres','averageRating']
    data = data[cols]
    data.columns = ['movie','year','runtime','generes','rating']
    
    
    # top 20 and bottom 20 rated movies

    data_top = data.sort_values('rating',ascending=False).reset_index(drop=True).loc[:20,['movie','rating']]
    data_bottom = data.sort_values('rating',ascending=True).reset_index(drop=True).loc[:20,['movie','rating']]


    # first chart plots top 20 movies
    
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = data_top.movie.tolist(),
      y = data_top.rating.tolist(),
      mode = 'markers'
      )
    )

    layout_one = dict(title = "IMDB's Highest Rated Top 20 Movies",
                xaxis = dict(title = 'Movie Title'),
                yaxis = dict(title = 'IMDB Rating'),
                )

# second chart plots bottom 20 movies
    graph_two = []

    graph_two.append(
      go.Scatter(
      x = data_bottom.movie.tolist(),
      y = data_bottom.rating.tolist(),
      mode = 'markers'
      )
    )

    layout_two = dict(title = "IMDB's Lowest Rated Bottom 20 Movies",
                xaxis = dict(title = 'Movie title',),
                yaxis = dict(title = 'IMDB Rating'),
                )

    
####################################
    # # top and bottom rated movies vs year

    top = data.groupby('year')['rating'].mean().sort_values(ascending=False)
    top = pd.DataFrame(top)
    top.loc[:,'year'] = top.index
    top = top.reset_index(drop=True)

    bottom = data.groupby('year')['rating'].mean().sort_values(ascending=True)
    bottom = pd.DataFrame(bottom)
    bottom.loc[:,'year'] = bottom.index
    bottom = bottom.reset_index(drop=True)

    top20 = top[:20]
    bottom20 = bottom[:20]

# third chart plots top rated movie's year and their average rating
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = top20.year.tolist(),
      y = top20.rating.tolist(),
      mode = 'markers'
      )
    )

    layout_three = dict(title = "IMDB's Highest Rated Movie's average rating <br> vs Year they came out ",
                xaxis = dict(title = 'Year of Release'),
                yaxis = dict(title = 'Average Rating')
                       )
    
# fourth  chart plots bottom rated movie's year and their average rating
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = bottom20.year.tolist(),
      y = bottom20.rating.tolist(),
      mode = 'markers'
      )
    )

    layout_four = dict(title =  "IMDB's Lowest Rated Movie's average rating <br> vs Year they came out ",
                xaxis = dict(title = 'Year of Release'),
                yaxis = dict(title = 'Average rating'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures