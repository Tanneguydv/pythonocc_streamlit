import streamlit as st
import streamlit.components.v1 as components

import os
import sys
sys.path.append(os.path.realpath(os.curdir))

from lib import threejs_renderer_st
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Section, BRepAlgoAPI_Fuse
from OCC.Core.gp import gp_Pnt

import threading
from multiprocessing import Queue

class app():
    def __init__(self):
        self.my_renderer = threejs_renderer_st.ThreejsRenderer()
        self.queue = Queue()
        self.setup_streamlit()
        
    def setup_streamlit(self):
        st.set_page_config(layout='wide')
        st.sidebar.header("Best Game Ever")
        st.sidebar.markdown("Move the sphere to touch the box")      
        
        self.create_sliders()  
        self.create_shape()
        
        address= self.queue.get()
        components.iframe(address, height=600, width=1100)

        if self.bool :
            st.sidebar.success("Touch, you're awesome!", icon="✅") 
        else :
            st.sidebar.warning("Not touch, try again", icon="⚠️")    
            
    def create_sliders(self):
        self.x = st.sidebar.slider("move x",0 ,200, 0)
        self.y = st.sidebar.slider("move y",0 ,200, 0)
        self.z = st.sidebar.slider("move z",0 ,200, 0)

    def create_shape(self):   
        shapes = [] 
        box = (BRepPrimAPI_MakeBox(gp_Pnt(100, 100, 100),10, 10, 10).Shape(), (0.7, 1, 0.5), 0.9) 
        shapes.append(box)
        sphere = (BRepPrimAPI_MakeSphere(gp_Pnt(self.x, self.y, self.z), 5).Shape(), (0.8, 0.3, 0.1), 0)
        shapes.append(sphere)
        section = BRepAlgoAPI_Section(box[0], sphere[0]).Shape()
        if section.NbChildren() > 0:
            self.bool = True
            shapes.clear()
            fused = (BRepAlgoAPI_Fuse(box[0], sphere[0]).Shape(), (1, 1, 0.9), 0.5)
            shapes.append(fused)
        else:
            self.bool = False
        p = threading.Thread(target=self.render, args=(self.queue, shapes))
        p.start()

    def render(self, q, shapes): 
        for shape in shapes:
            (shap, color, transp) = shape
            self.my_renderer.DisplayShape(shap, color=color, transparency=transp)
        self.my_renderer
        thread = threading.Thread(target=self.render_thread, args=(q,))
        thread.start()

    def render_thread(self, q):
        address= self.my_renderer.render()
        q.put(address)

if __name__ == '__main__':
    ap = app()


# streamlit run path_to_your_file/example_streamlit_pythonocc.py


