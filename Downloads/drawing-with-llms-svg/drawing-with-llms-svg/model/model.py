class Model:
    def __init__(self):
        pass

    def predict(self, prompt: str) -> str:
        # Generate SVG code based on prompt
        svg_code = f"""<svg height="100" width="100">
  <text x="10" y="50" font-size="14">{prompt}</text>
</svg>"""
        return svg_code
