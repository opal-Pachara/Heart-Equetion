"""Styling utilities for the heart animation application."""
from config import (
    FONT_FAMILY, HEART_COLOR, TEXT_COLOR, BACKGROUND_COLOR,
    TITLE, MESSAGE, LOADING_MESSAGE, ACCENT_COLOR
)

class StyleManager:
    """Manages the styling of the application."""
    
    @staticmethod
    def get_font_links():
        """Return the font preconnect and stylesheet links."""
        return """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c&display=swap" rel="stylesheet">
        """
    
    @staticmethod
    def get_custom_css():
        """Return the custom CSS styles."""
        return f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c&display=swap');
            
            * {{
                font-family: 'M PLUS Rounded 1c', sans-serif;
            }}

            /* Ensure LaTeX equations use their default font */
            .stMarkdown .katex {{
                font-family: KaTeX_Main, 'Times New Roman', serif !important;
            }}
            
            .main {{
                background-color: {BACKGROUND_COLOR};
            }}
            
            .stApp {{
                background-color: {BACKGROUND_COLOR};
            }}
            
            h1, h2, h3, p {{
                font-family: 'M PLUS Rounded 1c', sans-serif;
                color: {TEXT_COLOR};
            }}
            
            .heart-message {{
                font-family: 'M PLUS Rounded 1c', sans-serif;
                font-size: 1.2rem;
                color: {HEART_COLOR};
                text-align: center;
                margin: 1rem 0;
                font-weight: 500;
                text-shadow: 0 0 10px rgba(255, 107, 107, 0.3);
                padding: 0 0.5rem;
            }}

            .title-text {{
                font-family: 'M PLUS Rounded 1c', sans-serif;
                font-size: 2rem;
                font-weight: 700;
                text-align: center;
                color: {TEXT_COLOR};
                margin-bottom: 1.5rem;
                padding: 0 1rem;
                text-shadow: 0 0 10px rgba(224, 224, 224, 0.2);
            }}

            .highlight-name {{
                color: {HEART_COLOR};
                font-weight: 700;
                font-size: 2.2rem;
                text-shadow: 0 0 15px rgba(255, 107, 107, 0.5);
                padding: 0 0.2rem;
                position: relative;
                display: inline-block;
            }}

            .highlight-name::after {{
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                width: 100%;
                height: 2px;
                background: {HEART_COLOR};
                box-shadow: 0 0 10px {HEART_COLOR};
            }}

            .loading-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                width: 100%;
                position: fixed;
                top: 0;
                left: 0;
                background-color: {BACKGROUND_COLOR};
                z-index: 9999;
                opacity: 1;
                transition: opacity 0.5s ease-out;
            }}

            .loading-message {{
                font-family: 'M PLUS Rounded 1c', sans-serif;
                font-size: 1rem;
                color: {HEART_COLOR};
                text-align: center;
                margin-top: 0.8rem;
                font-weight: 400;
                padding: 0 1rem;
            }}

            .loading-heart {{
                width: 60px;
                height: 60px;
                position: relative;
                animation: pulse 1.5s ease-in-out infinite;
                margin-bottom: 1.5rem;
                filter: drop-shadow(0 0 20px {HEART_COLOR});
            }}

            .loading-heart::before,
            .loading-heart::after {{
                content: '';
                position: absolute;
                width: 30px;
                height: 50px;
                background: {HEART_COLOR};
                border-radius: 30px 30px 0 0;
                box-shadow: 0 0 30px {HEART_COLOR};
            }}

            .loading-heart::before {{
                left: 30px;
                transform: rotate(-45deg);
                transform-origin: 0 100%;
            }}

            .loading-heart::after {{
                left: 0;
                transform: rotate(45deg);
                transform-origin: 100% 100%;
            }}

            @keyframes pulse {{
                0% {{ 
                    transform: scale(1);
                    filter: drop-shadow(0 0 20px {HEART_COLOR});
                }}
                50% {{ 
                    transform: scale(1.2);
                    filter: drop-shadow(0 0 30px {HEART_COLOR});
                }}
                100% {{ 
                    transform: scale(1);
                    filter: drop-shadow(0 0 20px {HEART_COLOR});
                }}
            }}

            /* iPhone 11 and similar devices */
            @media screen and (max-width: 414px) {{
                .heart-message {{
                    font-size: 1rem;
                    margin: 0.8rem 0;
                    padding: 0 0.5rem;
                }}
                
                .title-text {{
                    font-size: 1.4rem;
                    margin-bottom: 1rem;
                    padding: 0 0.5rem;
                }}

                .highlight-name {{
                    font-size: 1.6rem;
                }}

                .loading-message {{
                    font-size: 0.9rem;
                    padding: 0 0.5rem;
                }}

                .loading-heart {{
                    width: 45px;
                    height: 45px;
                    margin-bottom: 1rem;
                }}

                .loading-heart::before,
                .loading-heart::after {{
                    width: 22px;
                    height: 38px;
                }}
            }}

            /* Smaller devices */
            @media screen and (max-width: 375px) {{
                .heart-message {{
                    font-size: 0.9rem;
                }}
                
                .title-text {{
                    font-size: 1.3rem;
                }}

                .highlight-name {{
                    font-size: 1.5rem;
                }}

                .loading-message {{
                    font-size: 0.85rem;
                }}

                .loading-heart {{
                    width: 40px;
                    height: 40px;
                }}

                .loading-heart::before,
                .loading-heart::after {{
                    width: 20px;
                    height: 35px;
                }}
            }}
        </style>
        """
    
    @staticmethod
    def get_title_html():
        """Return the styled title HTML."""
        title_parts = TITLE.split("Jeerapa Pusalee")
        return f"""
        <div class='title-text'>
            {title_parts[0]}<span class='highlight-name'>Jeerapa Pusalee</span>{title_parts[1]}
        </div>
        """
    
    @staticmethod
    def get_message_html():
        """Return the styled message HTML."""
        return f"<div class='heart-message'>{MESSAGE}</div>"

    @staticmethod
    def get_loading_html():
        """Return the loading animation HTML."""
        return f"""
        <div class='loading-container'>
            <div class='loading-heart'></div>
            <div class='loading-message'>{LOADING_MESSAGE}</div>
        </div>
        """ 