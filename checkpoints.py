import ipywidgets as widgets
import json

# Load the JSON data
with open('easyshayan.json') as file:
    data = json.load(file)

# Create a function to filter the model names based on the search query
def filter_model_names(search_query):
    return [model['modelName'] for model in data if search_query.lower() in model['modelName'].lower()]

# Create a function to filter the version names based on the selected model name
def filter_version_names(selected_model):
    model = next((model for model in data if model['modelName'] == selected_model), None)
    if model:
        return [version['versionName'] for version in model['modelVersions']]
    return []

# Create a function to handle the model name dropdown change event
def on_model_change(change):
    selected_model = change['new']
    version_names = filter_version_names(selected_model)
    version_dropdown.options = version_names

# Create the search input widget
search_input = widgets.Text(
    value='',
    placeholder='Search Model Name',
    description='Search:',
    disabled=False
)

# Create the model name dropdown widget
model_names = filter_model_names('')
model_dropdown = widgets.Dropdown(
    options=model_names,
    description='Model:',
    disabled=False
)

# Create the version name dropdown widget
version_names = filter_version_names(model_dropdown.value)
version_dropdown = widgets.Dropdown(
    options=version_names,
    description='Version:',
    disabled=False
)

# Attach the model name dropdown change event handler
model_dropdown.observe(on_model_change, names='value')

# Create a function to update the model names based on the search query
def on_search_change(change):
    search_query = change['new']
    model_names = filter_model_names(search_query)
    model_dropdown.options = model_names

# Attach the search input change event handler
search_input.observe(on_search_change, names='value')

# Display the widgets
display(search_input)
display(model_dropdown)
display(version_dropdown)
