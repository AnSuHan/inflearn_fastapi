from dash import Dash, dash_table, html, dcc, Input, Output, State
from api_helper import call_api

import plotly.express as px
import pandas as pd
import json

# Dash 앱 설정
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# DataTable과 버튼을 포함한 레이아웃 생성
app.layout = html.Div(className='container mt-5', children=[
    dcc.Tabs(id='tabs', value='read', children=[
        dcc.Tab(label='Read', value='read', className='btn-dark', style={'color': 'black'}),
        dcc.Tab(label='Create', value='create', className='btn-primary', style={'color': 'black'}),
        dcc.Tab(label='Update', value='update', className='btn-success', style={'color': 'black'}),
        dcc.Tab(label='Delete', value='delete', className='btn-danger', style={'color': 'black'}),
        dcc.Tab(label='Visualization', value='visualization', className='btn-primary', style={'color': 'black'})
    ]),
    html.Div(id='tabs-content')
])

# 탭 내용 생성 콜백 함수
@app.callback(
    Output('tabs-content', 'children'),
    [Input('tabs', 'value')]
)
def render_content(tab):
    if tab == 'read':
        response = call_api("/v1/gangnamgu-population", 'GET')
        response_data = json.loads(response.content)
        data = response_data['items']
        return html.Div(className='container mt-5', children=[
                html.H1("Data Read Form"),
                dash_table.DataTable(
                id='datatable-interactivity',
                data=data,
                columns=[{'name': i, 'id': i} for i in data[0].keys()],
                style_header={'backgroundColor': '#343a40', 'color': 'white', 'textAlign': 'center'},
                style_cell={
                    'backgroundColor': '#f8f9fa', 
                    'color': '#343a40',
                    'textAlign': 'center',
                    'fontFamily': 'Arial'
                },
                style_data_conditional=[
                    {'if': {'row_index': 'odd'}, 'backgroundColor': '#e9ecef'}
                ])
            ])
    elif tab == 'create':
        return html.Div(className='container mt-5', children=[
            html.H1("Data Creation Form"),
            html.Div(className='row mt-3', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='form-group', children=[
                        html.Label('Sex Ratio:'),
                        dcc.Input(id='sex-ratio', type='number', value=0, className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Male Population:'),
                        dcc.Input(id='male-population', type='number', value=0, className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Female Population:'),
                        dcc.Input(id='female-population', type='number', value=0, className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Total Population:'),
                        dcc.Input(id='total-population', type='number', value=0, className='form-control')
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='form-group', children=[
                        html.Label('Number of Households:'),
                        dcc.Input(id='number-of-households', type='number', value=0, className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Administrative Agency:'),
                        dcc.Input(id='administrative-agency', type='text', value='', className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Number of People per Household:'),
                        dcc.Input(id='number-of-people-per-household', type='number', value=0, className='form-control')
                    ])
                ])
            ]),
            html.Button('Create', id='create-button', n_clicks=0, className='btn btn-primary mt-3'),
            html.Div(id='create-status', className='mt-3')
        ])
    elif tab == 'update':
        return html.Div(className='container mt-5', children=[
            html.H1("Data Update Form"),
            html.Div(className='row mt-3', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='form-group', children=[
                        html.Label('ID:'),
                        dcc.Input(id='update-id', type='text', className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Sex Ratio:'),
                        dcc.Input(id='update-sex-ratio', type='number', value=0, className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Male Population:'),
                        dcc.Input(id='update-male-population', type='number', value=0, className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Female Population:'),
                        dcc.Input(id='update-female-population', type='number', value=0, className='form-control')
                    ])
                ]),
                html.Div(className='col-md-6', children=[
                    html.Div(className='form-group', children=[
                        html.Label('Number of Households:'),
                        dcc.Input(id='update-number-of-households', type='number', value=0, className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Administrative Agency:'),
                        dcc.Input(id='update-administrative-agency', type='text', value='', className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Number of People per Household:'),
                        dcc.Input(id='update-number-of-people-per-household', type='number', value=0, className='form-control')
                    ]),
                    html.Div(className='form-group', children=[
                        html.Label('Total Population:'),
                        dcc.Input(id='update-total-population', type='number', value=0, className='form-control')
                    ])
                ])
            ]),
            html.Button('Update', id='update-button', n_clicks=0, className='btn btn-success mt-3'),
            html.Div(id='update-status', className='mt-3')
        ])
    elif tab == 'delete':
        return html.Div(className='container mt-5', children=[
            html.H1("Data Deletion Form"),
            html.Div(className='row mt-3', children=[
                html.Div(className='col-md-6', children=[
                    html.Div(className='form-group', children=[
                        html.Label('ID:'),
                        dcc.Input(id='delete-id', type='text', className='form-control')
                    ])
                ])
            ]),
            html.Button('Delete', id='delete-button', n_clicks=0, className='btn btn-danger mt-3'),
            html.Div(id='delete-status', className='mt-3')
        ])
    elif tab == 'visualization':
        # 데이터 불러오기
        response = call_api("/v1/gangnamgu-population", 'GET')
        response_data = json.loads(response.content)
        data = response_data['items']

        # 데이터 프레임 생성
        df = pd.DataFrame(data)

        # 산점도 생성
        scatter_fig = px.scatter(df, x='male_population', y='female_population', 
                                 title='Male vs Female Population',
                                 labels={'male_population': 'Male Population', 'female_population': 'Female Population'},
                                 template="discrete+background+watermark")
    
        # 히스토그램 생성
        histogram_fig = px.histogram(df, x='total_population', 
                                     title='Total Population Distribution',
                                     labels={'total_population': 'Total Population'})
    
        # 선 그래프 생성
        line_fig = px.line(df, x='administrative_agency', y='total_population', 
                           title='Total Population Over Administrative Agency',
                           labels={'administrative_agency': 'Administrative Agency', 'total_population': 'Total Population'},
                           template="discrete+background+watermark")
    
        # 박스 플롯 생성
        box_fig = px.box(df, y='sex_ratio', 
                         title='Sex Ratio Box Plot',
                         labels={'sex_ratio': 'Sex Ratio'},
                         template="discrete+background+watermark")
    
        # 파이 차트 생성
        pie_fig = px.pie(df, values='number_of_households', names='administrative_agency', 
                         title='Number of Households by Administrative Agency',
                         labels={'number_of_households': 'Number of Households', 'administrative_agency': 'Administrative Agency'},
                         template="discrete+background+watermark")
    
        # 시각화를 표시하기 위한 dcc.Graph 추가
        visualization_layout = html.Div([
            dcc.Graph(figure=scatter_fig),
            dcc.Graph(figure=histogram_fig),
            dcc.Graph(figure=line_fig),
            dcc.Graph(figure=box_fig),
            dcc.Graph(figure=pie_fig)
        ])
    
        return visualization_layout

# Create 버튼 클릭 시 호출되는 콜백 함수
@app.callback(
    Output('create-status', 'children'),
    [Input('create-button', 'n_clicks')],
    [State('sex-ratio', 'value'),
     State('male-population', 'value'),
     State('female-population', 'value'),
     State('number-of-households', 'value'),
     State('administrative-agency', 'value'),
     State('number-of-people-per-household', 'value'),
     State('total-population', 'value')]
)
def create_data(n_clicks, sex_ratio, male_population, female_population, number_of_households, administrative_agency, number_of_people_per_household, total_population):
    if n_clicks:
        # Create API 호출 코드 작성
        data = {
            'sex_ratio': sex_ratio,
            'male_population': male_population,
            'female_population': female_population,
            'number_of_households': number_of_households,
            'administrative_agency': administrative_agency,
            'number_of_people_per_household': number_of_people_per_household,
            'total_population' : total_population
        }

        response = call_api("/v1/gangnamgu-population", 'POST', data)

        response_data = json.loads(response.content)

        if response.status_code == 200:
            return response_data['message']
        else:
            return "Failed to create data. Error: {}".format(response.text)
    else:
        return ""

# Delete 버튼 클릭 시 호출되는 콜백 함수
@app.callback(
    Output('delete-status', 'children'),
    [Input('delete-button', 'n_clicks')],
    [State('delete-id', 'value')]
)
def delete_data(n_clicks, delete_id):
    if n_clicks:
        # Delete API 호출 코드 작성
        if not delete_id:
            return "Please enter an ID."
        else:
            response = call_api(f"/v1/gangnamgu-population/{delete_id}", 'DELETE')
            if response.status_code == 200:
                return "Data deleted successfully."
            else:
                return "Failed to delete data. Error: {}".format(response.text)
    else:
        return ""

# Update 버튼 클릭 시 호출되는 콜백 함수
@app.callback(
    Output('update-status', 'children'),
    [Input('update-button', 'n_clicks')],
    [State('update-id', 'value'),
     State('update-sex-ratio', 'value'),
     State('update-male-population', 'value'),
     State('update-female-population', 'value'),
     State('update-number-of-households', 'value'),
     State('update-administrative-agency', 'value'),
     State('update-number-of-people-per-household', 'value'),
     State('update-total-population', 'value')]
)
def update_data(n_clicks, update_id, sex_ratio, male_population, female_population, number_of_households, administrative_agency, number_of_people_per_household, total_population):
    if n_clicks:
        # Update API 호출 코드 작성
        if not update_id:
            return "Please enter an ID."
        else:
            data = {
                'sex_ratio': sex_ratio,
                'male_population': male_population,
                'female_population': female_population,
                'number_of_households': number_of_households,
                'administrative_agency': administrative_agency,
                'number_of_people_per_household': number_of_people_per_household,
                'total_population' : total_population
            }

            response = call_api(f"/v1/gangnamgu-population/{update_id}", 'PUT', data)
            
            response_data = json.loads(response.content)

            if response.status_code == 200:
                return response_data['message']
            else:
                return "Failed to update data. Error: {}".format(response.text)
    else:
        return ""

if __name__ == '__main__':
    app.run(debug=True)
