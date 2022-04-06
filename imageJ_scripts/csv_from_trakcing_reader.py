from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import numpy as np
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('tracking_26hF0silnenieb.csv', encoding='unicode_escape')
#all_tracking_time = np.arange(0, 1300, 1.577)
#df['TIME'] = all_tracking_time
cols_names = [*df]

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                cols_names,
                'TRACK_ID',
                id='xaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='xaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                cols_names,
                'NUMBER_SPOTS',
                id='yaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='yaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    # dcc.Slider(
    #         df['TIME'].min(),
    #         df['TIME'].max(),
    #         step=None,
    #         id='time--slider',
    #         value=df['TIME'].max(),
    #         marks={str(time): str(time) for time in df['TIME'].unique()},
    #     )
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    #Input('time--slider', 'value')
)
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type): #time_value):
    #dff = df[df['TIME'] == time_value]

    # fig = px.scatter(x=dff[xaxis_column_name],
    #                  y=dff[yaxis_column_name])

    fig = px.scatter(x=df[xaxis_column_name], y=df[yaxis_column_name])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)



