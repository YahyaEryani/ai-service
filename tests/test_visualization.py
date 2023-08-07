import sys
sys.path.append('C:\\Users\\Yahya Al-Eryani\\Documents\\ai-service')
from app.visualization.charts import generate_chart

def test_chart_generation():
    data = {"A": 1, "B": 2}
    chart_path = generate_chart(data, "pie")
    assert chart_path.endswith(".png")
