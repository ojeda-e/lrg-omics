import plotly.express as px
from .template import *


def median_intensity(rawtools_matrix, title=None):
    fig = px.area(rawtools_matrix, 
                  x=None,
                  y=['PeakParentScanIntensity', 
                     'Ms1MedianIntensity', 
                     'Ms2MedianIntensity'],
                  title=title
                  )
    fig.update_layout(title='Intensity')
    fig.update_layout(yaxis_type="log")
    fig.update_layout(legend_title_text='')
    return fig


def filltime(rawtools_matrix, title=None):
    fig = px.area(rawtools_matrix, x=None, 
                  y=["Ms1FillTime", "Ms2FillTime"], 
                  color_discrete_sequence=px.colors.qualitative.Bold,
                  title=title)
    fig.add_trace(
        go.Scatter(
            x=None,
            y=rawtools_matrix['DutyCycle(s)'],
            mode="lines",
            line=go.scatter.Line(color="black"),
            showlegend=True,
            name='DutyCycle(s)',
        )
    )
    fig.update_layout(legend_title_text='')
    return fig

def histograms(rawtools_matrix, cols=['ParentIonMass'], title=None):
    fig = px.histogram(rawtools_matrix[cols[0]])
    if len(cols) == 1:
        fig.update_layout(title=cols[0])
        fig.update_layout(showlegend=False)
    for col in cols[1:]:
        fig.add_trace(
                go.Histogram(
                        x=rawtools_matrix[col], 
                        visible = 'legendonly', 
                        name=col,
                        title=title))
    fig.update_layout(legend_title_text='')
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    return fig