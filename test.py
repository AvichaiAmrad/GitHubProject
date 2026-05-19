import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Interactive Fruit Dashboard Example"),
    dcc.Dropdown(
        id='city-dropdown',
        options=[{'label': c, 'value': c} for c in df['City'].unique()],
        value='SF',
        clearable=False
    ),
    dcc.Graph(id='fruit-bar-plot'),
    html.Div(id='selected-city', style={'marginTop': 20, 'fontWeight': 'bold'})
])

@app.callback(
    [Output('fruit-bar-plot', 'figure'),
     Output('selected-city', 'children')],
    [Input('city-dropdown', 'value')]
)
def update_bar_chart(selected_city):
    filtered_df = df[df['City'] == selected_city]
    fig = px.bar(filtered_df, x="Fruit", y="Amount", color="Fruit", barmode="group")
    return fig, f"Selected City: {selected_city}"

if __name__ == '__main__':
    app.run_server(debug=True)