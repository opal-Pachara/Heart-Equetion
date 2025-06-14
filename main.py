"""Main application file for the heart animation."""
import streamlit as st
import time
import numpy as np
from heart_plot import HeartPlot
from styles import StyleManager
from config import LOADING_DELAY

def main():
    """Main application function."""
    st.set_page_config(
        page_title="Heart Animation",
        page_icon="❤️",
        layout="centered"
    )

    # Add custom CSS and font links
    st.markdown(StyleManager.get_font_links(), unsafe_allow_html=True)
    st.markdown(StyleManager.get_custom_css(), unsafe_allow_html=True)

    # Initialize session state for loading
    if 'loading_complete' not in st.session_state:
        st.session_state.loading_complete = False

    # Show loading animation if not complete
    if not st.session_state.loading_complete:
        loading_container = st.container()
        with loading_container:
            st.markdown(StyleManager.get_loading_html(), unsafe_allow_html=True)
            time.sleep(LOADING_DELAY)
            st.session_state.loading_complete = True
            st.rerun()
    
    # Show the main content after loading
    st.markdown(StyleManager.get_title_html(), unsafe_allow_html=True)
    
    # Create placeholder for the equation
    equation_placeholder = st.empty()
    
    # Create placeholder for the plot
    plot_placeholder = st.empty()
    
    # Create heart plot instance
    heart_plot = HeartPlot()
    
    # Animate the heart from a=0.01 to a=30
    a_values = np.linspace(0.01, 30, 300)  # 300 steps for smooth animation
    progress_bar = st.progress(0)
    
    for i, a in enumerate(a_values):
        # Show the equation with current a value (compact version)
        equation_placeholder.latex(
            fr'''\small f(x) = |x|^{{\frac{{2}}{{3}}}} + 0.9\sqrt{{3.3-x^2}}\sin(\textcolor{{red}}{{{a:.2f}}}\pi x)'''
        )
        
        # Update the plot
        fig = heart_plot.create_plot(a)
        plot_placeholder.plotly_chart(fig, use_container_width=True)
        
        # Update progress bar
        progress = (i + 1) / len(a_values)
        progress_bar.progress(progress)
        
        # Small delay for smooth animation
        time.sleep(0.02)
    
    # Wait for 3 seconds before showing the message
    time.sleep(3)
    
    # Show the message
    st.markdown(StyleManager.get_message_html(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()