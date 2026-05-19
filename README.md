# GitHubProject

A small Python project with an interactive [Dash](https://dash.plotly.com/) dashboard and a simple script.

## Contents

| File       | Description |
|------------|-------------|
| `test.py`  | Interactive bar chart dashboard: filter fruit sales by city |
| `test1.py` | Minimal example script |

## Requirements

- Python 3.8+
- [Dash](https://pypi.org/project/dash/)
- [Plotly](https://pypi.org/project/plotly/)
- [pandas](https://pypi.org/project/pandas/)

Install dependencies:

```bash
pip install dash plotly pandas
```

## Running the dashboard

From the project root:

```bash
python test.py
```

Open the URL shown in the terminal (typically `http://127.0.0.1:8050/`).

### Features (`test.py`)

- Sample dataset of fruit amounts by city (SF, Montreal)
- Dropdown to select a city
- Bar chart updates when the city changes
- Label showing the selected city

## Running the example script

```bash
python test1.py
```

## Repository

https://github.com/AvichaiAmrad/GitHubProject.git
