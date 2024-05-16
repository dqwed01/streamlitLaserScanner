import streamlit as st
import pyvista as pv
from stpyvista import stpyvista as stpv
from streamlit_image_comparison import image_comparison as im_comparison
import cv2
import time

pv.start_xvfb()
st.set_page_config("Laser Scanner")
modelImg = st.empty()
resultsImg = st.empty()

def showModel():
    st.title("Output")
    st.info("""3D model of scanned object""")
    
    plotter = pv.Plotter(windows_size=[400,400])
    mesh = pv.Cube(center=(0, 0, 0))
    
    plotter.add_mesh(
        mesh,
        scalars="My scalar",
        cmap="prism",
        show_edges=True,
        edge_color="#110000",
        ambient=0.2,
    )
    
    plotter.view_isometric()
    plotter.background_color = 'white'
    
    stpv(plotter, key="pv_cube")

def showResults():
    st.info("""Gaussian Blurring""")
    im_comparison(
        img1="rotated_image.png",
        img2="blurred.png",
        label1="Original",
        label2="Blurred",
    )

    st.info("""Canny Edge Detection""")
    im_comparison(
        img1="blurred.png",
        img2="canny.png",
        label1="Blurred",
        label2="Edged",
    )

    st.info("""Graph Plotting""")
    im_comparison(
        img1="canny.png",
        img2="laser_line_graph.png",
        label1="Edged",
        label2="Graphed",
    )

def scan():
    global resultsImg
    global modelImg
    scanText = st.sidebar.empty()
    scanText.text("Scanner is running")
    time.sleep(2)
    scanText.text("Scanning Complete !")
    modelImg.empty()
    resultsImg.empty()
    showModel()
    showResults()
    
def stop():
    st.sidebar.write("Stopping scan")

def disable():
    st.sidebar.write("Locking device")
    while True:
        continue

st.title("Laser Scanner Webpage")

st.sidebar.write("Select one of the buttons to operate the Laser Scanner")
st.sidebar.title("Options")
buttonStart = st.sidebar.button("Start Scanning", on_click=scan)
buttonStop = st.sidebar.button("Stop Scanning", on_click=stop)
buttonDisable = st.sidebar.button("Disactivate Scanner", on_click=disable)



