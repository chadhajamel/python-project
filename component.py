import streamlit.components.v1 as components

def hello_component(name):
    components.html(f""" 
 <div style='font-size: 100px'
 onclick='alert("clicked!")'
 Hello {name}> </div>
""")

hello_component('world')

#you can deploy app with heroku