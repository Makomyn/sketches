from dash import Dash, html, dcc, Input, Output
import pandas as pd

df = pd.read_excel("patrimonio_df.xlsx")

patrimonios = ['POLTRONAS', 'MONITOR 1', 'MONITOR 2', 'MONITOR 3', 'COMPUTADORES', 
               'TELEFONES', 'MESAS', 'GAVETEIROS', 'FONE DE OUVIDO', 'WEBCAM', 'VENTILADOR'] #IMPLEMENTAR -- COLOCAR MONITORES TODOS EM UMA SÓ COLUNA E SEPARAR VALORES POR VÍRGULA! 

df_long = df.melt(id_vars=['COLABORADORES'], value_vars=patrimonios, 
                  var_name='Patrimônio', value_name='Nº de patrimônio')

df_long = df_long[df_long['Nº de patrimônio'] != 'N.A']

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children=[
        html.H1("Patrimônios - CGISE", style={"textAlign": "center"}),

        html.Label("Colaboradores"), 
        dcc.Dropdown(id="servidor-dropdown",
                     options=[{'label': i, 'value': i} for i in df_long['COLABORADORES'].unique()],
                     value=None),

        html.Br(),

        html.Label("Patrimônio"),
        dcc.Dropdown(id="patrimonio-dropdown", multi=False),

        html.Br(),

        html.Label("Nº de patrimônio"),
        dcc.Dropdown(id="numero-patrimonio-dropdown", multi=False),

        html.Br(),
        
        html.Label("Pesquisa"),
        #COLOCAR AQ PESQUISA GERAL 

    ], style={'font-family': 'Lucida Console', 'padding': 10, 'flex': 1}),
], style={'display': 'flex', 'flexDirection': 'row', 'background-color': '#a9b3d1'})


@app.callback(
    Output('patrimonio-dropdown', 'options'),
    Input('servidor-dropdown', 'value')
)
def update_patrimonios(servidor):
    if servidor is None:
        return []
    patrimônios = df_long[df_long['COLABORADORES'] == servidor]['Patrimônio'].unique()
    return [{'label': p, 'value': p} for p in patrimônios]

@app.callback(
    Output('numero-patrimonio-dropdown', 'options'),
    Input('patrimonio-dropdown', 'value'),
    Input('servidor-dropdown', 'value')
)
def update_numero_patrimonio(patrimonio, servidor):
    if patrimonio is None or servidor is None:
        return []
    
    numero = df_long[(df_long['COLABORADORES'] == servidor) & 
                     (df_long['Patrimônio'] == patrimonio)]['Nº de patrimônio']
    
    numero = numero.dropna().tolist()
    
    return [{'label': n, 'value': n} for n in numero if n]

if __name__ == '__main__':
    app.run(debug=True)
