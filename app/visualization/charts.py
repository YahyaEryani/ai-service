import matplotlib.pyplot as plt

def generate_chart(data: dict, chart_type: str) -> str:
    """
    Generate a chart based on the provided data and chart type.
    Currently, this function only supports pie charts for demonstration purposes.
    """
    if chart_type == "pie":
        return generate_pie_chart(data)
    if chart_type == "bar":
         return generate_bar_chart(data)
    # Add other chart types as needed
    raise ValueError(f"Unsupported chart type: {chart_type}")


def generate_pie_chart(data: dict) -> str:
    """
    Generate a pie chart and save it as an image file. Returns the file path.
    """
    labels = list(data.keys())
    sizes = list(data.values())

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    file_path = "pie_chart.png"
    plt.savefig(file_path)
    return file_path

def generate_bar_chart(data):
    # Assuming 'data' is a dictionary like {'category1': value1, 'category2': value2,...}
    names = list(data.keys())
    values = list(data.values())

    # Create bar chart
    plt.figure(figsize=(10, 5))  # size is optional
    plt.bar(names, values)
    
    # You may want to save your figure instead of displaying it directly,
    # especially if you're running this in a server environment.
    plt.savefig('bar_chart.png')
    return 'bar_chart.png'