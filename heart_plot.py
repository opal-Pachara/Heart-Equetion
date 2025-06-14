"""Heart plot generation and animation."""
import numpy as np
import plotly.graph_objects as go
from config import (
    PLOT_SIZE, PLOT_POINTS, X_RANGE,
    HEART_COLOR
)

class HeartPlot:
    """Handles the creation and animation of the heart plot."""
    
    def __init__(self):
        """Initialize the heart plot."""
        self.x = np.linspace(X_RANGE[0], X_RANGE[1], PLOT_POINTS)
    
    def calculate_y(self, a):
        """
        Calculate y values for the heart equation.
        
        Args:
            a (float): Parameter controlling the sine wave frequency
        
        Returns:
            numpy.ndarray: Y values for the heart shape
        """
        return (np.power(np.abs(self.x), 2/3) + 
                0.9 * np.sqrt(3.3 - self.x**2) * np.sin(a * np.pi * self.x))
    
    def create_plot(self, a):
        """
        Create a heart-shaped plot using the mathematical equation.
        
        Args:
            a (float): Parameter controlling the sine wave frequency
        
        Returns:
            go.Figure: Plotly figure object containing the heart plot
        """
        y = self.calculate_y(a)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=self.x,
            y=y,
            mode='lines',
            line=dict(color=HEART_COLOR, width=2),
            name='Heart'
        ))
        
        fig.update_layout(
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                scaleanchor="y",
                scaleratio=1,
                autorange=True
            ),
            yaxis=dict(
                showgrid=False,
                showticklabels=False,
                zeroline=False,
                scaleanchor="x",
                scaleratio=1,
                autorange=True
            ),
            height=PLOT_SIZE,
            width=PLOT_SIZE
        )
        
        return fig
 