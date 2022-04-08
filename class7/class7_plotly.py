import plotly.express as px
import pandas as pd
import pandas_datareader as web
import plotly.graph_objects as go
from plotly.subplots import make_subplots

iris = px.data.iris()
tips = px.data.tips()

# fig = px.line(x=[1,2,3], y=[1,2,3])
# # fig.show(renderer = 'browser')
#
# #######################################
# # load data
# #######################################
# dfAAPL = web.DataReader("AAPL", data_source="yahoo", start="2016-01-01")
# dfORCL = web.DataReader("ORCL", data_source="yahoo", start="2016-01-01")
# dfTSLA = web.DataReader("TSLA", data_source="yahoo", start="2016-01-01")
# dfIBM = web.DataReader("IBM", data_source="yahoo", start="2016-01-01")
# dfYELP = web.DataReader("YELP", data_source="yahoo", start="2016-01-01")
# dfMSFT = web.DataReader("MSFT", data_source="yahoo", start="2016-01-01")
#
# df1 = dfAAPL.copy()
# df1['company'] = 'AAPL'
#
# df2 = dfORCL.copy()
# df2['company'] = 'ORCL'
#
# df3 = dfTSLA.copy()
# df3['company'] = 'TSLA'
#
# df4 = dfIBM.copy()
# df4['company'] = 'IBM'
#
# df5 = dfYELP.copy()
# df5['company'] = 'YELP'
#
# df6 = dfMSFT.copy()
# df6['company'] = 'MSFT'
#
# frames = [df1,df2,df3,df4,df5,df6]
# result = pd.concat(frames)
#
# # lineplot
# fig = px.line(data_frame=result, x=result.index, y=result.Close, color='company')
# fig.show(renderer = 'browser')
#
# # barplot
# fig = px.bar(result, x= 'company', y='Close')
# fig.show(renderer = 'browser')
# # stack
# fig = px.bar(iris, x='sepal_length',
#              y='sepal_width',
#              color='species',
#              hover_data=['petal_width'],
#              barmode='stack',
#              orientation='h')
# fig.show(renderer = 'browser')
# # group
# fig = px.bar(tips, x='total_bill', y='day',
#              color='sex',barmode='group')
# fig.show(renderer = 'browser')
# # update_xaxes
# fig = px.bar(tips, x='total_bill', y='day',
#              color='sex',barmode='group').update_xaxes(categoryorder='total descending')
# fig.show(renderer = 'browser')
# #
# fig = px.bar(tips, x='day',
#              color='smoker')
# fig.update_xaxes(categoryorder='total ascending')
# fig.show(renderer = 'browser')
# #scatter_matrix
# features = iris.columns.tolist()
# fig = px.scatter_matrix(iris,
#                         dimensions=features,
#                         color='species')
# fig.update_traces(diagonal_visible=False)
# fig.show(renderer = 'browser')
# # histogram
# fig = px.histogram(tips,
#                         x='total_bill',
#                         nbins=50)
# fig.show(renderer = 'browser')
# #
# fig = px.histogram(tips,
#                    x='total_bill',
#                    y='tip',
#                    color='smoker',
#                    marginal='histogram',
#                     nbins=50)
# fig.show(renderer = 'browser')
# # go
# fig = go.Figure(data = [go.Histogram(x=iris['sepal_width'],
#                 nbinsx = 50)])
# fig.show(renderer = 'browser')
#
# fig = go.Figure(data = [go.Histogram(y=iris['sepal_width'])])
# fig.show(renderer = 'browser')
# # go.Figure()
# fig = go.Figure()
# fig.add_trace((go.Histogram(x = iris['sepal_width'])))
# fig.add_trace((go.Histogram(x = iris['sepal_length'])))
# fig.update_layout(barmode='stack')
# fig.show(renderer = 'browser')
#
# pie name来分类
fig = px.pie(tips,
             values='total_bill',
             names='day')
fig.show(renderer = 'browser')
# # box
# fig = px.box(tips,
#              x='day',
#              y='total_bill')
# fig.show(renderer = 'browser')
# # violin
# fig = px.violin(tips,
#              x='day',
#              y='total_bill')
# fig.show(renderer = 'browser')
#
# # subplots
# fig = make_subplots(rows=1, cols=2)
# fig.add_trace(go.Scatter(x=[1,2,3],y=[5,6,7]),
#               row=1, col=1)
# fig.add_trace(go.Scatter(x=[15,25,35],y=[1,6,7]),
#               row=1, col=2)
# fig.show(renderer = 'browser')
# # subplots title,
# fig = make_subplots(rows=1, cols=2,
#                     subplot_titles=('Stock Volume Pie','Stock Volume Bar'),
#                     specs=[[{'type':'pie'},{'type':'bar'}]])
# fig.add_trace(go.Pie(values = result.Volume, labels=result.company),
#               row=1, col=1)
# fig.add_trace(go.Bar(x=result['company'],y=result['Volume']),
#               row=1, col=2)
# fig.show(renderer = 'browser')
# #
# fig = make_subplots(rows=1,cols=2, subplot_titles=('Pie plot','Pie plot2'),specs=[[{'type':'pie'},{'type':'pie'}]])
# fig.add_trace(go.Pie(values=tips['total_bill'], labels=tips['day']), row=1, col=1)
# fig.add_trace(go.Pie(values=tips['total_bill'], labels=tips['day']), row=1, col=2)
# fig.show()


















